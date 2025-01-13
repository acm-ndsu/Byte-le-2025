import os

from visualizer.sprites.active import Active

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from math import ceil
from game.commander_clash.character.character import Character
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
                 country: int, index: int) -> None:
        super().__init__(screen, topleft, size, font, color)

        # Save who to update
        self.country: int = country
        self.index: int = index

        self.backdrop: CharacterInfoBackdrop = CharacterInfoBackdrop(top_left=topleft)
        self.backdrop.add(self.render_list)

        self.headshot: Headshot = Headshot(top_left=Vector.add_vectors(topleft, Vector(x=15, y=23)))
        self.headshot.add(self.render_list)

        self.active: Active = Active(top_left=Vector.add_vectors(topleft, Vector(x=55, y=10)))
        self.active.add(self.render_list)

        self.hp_bar: HPBar = HPBar(top_left=Vector.add_vectors(topleft, Vector(x=89, y=23)))
        self.hp_bar.add(self.render_list)

        self.hp_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=296, y=19)))

        self.sp_bar = SPBar(top_left=Vector.add_vectors(topleft, Vector(x=89, y=62)))
        self.sp_bar.add(self.render_list)

        self.sp_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=202, y=58)))

        self.attack_stat = AttackStat(top_left=Vector.add_vectors(topleft, Vector(x=15, y=106)))
        self.attack_stat.add(self.render_list)

        self.attack_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                     position=Vector.add_vectors(topleft, Vector(x=64, y=109)))

        self.defense_stat = DefenseStat(top_left=Vector.add_vectors(topleft, Vector(x=121, y=106)))
        self.defense_stat.add(self.render_list)

        self.defense_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                      position=Vector.add_vectors(topleft, Vector(x=170, y=109)))

        self.speed_stat = SpeedStat(top_left=Vector.add_vectors(topleft, Vector(x=224, y=106)))
        self.speed_stat.add(self.render_list)

        self.speed_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                    position=Vector.add_vectors(topleft, Vector(x=273, y=109)))

    def recalc_animation(self, turn_log: dict) -> None:
        # Get character we are recalculating
        team: list[Character] = turn_log['clients'][self.country - 1]['team_manager']['team']
        dead_team: list[Character] = turn_log['clients'][self.country - 1]['team_manager']['dead_team']

        character: Character = Character().from_json(data=[char for char in team + dead_team if char['index'] == self.index][0])

        # Get which headshot to grab
        self.headshot.character = f'{character.name.split(" ", 2)[0].lower()}_{character.name.split(" ", 2)[1].lower()}'

        # Get if the character is active
        active_pair_index: int = turn_log['game_board']['active_pair_index']
        if turn_log['game_board']['ordered_teams'][active_pair_index][character.country_type.value - 1] is None:
            self.active.transparent = True
        else:
            self.active.transparent = False if character.name == turn_log['game_board']['ordered_teams'][active_pair_index][character.country_type.value - 1]['name'] else True

        # Get hp and sp of character
        self.hp_bar.hp = int(ceil((float(character.current_health) / float(character.max_health)) * 10))
        self.hp_bar_text.text = f'{character.current_health} / {character.max_health}'
        self.sp_bar.sp = character.special_points
        self.sp_bar_text.text = f'{character.special_points} / 5'

        # Get attack, defense, and speed based on generated character
        self.attack_stat.attack_stat = 0 if character.attack.value == character.attack.base_value else 1 \
            if character.attack.value > character.attack.base_value else 2
        self.attack_stat_text.text = str(character.attack.value)

        self.defense_stat.defense_stat = 0 if character.defense.value == character.defense.base_value else 1 \
            if character.defense.value > character.defense.base_value else 2
        self.defense_stat_text.text = str(character.defense.value)

        self.speed_stat.speed_stat = 0 if character.speed.value == character.speed.base_value else 1 \
            if character.speed.value > character.speed.base_value else 2
        self.speed_stat_text.text = str(character.speed.value)

    def render(self) -> None:
        super().render()
        self.hp_bar_text.render()
        self.sp_bar_text.render()
        self.attack_stat_text.render()
        self.defense_stat_text.render()
        self.speed_stat_text.render()
