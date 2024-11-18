import random

from game.commander_clash.generation.character_generation import *
from game.common.game_object import GameObject
from game.common.team_manager import TeamManager
from game.utils.vector import Vector
from game.config import *
from game.utils.helpers import write_json_file
from game.utils.pre_generate_game import pre_generate
from game.common.map.game_board import GameBoard


def generate(seed: int = random.randint(0, 1000000000)):
    """
    This method is what generates the game_map. This method is slow, so be mindful when using it. A seed can be set as
    the parameter; otherwise, a random one will be generated. Then, the method checks to make sure the location for
    storing logs exists. Lastly, the game map is written to the game file.
    :param seed:
    :return: None
    """

    print(f'Generating game map... seed: {seed}')

    # get the locations of the characters necessary from the pre_generation methodc
    locations: dict[Vector, list[GameObject]] = pre_generate()

    temp: GameBoard = GameBoard(seed, map_size=Vector(6, 6), walled=False, locations=locations)
    temp.generate_map()
    data: dict = {'game_board': temp.to_json()}
    # for x in range(1, MAX_TICKS + 1):
    #     data[x] = 'data'

    # Verify logs location exists
    if not os.path.exists(GAME_MAP_DIR):
        os.mkdir(GAME_MAP_DIR)

    # Write game map to file
    write_json_file(data, GAME_MAP_FILE)
