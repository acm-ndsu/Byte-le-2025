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

        # keep checking the class properties like this.

        # it'll be different for an object that's allowed to be None like the position.
            # in that case, test it with a different class (e.g., self.gen_tank.position = self.character)

        # since a lot of this is comparing strings, you can use the spell_check method.
            # Set the bool to True to print the differences. Set it to False to not print anything (look at method docs)

    def test_to_json(self):
        data: dict = self.character.to_json()
        char: Character = Character().from_json(data)
        self.assertEqual(char.name, self.character.name)
        self.assertEqual(char.character_type, self.character.character_type)
        self.assertEqual(char.health, self.character.health)
        # continue here...
        # reference the to_ and from_json methods in the actual classes to see what is stored.
        # do this for Character, GenericAttacker, GenericHealer, GenericTank, and Leader
        # make sure to check the rank type especially for all of them
        # test the to_ and from_json methods work

