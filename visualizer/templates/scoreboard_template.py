import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

from game.utils.vector import Vector
from visualizer.templates.info_template import InfoTemplate
from visualizer.utils.text import Text
from game.config import MAX_TICKS


class ScoreboardTemplate(InfoTemplate):
    def __init__(self, screen: pygame.Surface, topleft: Vector, size: Vector, font: str, color: str) -> None:
        super().__init__(screen, topleft, size, font, color)

        self.uroda_score: Text = Text(screen, text="0", font_size=42, font_name=self.font, color=self.color,
                                             position=Vector.add_vectors(topleft, Vector(x=340, y=65)))

        self.turpis_score: Text = Text(screen, text="0", font_size=42, font_name=self.font, color=self.color,
                                             position=Vector.add_vectors(topleft, Vector(x=1200, y=65)))

        self.turn: Text = Text(screen, text="0", font_size=48, font_name=self.font, color=self.color,
                                             position=Vector.add_vectors(topleft, Vector(x=600, y=100)))

    def recalc_animation(self, turn_log: dict) -> None:
        clients = sorted(turn_log['clients'], key=lambda client: client.get('team_manager', {'country_type': 0})['country_type'])
        scores: list[int] = [client['team_manager']['score'] if client['team_manager'] else 0 for client in clients]
        turn = turn_log['tick']

        self.uroda_score.text = str(scores[0])
        self.turpis_score.text = str(scores[1])
        self.turn.text = f'{turn}/{MAX_TICKS}'

    def render(self) -> None:
        super().render()
        self.uroda_score.render()
        self.turpis_score.render()
        self.turn.render()
