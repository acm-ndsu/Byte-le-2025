import pygame

from game.utils.vector import Vector
from visualizer.templates.info_template import InfoTemplate
from visualizer.utils.text import Text


class CharacterInfoTemplate(InfoTemplate):
    def __init__(self, screen: pygame.Surface, topleft: Vector, size: Vector, font: str, color: str,
                 country: int) -> None:
        super().__init__(screen, topleft, size, font, color)

        # self.backdrop: CharacterInfoBackdrop = CharacterInfoBackdrop(top_left=topleft)
        # self.backdrop.add(self.render_list)
        #
        # self.country = country
        # self.country_text: Text = Text(screen, text=f'{"Uroda" if country == 1 else "Turpis"}',
        #                                font_size=32, font_name=self.font, color=self.color,
        #                                position=Vector.add_vectors(topleft, Vector(y=25, x=25)))
        #
        # self.health_bar = HealthBar(top_left=Vector.add_vectors(topleft, Vector(y=100, x=50)))
        # self.health_bar.add(self.render_list)
        #
        # self.health_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
        #                                     position=Vector.add_vectors(topleft, Vector(y=95, x=100)))
        #
        # self.attack_stat = AttackStat(top_left=Vector.add_vectors(topleft, Vector(y=150, x=50)))
        # self.attack_stat.add(self.render_list)
        #
        # self.attack_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
        #                         position=Vector.add_vectors(topleft, Vector(y=145, x=100)))
        # 
        # self.defense_stat = DefenseStat(top_left=Vector.add_vectors(topleft, Vector(y=200, x=50)))
        # self.defense_stat.add(self.render_list)
        #
        # self.defense_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
        #                           position=Vector.add_vectors(topleft, Vector(y=195, x=100)))
        #
        # self.speed_stat = SpeedStat(top_left=Vector.add_vectors(topleft, Vector(y=250, x=50)))
        # self.speed_stat.add(self.render_list)
        #
        # self.speed_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
        #                         position=Vector.add_vectors(topleft, Vector(y=245, x=100)))

    def recalc_animation(self, turn_log: dict) -> None:
        # self.health_bar.text = str(len([item for item in inventory if item.get('object_type', 1) == 15]))
        # self.attack_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 13]))
        # self.defense_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 11]))
        # self.speed_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 12]))

    def render(self) -> None:
        super().render()
        self.health_bar_text.render()
        self.attack_stat_text.render()
        self.defense_stat_text.render()
        self.speed_stat_text.render()
