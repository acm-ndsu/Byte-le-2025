import pygame

from math import ceil
from game.commander_clash.character.character import Character
from game.common.enums import RankType, CountryType
from game.utils.vector import Vector
from visualizer.sprites.attack_stat import AttackStat
from visualizer.sprites.character_info_backdrop import CharacterInfoBackdrop
from visualizer.sprites.defense_stat import DefenseStat
from visualizer.sprites.headshot import Headshot
from visualizer.sprites.hp_bar import HPBar
from visualizer.sprites.sp_bar import SPBar
from visualizer.sprites.speed_stat import SpeedStat
from visualizer.templates.info_template import InfoTemplate
from visualizer.utils.text import Text


class CharacterInfoTemplate(InfoTemplate):
    def __init__(self, screen: pygame.Surface, topleft: Vector, size: Vector, font: str, color: str,
                 country: int, rank_type: RankType, second_gen: bool = False) -> None:
        super().__init__(screen, topleft, size, font, color)

        # Save who to update
        self.country: int = country
        self.rank_type: RankType = rank_type
        self.second_gen: bool = second_gen

        self.backdrop: CharacterInfoBackdrop = CharacterInfoBackdrop(top_left=topleft)
        self.backdrop.add(self.render_list)

        self.headshot: Headshot = Headshot(top_left=Vector.add_vectors(topleft, Vector(x=22, y=23)))
        self.headshot.add(self.render_list)

        self.hp_bar: HPBar = HPBar(top_left=Vector.add_vectors(topleft, Vector(x=96, y=23)))
        self.hp_bar.add(self.render_list)

        self.hp_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=303, y=23)))

        self.sp_bar = SPBar(top_left=Vector.add_vectors(topleft, Vector(x=96, y=62)))
        self.sp_bar.add(self.render_list)

        self.sp_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=209, y=62)))

        self.attack_stat = AttackStat(top_left=Vector.add_vectors(topleft, Vector(x=29, y=106)))
        self.attack_stat.add(self.render_list)

        self.attack_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                     position=Vector.add_vectors(topleft, Vector(x=78, y=106)))

        self.defense_stat = DefenseStat(top_left=Vector.add_vectors(topleft, Vector(x=135, y=106)))
        self.defense_stat.add(self.render_list)

        self.defense_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=184, y=106)))

        self.speed_stat = SpeedStat(top_left=Vector.add_vectors(topleft, Vector(x=238, y=106)))
        self.speed_stat.add(self.render_list)

        self.speed_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                    position=Vector.add_vectors(topleft, Vector(x=287, y=106)))

    def recalc_animation(self, turn_log: dict) -> None:

        # Get character we are recalculating
        team: list[Character] = turn_log['clients']['team_manager']['team'] \
            if turn_log['clients']['team_manager']['country'] == self.country else None
        dead_team: list[Character] = turn_log['clients']['team_manager']['dead_team'] \
            if turn_log['clients']['team_manager']['country'] == self.country else None

        character: Character
        if self.rank_type == RankType.LEADER:
            character = [character for character in team + dead_team if character.rank_type == self.rank_type][0]
        else:
            if not self.second_gen:
                character = [character for character in team + dead_team if '1' in character.name][0]
            else:
                character = [character for character in team + dead_team if '2' in character.name][0]

        # Get which headshot to grab
        if self.rank_type == RankType.LEADER:
            self.headshot.character = character.name.lower()
        else:
            self.headshot.character = (f'{CountryType(self.country).name.lower()}_generic_'
                                       f'{character.character_type.name.lower()}')

        # Get hp and sp of character
        self.hp_bar.hp = int(ceil((float(character.current_health) / float(character.max_health)) * 10))
        self.hp_bar_text.text = f'{character.current_health} / {character.max_health}'
        self.sp_bar.sp = character.special_points
        self.sp_bar_text.text = f'{character.special_points} / 5'

        # Get attack, defense, and speed based on generated character
        self.attack_stat.attack_stat = 0 if character.attack.value == character.attack.base_value else 1 \
            if character.attack.value > character.attack.base_value else 2
        self.attack_stat_text.text = character.attack.value

        self.defense_stat.defense_stat = 0 if character.defense.value == character.defense.base_value else 1 \
            if character.defense.value > character.defense.base_value else 2
        self.defense_stat_text.text = character.defense.value

        self.speed_stat.speed_stat = 0 if character.speed.value == character.speed.base_value else 1 \
            if character.speed.value > character.speed.base_value else 2
        self.speed_stat_text.text = character.speed.value

    def render(self) -> None:
        super().render()
        self.hp_bar_text.render()
        self.sp_bar_text.render()
        self.attack_stat_text.render()
        self.defense_stat_text.render()
        self.speed_stat_text.render()
