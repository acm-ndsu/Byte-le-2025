import unittest

from game.byte_2025.character import *
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
        self.special: Character = Character('Special', CharacterType.TANK, 10, 15, 20, 10,
                                            None, self.leader, {}, 5, Vector(0, 0))
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

        # test that all the parameters are set properly with the constructor
        self.assertEqual(self.special.name, 'Special')
        self.assertEqual(self.special.character_type, CharacterType.TANK)
        self.assertEqual(self.special.health, 10)
        self.assertEqual(self.special.attack, 15)
        self.assertEqual(self.special.defense, 20)
        self.assertEqual(self.special.speed, 10)
        self.assertEqual(self.special.passive, None)
        self.assertEqual(self.special.guardian, self.leader)
        self.assertEqual(self.special.position, Vector(0, 0))

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
        self.assertTrue(
            spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.special_points must be a positive '
                                          f'int.', True))

        # check that a None value fails for special_points
        with self.assertRaises(ValueError) as e:
            self.gen_tank.special_points = self.none
        self.assertTrue(
            spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.special_points must be an int. It '
                                          f'is a(n) {self.none.__class__.__name__} '
                                          f'and has the value of {self.none}', True))

        # check that the Character position has to be a Vector
        value: int = 10
        with self.assertRaises(ValueError) as e:
            self.gen_tank.position = value
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.position must be a Vector '
                                                      f'or None. It is a(n) {value.__class__.__name__} and has the '
                                                      f'value of {value}', False))

        # check that the Character's guardian has to be a Character of None
        with self.assertRaises(ValueError) as e:
            self.gen_tank.guardian = value
        self.assertTrue(spell_check(str(e.exception), f'{self.gen_tank.__class__.__name__}.guardian must be a '
                                                      f'Character or None. It is a(n) {value.__class__.__name__} and '
                                                      f'has the value of {value}', False))

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
