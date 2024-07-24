from copy import deepcopy
import random

from game.byte_2025.character import Character
from game.common.action import Action
from game.common.team_manager import TeamManager
from game.common.enums import *
from game.common.player import Player
import game.config as config   # this is for turns
from game.utils.thread import CommunicationThread
from game.controllers.movement_controller import MovementController
from game.controllers.controller import Controller
from game.common.map.game_board import GameBoard
from game.config import MAX_NUMBER_OF_ACTIONS_PER_TURN
from game.utils.vector import Vector 


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
        self.movement_controller: MovementController = MovementController()

    # Receives all clients for the purpose of giving them the objects they will control
    def give_clients_objects(self, clients: list[Player], world: dict):
        # starting_positions would set done in generate game

        gb: GameBoard = world['game_board']

        # get the two teams from the gameboard
        uroda_team: dict[Vector, Character] = gb.get_characters(CountryType.URODA)
        turpis_team: dict[Vector, Character] = gb.get_characters(CountryType.TURPIS)

        # create a new TeamManager for every Player object
        # the first Player is assigned the Uroda team, and then second is assigned Turpis
        for iteration, client in enumerate(clients):
            client.team_manager = TeamManager()
            client.team_manager.team = uroda_team if iteration == 0 else turpis_team

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
            random.seed(world['game_board'].seed)
            # self.event_times = random.randrange(162, 172), random.randrange(329, 339)

    # Receive a specific client and send them what they get per turn. Also obfuscates necessary objects.
    def client_turn_arguments(self, client: Player, turn):
        # turn_action: Action = Action()
        # client.action: Action = turn_action
        # ^if you want to use action as an object instead of an enum

        turn_actions: list[ActionType] = []
        client.actions = turn_actions

        # Create deep copies of all objects sent to the player
        current_world = deepcopy(self.current_world_data["game_board"])    # what is current world and copy avatar
        copy_avatar = deepcopy(client.team_manager)
        # Obfuscate data in objects that that player should not be able to see
        # Currently world data isn't obfuscated at all
        args = (self.turn, turn_actions, current_world, copy_avatar)
        return args

    # Perform the main logic that happens per turn
    def turn_logic(self, clients: list[Player], turn):
        for client in clients:
            for i in range(MAX_NUMBER_OF_ACTIONS_PER_TURN):
                try:
                    self.movement_controller.handle_actions(client.actions[i], client, self.current_world_data["game_board"])
                except IndexError:
                    pass

        # checks event logic at the end of round
        # self.handle_events(clients)

    # comment out for now, nothing is in place for event types yet
    # def handle_events(self, clients):
        # If it is time to run an event, master controller picks an event to run
        # if self.turn == self.event_times[0] or self.turn == self.event_times[1]:
        #    self.current_world_data["game_map"].generate_event(EventType.example, EventType.example)
        # event type.example is just a placeholder for now

    # Return serialized version of game
    def create_turn_log(self, clients: list[Player], turn: int):
        data = dict()
        data['tick'] = turn
        data['clients'] = [client.to_json() for client in clients]
        # Add things that should be thrown into the turn logs here
        data['game_board'] = self.current_world_data["game_board"].to_json()

        return data

    # Gather necessary data together in results file
    def return_final_results(self, clients: list[Player], turn):
        data = dict()

        data['players'] = list()
        # Determine results
        for client in clients:
            data['players'].append(client.to_json())

        return data
