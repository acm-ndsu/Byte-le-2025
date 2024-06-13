import unittest

from game.byte_le_2025.character.character import Character
from game.byte_le_2025.character.generic_attacker import GenericAttacker
from game.byte_le_2025.character.generic_healer import GenericHealer
from game.byte_le_2025.character.generic_tank import GenericTank
from game.byte_le_2025.character.leader import Leader
from game.common.enums import CharacterType
from game.utils.vector import Vector
from game.test_suite.utils import spell_check


class TestCharacter(unittest.TestCase):
    def setUp(self) -> None:
        self.character: Character = Character('name', CharacterType.TANK)
        self.gen_attacker: GenericAttacker = GenericAttacker('Billy', CharacterType.ATTACKER)
        self.gen_healer: GenericHealer = GenericHealer('Steve', CharacterType.HEALER)
        self.gen_tank: GenericTank = GenericTank('Bertha', CharacterType.TANK)
        self.leader: Leader = Leader('Phil', CharacterType.TANK)
        self.num: int = 100
        self.neg_num: int = -1
        self.none: None = None

    # Test that passing in valid inputs for all the constructor parameters is correct
    def test_initialization(self):
        self.gen_tank.health = self.num
        self.gen_tank.attack = self.num
        self.gen_tank.defense = self.num
        self.gen_tank.speed = self.num
        # test passive ability later
        self.gen_tank.guardian = self.gen_attacker
        # test possible moves later
        self.gen_tank.special_points = self.num
        self.gen_tank.position = Vector(0, 0)

        # ensure the values are stored properly
        self.assertEqual(self.gen_tank.health, self.num)
        self.assertEqual(self.gen_tank.attack, self.num)
        self.assertEqual(self.gen_tank.defense, self.num)
        self.assertEqual(self.gen_tank.speed, self.num)
        self.assertEqual(self.gen_tank.guardian, self.gen_attacker)
        self.assertEqual(self.gen_tank.special_points, self.num)
        self.assertEqual(self.gen_tank.position, Vector(0, 0))

    # Test that passing in bad inputs (a string instead of an int, a None value where it's not needed, etc)
    def test_initialization_fail(self):
        # check that a negative int fails for health
        with self.assertRaises(ValueError) as e:
            self.gen_tank.health = self.neg_num
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.health must be a positive '
                                                      f'int.', True))

        # check that a None value fails for health
        with self.assertRaises(ValueError) as e:
            self.gen_tank.health = self.none
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.health must be an int. It '
                                                      f'is a(n) {self.none.__class__.__name__} '
                                                      f'and has the value of {self.none}', True))

        # check that a negative int fails for attack
        with self.assertRaises(ValueError) as e:
            self.gen_tank.attack = self.neg_num
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.attack must be a positive '
                                                      f'int.', True))

        # check that a None value fails for attack
        with self.assertRaises(ValueError) as e:
            self.gen_tank.attack = self.none
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.attack must be an int. It '
                                                      f'is a(n) {self.none.__class__.__name__} '
                                                      f'and has the value of {self.none}', True))

        # check that a negative int fails for defense
        with self.assertRaises(ValueError) as e:
            self.gen_tank.defense = self.neg_num
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.defense must be a positive '
                                                      f'int.', True))

        # check that a None value fails for defense
        with self.assertRaises(ValueError) as e:
            self.gen_tank.defense = self.none
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.defense must be an int. It '
                                                      f'is a(n) {self.none.__class__.__name__} '
                                                      f'and has the value of {self.none}', True))

        # check that a negative int fails for speed
        with self.assertRaises(ValueError) as e:
            self.gen_tank.speed = self.neg_num
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.speed must be a positive '
                                                      f'int.', True))

        # check that a None value fails for speed
        with self.assertRaises(ValueError) as e:
            self.gen_tank.speed = self.none
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.speed must be an int. It '
                                                      f'is a(n) {self.none.__class__.__name__} '
                                                      f'and has the value of {self.none}', True))

        # check that a negative int fails for special_points
        with self.assertRaises(ValueError) as e:
            self.gen_tank.special_points = self.neg_num
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.special_points must be a positive '
                                                      f'int.', True))

        # check that a None value fails for special_points
        with self.assertRaises(ValueError) as e:
            self.gen_tank.special_points = self.none
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.special_points must be an int. It '
                                                      f'is a(n) {self.none.__class__.__name__} '
                                                      f'and has the value of {self.none}', True))

        #Come back to this
        value: int = 10
        with self.assertRaises(ValueError) as e:
            self.gen_tank.position = value
        self.assertTrue(self.utils.spell_check(str(e.exception), f'gen_tank.position must be a Vector or None. '
                                                                 f'It is a(n) {value.__class__.__name__} and has the value of {value}',
                                               False))

        with self.assertRaises(ValueError) as e:
            self.gen_tank.guardian = value
        self.assertTrue(self.utils.spell_check(str(e.exception), f'gen_tank.guardian must be a Character or None. '
                                                                 f'It is a(n) {value.__class__.__name__} and has the value of {value}',
                                               False))

    def test_to_json_character(self):
        data: dict = self.character.to_json()
        char: Character = Character().from_json(data)
        self.assertEqual(char.name, self.character.name)
        self.assertEqual(char.character_type, self.character.character_type)
        self.assertEqual(char.health, self.character.health)
        self.assertEqual(char.attack, self.character.attack)
        self.assertEqual(char.defense, self.character.defense)
        self.assertEqual(char.speed, self.character.speed)
        self.assertEqual(char.rank, self.character.rank)
        self.assertEqual(char.special_points, self.character.special_points)
        self.assertEqual(char.position, None)
        self.assertEqual(char.guardian, None)

    def test_to_json_genatk(self):
        data: dict = self.gen_attacker.to_json()
        char: GenericAttacker = GenericAttacker().from_json(data)
        self.assertEqual(char.name, self.gen_attacker.name)
        self.assertEqual(char.character_type, self.gen_attacker.character_type)
        self.assertEqual(char.health, self.gen_attacker.health)
        self.assertEqual(char.attack, self.gen_attacker.attack)
        self.assertEqual(char.defense, self.gen_attacker.defense)
        self.assertEqual(char.speed, self.gen_attacker.speed)
        self.assertEqual(char.rank, self.gen_attacker.rank)
        self.assertEqual(char.special_points, self.gen_attacker.special_points)
        self.assertEqual(char.position, None)
        self.assertEqual(char.guardian, None)

    def test_to_json_genheal(self):
        data: dict = self.gen_healer.to_json()
        char: GenericHealer = GenericHealer().from_json(data)
        self.assertEqual(char.name, self.gen_healer.name)
        self.assertEqual(char.character_type, self.gen_healer.character_type)
        self.assertEqual(char.health, self.gen_healer.health)
        self.assertEqual(char.attack, self.gen_healer.attack)
        self.assertEqual(char.defense, self.gen_healer.defense)
        self.assertEqual(char.speed, self.gen_healer.speed)
        self.assertEqual(char.rank, self.gen_healer.rank)
        self.assertEqual(char.special_points, self.gen_healer.special_points)
        self.assertEqual(char.position, None)
        self.assertEqual(char.guardian, None)

    def test_to_json_gentank(self):
        data: dict = self.gen_tank.to_json()
        char: GenericTank = GenericTank().from_json(data)
        self.assertEqual(char.name, self.gen_tank.name)
        self.assertEqual(char.character_type, self.gen_tank.character_type)
        self.assertEqual(char.health, self.gen_tank.health)
        self.assertEqual(char.attack, self.gen_tank.attack)
        self.assertEqual(char.defense, self.gen_tank.defense)
        self.assertEqual(char.speed, self.gen_tank.speed)
        self.assertEqual(char.rank, self.gen_tank.rank)
        self.assertEqual(char.special_points, self.gen_tank.special_points)
        self.assertEqual(char.position, None)
        self.assertEqual(char.guardian, None)

    def test_to_json_leader(self):
        data: dict = self.leader.to_json()
        char: Leader = Leader().from_json(data)
        self.assertEqual(char.name, self.leader.name)
        self.assertEqual(char.character_type, self.leader.character_type)
        self.assertEqual(char.health, self.leader.health)
        self.assertEqual(char.attack, self.leader.attack)
        self.assertEqual(char.defense, self.leader.defense)
        self.assertEqual(char.speed, self.leader.speed)
        self.assertEqual(char.rank, self.leader.rank)
        self.assertEqual(char.special_points, self.leader.special_points)
        self.assertEqual(char.position, None)
        self.assertEqual(char.guardian, None)




        # continue here...
        # reference the to_ and from_json methods in the actual classes to see what is stored.
        # do this for Character, GenericAttacker, GenericHealer, GenericTank, and Leader
        # make sure to check the rank type especially for all of them
        # test the to_ and from_json methods work


