import unittest

from game.commander_clash.character.character import Generic, Leader, GenericAttacker
from game.commander_clash.validate_team import validate_team_selection as validate
from game.common.enums import SelectLeader, SelectGeneric


class TestValidateTeam(unittest.TestCase):
    """
    Tests the `validate_team_selection` method and what it returns for valid and invalid team selections.
    """

    def setUp(self):
        self.valid_team: tuple[SelectLeader, SelectGeneric, SelectGeneric] = (SelectLeader.ANAHITA,
                                                                              SelectGeneric.GEN_ATTACKER,
                                                                              SelectGeneric.GEN_ATTACKER)

        self.invalid_team: tuple[SelectGeneric, SelectLeader, SelectLeader] = (SelectGeneric.GEN_ATTACKER,
                                                                               SelectLeader.ANAHITA,
                                                                               SelectLeader.BERRY)

    def test_valid_team(self) -> None:
        result: tuple[Leader, Generic, Generic] = validate(self.valid_team)

        # test that all the characters are instances of the correct class
        self.assertTrue(isinstance(result[0], Leader))
        self.assertTrue(isinstance(result[1], GenericAttacker))
        self.assertTrue(isinstance(result[2], GenericAttacker))

    def test_invalid_team(self) -> None:
        # returns true if all characters returned from the `validate_team_selection()` are GenericAttackers
        self.assertTrue(all([isinstance(character, GenericAttacker) for character in validate(self.invalid_team)]))
