import os
import pygame
from game.config import *
from typing import Callable, Any

from game.utils.vector import Vector
from visualizer.config import Config
from visualizer.bytesprites.charactersBS import CharactersBS
from visualizer.templates.scoreboard_template import ScoreboardTemplate
from visualizer.utils.text import Text
from visualizer.bytesprites.bytesprite import ByteSprite
from visualizer.templates.menu_template import Basic, MenuTemplate
from visualizer.templates.playback_template import PlaybackTemplate, PlaybackButtons

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"


class Adapter:
    """
    The Adapter class can be considered the "Master Controller" of the Visualizer; it works in tandem with main.py.
    Main.py will call many of the methods that are provided in here to keep the Visualizer moving smoothly.
    """

    def __init__(self, screen):
        self.screen: pygame.Surface = screen
        self.config: Config = Config()
        self.bytesprites: list[ByteSprite] = []
        self.populate_bytesprite: pygame.sprite.Group = pygame.sprite.Group()
        self.menu: MenuTemplate = Basic(screen, self.config.FONT, self.config.FONT_COLOR_ALT,
                                        self.config.BUTTON_COLORS, 'Commander Clash')
        self.scoreboard = ScoreboardTemplate(screen, Vector(), Vector(y=100, x=1366), self.config.FONT,
                                             self.config.FONT_COLOR)
        self.playback: PlaybackTemplate = PlaybackTemplate(screen, self.config.FONT, self.config.BUTTON_COLORS)
        self.turn_number: int = 0
        self.turn_max: int = MAX_TICKS

    # Define any methods button may run

    def start_menu_event(self, event: pygame.event) -> Any:
        """
        This method is used to manage any events that will occur on the starting screen. For example, a start button
        is implemented currently. Pressing it or pressing enter will start the visualizer to show the game's results.
        This method will manage any specified events and return them (hence why the return type is Any). Refer to
        menu_templates.py's start_events method for more info.
        :param event: The pygame event triggered each frame. See
        `pygame <https://www.pygame.org/docs/ref/event.html for more information>`_
        for more information.
        :return: Any specified event desired in the start_events method
        """
        return self.menu.start_events(event)

    def start_menu_render(self) -> None:
        """
        Renders and shows everything in the start menu.
        :return: None
        """
        self.menu.start_render()

    def on_event(self, event) -> PlaybackButtons:
        """
        By giving this method an event, this method can execute whatever is specified. An example is provided below
        and commented out. Use as necessary.
        :param event: The pygame event triggered each frame. See
        `pygame <https://www.pygame.org/docs/ref/event.html for more information>`_
        for more information.
        :return: None
        """

        # The line below is an example of what this method could be used for.
        # self.button.mouse_clicked(event)
        return self.playback.playback_events(event)

    def prerender(self) -> None:
        """
        This will handle anything that needs to be completed before animations start every turn.
        :return: None
        """
        ...

    def continue_animation(self) -> None:
        """
        This method is used after the main.py continue_animation() method.
        :return: None
        """
        ...

    # re-renders the animation
    def recalc_animation(self, turn_log: dict) -> None:
        """
        This method is called every time the turn changes
        :param turn_log: A dictionary containing the entire turn state
        :return: None
        """
        self.scoreboard.recalc_animation(turn_log)
        self.turn_number = turn_log['tick']

    def populate_bytesprite_factories(self) -> dict[int: Callable[[pygame.Surface], ByteSprite]]:
        """
        Instantiate all bytesprites for each objectType and add them here using the value of ObjectType as the key
        and the factory function as the value
        :return: dict[int, Callable[[pygame.Surface], ByteSprite]]
        """
        return {
            12: CharactersBS.create_bytesprite,
            13: CharactersBS.create_bytesprite,
            14: CharactersBS.create_bytesprite,
            15: CharactersBS.create_bytesprite,
        }

    def render(self) -> None:
        """
        This method contains all logic for rendering additional text, buttons, and other visuals
        during the playback phase.
        :return: None
        """
        # self.button.render()
        # any logic for rendering text, buttons, and other visuals
        text = Text(self.screen, f'{self.turn_number:3d} / {self.turn_max:3d}', 48, color=self.config.FONT_COLOR,
                    font_name=self.config.FONT)
        text.rect.center = Vector.add_vectors(Vector(*self.screen.get_rect().midtop), Vector(0, 50)).as_tuple()
        text.render()

        self.scoreboard.render()
        self.playback.playback_render()

    # is used in post render - post render is used to clear the playback buttons
    def clean_up(self) -> None:
        """
        This method is called after rendering each frame.
        :return: None
        """
        ...

    def results_load(self, results: dict) -> None:
        """
        This method is called to load the end screen for the visualizer.
        :param results: A dictionary containing the results of the run
        :return: None
        """
        self.menu.load_results_screen(results)

    def results_event(self, event: pygame.event) -> Any:
        """
        This method is called to handle events of the visualizer in the end screen
        :param event: The pygame event triggered each frame. See
        `pygame <https://www.pygame.org/docs/ref/event.html>`_
        for more information.
        :return: Any value that is defined in the results_events
        """
        return self.menu.results_events(event)

    def results_render(self) -> None:
        """
        This renders the results for the game / the end screen
        :return:
        """
        self.menu.results_render()
