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

    # get the locations of the characters necessary from the pre_generation method
    info: tuple[dict[Vector, list[GameObject]], list[TeamManager]] = pre_generate()

    temp: GameBoard = GameBoard(seed, map_size=Vector(2, 3), walled=False, locations=info[0])
    temp.generate_map()
    data: dict = {'game_board': temp.to_json()}
    # for x in range(1, MAX_TICKS + 1):
    #     data[x] = 'data'

    # for every created team manager, write them to the json
    for team_manager in info[1]:
        if team_manager.country_type == CountryType.URODA:
            data['game_board']['uroda_team_manager'] = team_manager.to_json()
        else:
            data['game_board']['turpis_team_manager'] = team_manager.to_json()

    # Verify logs location exists
    if not os.path.exists(GAME_MAP_DIR):
        os.mkdir(GAME_MAP_DIR)

    # Write game map to file
    write_json_file(data, GAME_MAP_FILE)
