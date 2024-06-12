import unittest

from game.byte_le_2025.character.character import Character
from game.byte_le_2025.character.generic_attacker import GenericAttacker
from game.byte_le_2025.character.generic_healer import GenericHealer
from game.byte_le_2025.character.generic_tank import GenericTank
from game.byte_le_2025.character.leader import Leader
from game.common.enums import CharacterType


class TestCharacter(unittest.TestCase):
    def setUp(self) -> None:
        self.character: Character = Character('name', CharacterType.TANK)
        self.gen_attacker: GenericAttacker = GenericAttacker('Billy', CharacterType.ATTACKER)
        self.gen_healer: GenericHealer = GenericHealer('Steve', CharacterType.HEALER)
        self.gen_tank: GenericTank = GenericTank('Bertha', CharacterType.TANK)
        self.leader: Leader = Leader('Phil', CharacterType.TANK)

    def test_initalization(self):
        # Test that passing in valid inputs for all the constructor parameters is correct.
        pass

    def test_invalid_initalization(self):
        # Test that passing in bad inputs (a string instead of an int, a None value where it's not needed, etc)
        pass

    def test_to_json(self):
        # test the to and from json methods work
        pass


