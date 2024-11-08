import pygame

from game.utils.vector import Vector
from visualizer.templates.info_template import InfoTemplate
from visualizer.utils.text import Text


class CharacterInfoTemplate(InfoTemplate):
    def __init__(self, screen: pygame.Surface, topleft: Vector, size: Vector, font: str, color: str,
                 country: int, character: int) -> None:
        super().__init__(screen, topleft, size, font, color)

        # self.backdrop: CharacterInfoBackdrop = CharacterInfoBackdrop(top_left=topleft)
        # self.backdrop.add(self.render_list)
        #
        # self.characterProfile: CharacterProfile = CharacterProfile(top_left=Vector.add_vectors(topleft, Vector(x=22, y=23)))
        # self.characterProfile.add(self.render_list)
        #
        # self.health_bar: HealthBar = HealthBar(top_left=Vector.add_vectors(topleft, Vector(x=96, y=23)))
        # self.health_bar.add(self.render_list)
        #
        self.health_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                             position=Vector.add_vectors(topleft, Vector(x=303, y=23)))

        # self.sp_bar = SPBar(top_left=Vector.add_vectors(topleft, Vector(x=96, y=62)))
        # self.sp_bar.add(self.render_list)
        #
        self.sp_bar_text: Text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                                      position=Vector.add_vectors(topleft, Vector(x=209, y=62)))

        # self.attack_stat = AttackStat(top_left=Vector.add_vectors(topleft, Vector(x=29, y=106)))
        # self.attack_stat.add(self.render_list)
        #
        self.attack_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                 position=Vector.add_vectors(topleft, Vector(x=78, y=106)))

        # self.defense_stat = DefenseStat(top_left=Vector.add_vectors(topleft, Vector(x=135, y=106)))
        # self.defense_stat.add(self.render_list)
        #
        self.defense_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                   position=Vector.add_vectors(topleft, Vector(x=184, y=106)))

        # self.speed_stat = SpeedStat(top_left=Vector.add_vectors(topleft, Vector(x=238, y=106)))
        # self.speed_stat.add(self.render_list)
        #
        self.speed_stat_text = Text(screen, text="0", font_size=32, font_name=self.font, color=self.color,
                                 position=Vector.add_vectors(topleft, Vector(x=287, y=106)))

    def recalc_animation(self, turn_log: dict) -> None:
        # Three sections for this recalc, grab info, choose images to render from info, then recalc text to render
        # self.health_bar.text = str(len([item for item in inventory if item.get('object_type', 1) == 15]))
        # self.sp_bar.text = str(len([item for item in inventory if item.get('object_type', 1) == 15]))
        # self.attack_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 13]))
        # self.defense_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 11]))
        # self.speed_stat.text = str(len([item for item in inventory if item.get('object_type', 1) == 12]))
        ...

    def render(self) -> None:
        super().render()
        self.health_bar_text.render()
        self.sp_bar_text.render()
        self.attack_stat_text.render()
        self.defense_stat_text.render()
        self.speed_stat_text.render()
