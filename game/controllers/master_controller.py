import random

from game.common.enums import *
from game.common.map.game_board import GameBoard
from game.common.player import Player
from game.common.team_manager import TeamManager
from game.config import MAX_NUMBER_OF_ACTIONS_PER_TURN, WIN_SCORE, DIFFERENTIAL_BONUS
from game.controllers.controller import Controller
from game.controllers.swap_controller import SwapController
from game.controllers.select_move_controller import SelectMoveController
from game.controllers.new_move_controller import NewMoveController


class MasterController(Controller):
    """
    `Master Controller Notes:`

        Give Client Objects:
            Takes a list of Player objects and places each one in the game world.

        Game Loop Logic:
            Increments the turn count as the game plays (look at the engine to see how it's controlled more).

        Interpret Current Turn Data:
            This accesses the gameboard in the first turn of the game and generates the game's seed.

        Client Turn Arguments:
            There are lines of code commented out that create Action Objects instead of using the enum. If your project
            needs Actions Objects instead of the enums, comment out the enums and use Objects as necessary.

        Turn Logic:
            This method executes every movement and interact behavior from every client in the game. This is done by
            using every other type of Controller object that was created in the project that needs to be managed
            here (InteractController, MovementController, other game-specific controllers, etc.).

        Create Turn Log:
            This method creates a dictionary that stores the turn, all client objects, and the gameboard's JSON file to
            be used as the turn log.

        Return Final Results:
            This method creates a dictionary that stores a list of the clients' JSON files. This represents the final
            results of the game.
    """

    def __init__(self):
        super().__init__()
        self.game_over: bool = False
        # self.event_timer = GameStats.event_timer   # anything related to events are commented it out until made
        # self.event_times: tuple[int, int] | None = None
        self.turn: int = 1
        self.current_world_data: dict = None
        self.swap_controller: SwapController = SwapController()
        self.select_move_controller: SelectMoveController = SelectMoveController()
        self.new_move_controller: NewMoveController = NewMoveController()

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients: list[Player], world: dict, team_managers: list[TeamManager]):
        # the clients and their team managers will match up, so assign the client their correct team manager
        for iteration, client in enumerate(clients):
            client.team_manager = team_managers[iteration]

    # Generator function. Given a key:value pair where the key is the identifier for the current world and the value is
    # the state of the world, returns the key that will give the appropriate world information
    def game_loop_logic(self, start=1):
        self.turn = start

        # Basic loop from 1 to max turns
        while True:
            # Wait until the next call to give the number
            yield str(self.turn)
            # Increment the turn counter by 1
            self.turn += 1

    # Receives world data from the generated game log and is responsible for interpreting it
    def interpret_current_turn_data(self, clients: list[Player], world: dict, turn):
        self.current_world_data = world

        if turn == 1:
            random.seed(world['game_board']['seed'])
            # self.event_times = random.randrange(162, 172), random.randrange(329, 339)

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client: Player, turn):
        # turn_action: Action = Action()
        # client.action: Action = turn_action
        # ^if you want to use action as an object instead of an enum

        turn_actions: list[ActionType] = []
        client.actions = turn_actions

        # Create deep copies of all objects sent to the player
        current_world = GameBoard().from_json(self.current_world_data[
                                                  'game_board'])  # deepcopy(self.current_world_data["game_board"])  # what is current world and copy avatar
        copy_team_manager = TeamManager().from_json(client.team_manager.to_json())  # deepcopy(client.team_manager)
        # Obfuscate data in objects that that player should not be able to see
        # Currently world data isn't obfuscated at all

        args = (self.turn, turn_actions, current_world, copy_team_manager)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients: list[Player], turn):
        gameboard: GameBoard = GameBoard().from_json(self.current_world_data['game_board'])

        # start by removing any dead characters off the game map
        for client in clients:
            # remove any dead characters off the game map
            gameboard.remove_dead_from_game_map(client.team_manager.dead_team)

        # reset the turn info string for new information
        gameboard.turn_info = ''

        for client in clients:
            # set each character's state to 'idle' in the client's team manager
            for character in client.team_manager.team:
                character.state = 'idle'

            # if the team is defeated, move on
            if client.team_manager.everyone_is_defeated():
                continue

            # attempt to perform the action for the given ActionType
            for i in range(MAX_NUMBER_OF_ACTIONS_PER_TURN):
                try:
                    self.swap_controller.handle_actions(client.actions[i], client, gameboard)
                    self.select_move_controller.handle_actions(client.actions[i], client, gameboard)
                except IndexError:
                    pass

            # # update the game board's team manager references
            # gameboard.update_team_managers()

        self.new_move_controller.handle_logic(clients, gameboard, turn)

        # update the game board's team manager references
        gameboard.update_team_managers()

        # to ensure the clients receive the updates for their characters, loop over the two and reassign their
        # team managers to be the game board references
        # call the variable client_ to not get confused with the outer for loop
        # this for loop needs to happen every turn
        for client in clients:
            # get the client's score before it is overwritten
            client_score: int = client.team_manager.score

            if client.team_manager.country_type == CountryType.URODA:
                client.team_manager = gameboard.uroda_team_manager
            else:
                client.team_manager = gameboard.turpis_team_manager

            client.team_manager.score = client_score

            # if everyone took their action in the given team manager, set their took_action bool to False
            if client.team_manager.everyone_took_action():
                for character in client.team_manager.team:
                    character.took_action = False

                # ensure the team is ordered by speed after everyone took their turn
                client.team_manager.speed_sort()

        # repopulate the ordered_teams property if the list is empty in the gameboard
        if len(gameboard.ordered_teams) == 0:
            gameboard.order_teams()

        # update the current world json by setting it to the game board's updated state

        self.current_world_data['game_board'] = gameboard.to_json()

    # Return serialized version of game
    def create_turn_log(self, clients: list[Player], turn: int):
        data = dict()
        data['tick'] = turn
        data['clients'] = [client.to_json() for client in clients]

        # Add things that should be thrown into the turn logs here
        data['game_board'] = self.current_world_data['game_board']

        return data

    # Gather necessary data together in results file
    def return_final_results(self, clients: list[Player], turn):
        data = dict()

        client1: Player = clients[0]
        client2: Player = clients[1]

        # add the differential bonus to both teams (150 * # of alive characters)
        client1.team_manager.score += DIFFERENTIAL_BONUS * len(client1.team_manager.team)
        print(f'Giving client {client1.team_name} different bonus of {DIFFERENTIAL_BONUS} * '
              f'{len(client1.team_manager.team)} = {DIFFERENTIAL_BONUS * len(client1.team_manager.team)}')

        client2.team_manager.score += DIFFERENTIAL_BONUS * len(client2.team_manager.team)
        print(f'Giving client {client2.team_name} different bonus of {DIFFERENTIAL_BONUS} * '
              f'{len(client2.team_manager.team)} = {DIFFERENTIAL_BONUS * len(client2.team_manager.team)}')

        # client1 is the winner if client2's team is all dead
        winner: Player | None = client1 if client2.team_manager.everyone_is_defeated() else \
            client2 if client1.team_manager.everyone_is_defeated() else None

        # if there is a clear winner (one team was defeated), add the winning score to the winner
        if winner is not None:
            winner.team_manager.score += WIN_SCORE
            print(f'Giving client {winner.team_name} win bonus of {WIN_SCORE}')

        data['players'] = list()

        # Determine results
        for client in clients:
            data['players'].append(client.to_json())

        return data
