import unittest

from game.byte_2025.character import GenericAttacker, GenericTank
from game.byte_2025.moves import *
from game.byte_2025.moves.moves import *
from game.common.enums import CharacterType
from game.common.map.game_board import GameBoard
from game.common.team_manager import TeamManager
from game.test_suite.utils import spell_check
from game.utils.vector import Vector


class TestMoveController(unittest.TestCase):
    def setUp(self):
        self.moves = {
            'NA': Attack('Baja Blast', TargetType.SINGLE_OPP, 0, None, 5),
            'S1': Buff('Baja Slurp', TargetType.SELF, 0, HealEffect(heal_points=10), 1.5),
            'S2': Debuff('Baja Dump', TargetType.ALL_OPPS, 0, None, 0.5),
            'S3': Heal('Baja Blessing', TargetType.ALL_ALLIES, 0, None, 10),
        }

        self.gen_attacker: GenericAttacker(health=10, defense=5, speed=15, country_type=CountryType.URODA, moveset=self.moves)
        self.gen_tank: GenericTank(health=15, defense=10, speed=5, country_type=CountryType.TURPIS)
        self.gen_tank1: GenericTank(health=20, defense=10, speed=5, country_type=CountryType.TURPIS)
        self.gen_tank2: GenericTank(health=25, defense=10, speed=5, country_type=CountryType.TURPIS)

        self.uroda_team_manager: TeamManager([], CountryType.URODA)

        self.gameboard: GameBoard = GameBoard()
