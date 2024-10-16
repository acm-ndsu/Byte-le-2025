import pygame

from game.utils.vector import Vector
from visualizer.templates.info_template import InfoTemplate
from visualizer.templates.character_info_template import CharacterInfoTemplate
from visualizer.utils.text import Text


class TeamInfoTemplate(InfoTemplate):
    def __init__(self, screen: pygame.Surface, topleft: Vector, size: Vector, font: str, color: str,
                 country: int) -> None:
        super().__init__(screen, topleft, size, font, color)
        """
        Displays a Country name and Team name with the font size of 32
        and instantiates the character info templates
        """

        # self.backdrop: TeamInfoBackdrop = TeamInfoBackdrop(top_left=topleft)
        # self.backdrop.add(self.render_list)
        #
        self.country = country
        self.country_text: Text = Text(screen, text=f'{"Uroda" if country == 1 else "Turpis"}',
                                       font_size=32, font_name=self.font, color=self.color,
                                       position=Vector.add_vectors(self.topleft, Vector(y=25, x=25)))

        # Character Info Templates instantiated here
        self.character1 = CharacterInfoTemplate(screen, Vector.add_vectors(self.topleft, Vector(y=70, x=10)), Vector(y=240, x=530),
                              self.font, self.color, self.country, 0)
        self.character2 = CharacterInfoTemplate(screen, Vector.add_vectors(self.topleft, Vector(y=330, x=10)), Vector(y=240, x=530),
                              self.font, self.color, self.country, 1)
        self.character3 = CharacterInfoTemplate(screen, Vector.add_vectors(self.topleft, Vector(y=590, x=10)), Vector(y=240, x=530),
                              self.font, self.color, self.country, 2)

    def recalc_animation(self, turn_log: dict) -> None:
        team_name: str = [client['team_name']
                          for client in turn_log['clients']
                          if client['team_manager']['country'] == self.country][0]
        self.country_text.text = f'{"Uroda" if self.country == 1 else "Turpis"}: {team_name}'[:30]
        self.character1.recalc_animation(turn_log)
        self.character2.recalc_animation(turn_log)
        self.character3.recalc_animation(turn_log)

    def render(self) -> None:
        super().render()
        self.country_text.render()
        self.character1.render()
        self.character2.render()
        self.character3.render()