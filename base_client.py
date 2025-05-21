"""
-Ofastbear
base_client.py rev 1.0.1
Kyle Holter Vogel, Joseph Melancon, Jonah Stroup
University of North Dakota
2024 February 01
"""

import random

from game.client.user_client import UserClient
from game.commander_clash.character.character import Character
from game.common.enums import *
from game.common.map.game_board import GameBoard
from game.common.team_manager import TeamManager
from game.utils.vector import Vector
from game.commander_clash.moves.moves import *
from game.commander_clash.moves.effects import *


class State(Enum):
    HEALTHY = auto()
    UNHEALTHY = auto()


class Client(UserClient):
    # Variables and info you want to save between turns go here
    def __init__(self):
        super().__init__()

        # Our implementation relies heavily on Fultra, given they're
        # the only real force on the team. These properties track if
        # Healers need to take action on Fultra.
        self.FultraNeedsHealing = False
        self.FultraSwapped = True

    def team_data(self) -> tuple[str, tuple[SelectGeneric, SelectLeader, SelectGeneric]]:
        """
        Returns your team name (to be shown on visualizer) and a tuple of enums representing the characters you
        want for your team. The tuple of the team must be ordered as (Generic, Leader, Generic). If an enum is not
        placed in the correct order (e.g., (Generic, Leader, Leader)), whichever selection is incorrect will be
        swapped with a default value of Generic Attacker.
        """
        return '-Ofastbear', (SelectGeneric.GEN_HEALER, SelectLeader.FULTRA, SelectGeneric.GEN_HEALER)

    def first_turn_init(self, team_manager: TeamManager):
        """
        This is where you can put setup for things that should happen at the beginning of the first turn. This can be
        edited as needed.
        """
        self.country = team_manager.country_type
        self.my_team = team_manager.team
        self.enemy_country: CountryType = CountryType.TURPIS if team_manager.country_type == CountryType.URODA else CountryType.URODA
        self.current_state = State.HEALTHY

    def get_health_percentage(self, character: Character):
        """
        Returns a float representing the health of the given character.
        :param character: The character to get the health percentage for.
        """
        return float(character.current_health / character.max_health)

    def possible_moves(self, character: Character) -> dict[ActionType: Vector]:
        '''
        Fetch an associative array containing a map of any possible moves from
        a character's current position and the Vector it'd place them at.
        :param character: The character!!
        '''
        x = character.position.x
        match (character.position.y):
            case 0:
                return {
                    ActionType.NONE: Vector(x, 0),
                    ActionType.SWAP_DOWN: Vector(x, 1)
                }
            case 1:
                return {
                    ActionType.SWAP_UP: Vector(x, 0),
                    ActionType.NONE: Vector(x, 1),
                    ActionType.SWAP_DOWN: Vector(x, 2)
                }
            case 2:
                return {
                    ActionType.SWAP_UP: Vector(x, 1),
                    ActionType.NONE: Vector(x, 2)
                }

    def get_attack_dmg(self, move: Move | Effect) -> int:
        if (isinstance(move, Attack) or isinstance(move, AttackEffect)) and move.target_type not in [TargetType.SELF,
                                                                                                     TargetType.ADJACENT_ALLIES,
                                                                                                     TargetType.ENTIRE_TEAM]:
            return move.damage_points
        return 0

    def get_max_attack(self, character: Character) -> int:
        max_attack = self.get_attack_dmg(character.get_nm())

        if max_attack != 0:
            max_attack += character.attack.base_value

        max_attack += self.get_attack_dmg(character.get_nm().effect)

        return max_attack

    def character_vulnerability_index(self, character: Character, world: GameBoard, vector: Vector) -> float:
        ''''
        :param character - The character to assess vulnerability for.
        :param world     - The GameBoard object
        :param vector    - The Vector to query for vulnerability
        :returns         - Returns a value between 0 and 1. 0 is no risk, 1 is full risk.
        '''
        # Get relevant coords/enemy
        enemyCoords: Vector = Vector(self.enemy_country.value - 1, vector.y)
        enemy: Character | None = world.get_character_from(enemyCoords)

        # Signal high vulnerability if there's no enemy here
        if enemy is None:
            return 1

        char_percent = character.current_health / character.max_health
        enemy_is_faster = enemy.speed > character.speed

        # Determine max attack
        enemy_attack = self.get_max_attack(enemy)
        char_attack = self.get_max_attack(character)

        # Determine HP left after attacks
        enemy_remaining_hp = enemy.current_health - char_attack * (character.defense.value / 100)
        char_remaining_hp = character.current_health - enemy_attack * (character.defense.value / 100)

        # Exit now if we can just kill the guy
        if enemy_remaining_hp <= 0 and not enemy_is_faster:
            return 0

        # Exit now if the guy can just kill *us*
        if char_remaining_hp <= 0 and enemy_is_faster:
            return 1

        # Hardcoded edge cases
        flightyness = 0.0

        # If a generic healer exists on the field, we want to take them on first.
        # This is because if the opponent uses a Healer+Berry+X loadout, targeting
        # Berry first will put us in deadlock at best or a loss at worst.
        if character.class_type == ClassType.ATTACKER and enemy.object_type in [ObjectType.TURPIS_GENERIC_HEALER,
                                                                                ObjectType.URODA_GENERIC_HEALER]:
            return 0

        # If Berry's on the field, give them a 21% vulnerability index. This is so we
        # don't target them if there's a higher priority item on field, such as the aforementioned
        # case.
        if character.class_type == ClassType.ATTACKER and enemy.object_type == ObjectType.BERRY:
            return 0.21

        # We don't really like Anahita, so dissuade the metrics from preferring them.
        if character.class_type == ClassType.ATTACKER and enemy.object_type == ObjectType.ANAHITA:
            flightyness = 0.3

        # Ranges from -1 (their favor) to 1 (our favor)
        healthFactor = (char_remaining_hp / character.max_health) - (enemy_remaining_hp / enemy.max_health)

        # Ranges from 0 (their favor) to 1 (our favor)
        try:
            attackFactor = char_attack / (char_attack + enemy_attack)
        except ZeroDivisionError:
            attackFactor = 0

        return 1 - (attackFactor * ((healthFactor + 1) / 2) * (1 - flightyness))

    # This is where your AI will decide what to do
    def take_turn(self, turn: int, actions: list[ActionType], world: GameBoard, team_manager: TeamManager):
        """
        This is where your AI will decide what to do.
        :param turn:         The current turn of the game.
        :param actions:      This is the actions object that you will add effort allocations or decrees to.
        :param world:        Generic world information
        :param team_manager: A class that wraps the list of Characters to control
        """
        if turn == 1:
            self.first_turn_init(team_manager)

        # get your active character for the turn; may be None
        character: Character = self.get_my_active_char(team_manager, world)

        if character is None:
            return []

        # Pull HP and SP
        sp_cur = character.special_points
        hp_cur = character.current_health
        hp_max = character.max_health
        hp_percent = self.get_health_percentage(character)

        print("\nLOG (O): %d/%d - %s" % (hp_cur, hp_max, character.name))

        is_leader = character.rank_type == RankType.LEADER

        if is_leader:
            # Check if we need to request healing from Healers
            self.FultraNeedsHealing = hp_percent < 0.8

            # Pull viable positions
            viable_positions = self.possible_moves(character)
            action_weights = {action: self.character_vulnerability_index(character, world, vector) for (action, vector)
                              in viable_positions.items()}

            # EDGE CASE: Are both options not viable and and we're boxed up top or down below?
            if len(action_weights) == 2 and sum(list(action_weights.values())) == 2:
                if character.position.y == 0:
                    return [ActionType.SWAP_DOWN]
                else:
                    return [ActionType.SWAP_UP]

            # Determine which ActionType is most viable
            min_action = ActionType.NONE
            for each in [x for x in list(action_weights.keys()) if x != ActionType.NONE]:
                if action_weights[min_action] > action_weights[each]:
                    min_action = each

            if action_weights[ActionType.NONE] <= 0.2 or min_action == ActionType.NONE:
                if sp_cur == 5:
                    # if the active character from my team is healthy, use its Normal Move
                    return [ActionType.USE_S2]
                elif hp_percent < 0.4 and sp_cur > 2:
                    return [ActionType.USE_S1]
                else:
                    return [ActionType.USE_NM]

            else:
                return [min_action]

        else:

            if (self.FultraNeedsHealing) and (sp_cur > 2):
                print("\nLOG (O): Fultra needs healing!")
                self.FultraNeedsHealing = False
                return [ActionType.USE_S2]
            elif hp_percent > 0.70:
                # if the active character from my team is healthy, use its Normal Move
                return [ActionType.USE_NM]
            else:
                # if unhealthy, heal thyself
                print("\nLOG (O): Healer needs to heal themself!")
                return [ActionType.USE_S1]

    def get_my_active_char(self, team_manager: TeamManager, world: GameBoard) -> Character | None:
        """
        Returns your active character based on which characters have already acted. If None is returned, that means
        none of your characters can act again until the turn order refreshes. This also means your team has fewer
        characters than the opponent.
        """

        active_character = team_manager.get_active_character(world.ordered_teams, world.active_pair_index)

        return active_character
