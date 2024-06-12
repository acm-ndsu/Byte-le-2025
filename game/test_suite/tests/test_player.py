import unittest
from game.common.player import Player
from game.common.enums import *
from game.common.team_manager import TeamManager
import game.test_suite.utils


class TestPlayer(unittest.TestCase):
    """
    `Test Player Notes:`

        This class tests the different methods in the Player class.
    """
    pass
    # WRITE TESTS FOR PLAYER WHEN TEAM MANAGER AND PLAYER FINISHED

    # def test_actions(self):
    #     # accepts a list of ActionType
    #     self.actions = [ActionType.MOVE_LEFT]
    #     self.player.actions = self.actions
    #     self.assertEqual(self.player.actions, self.actions)
    #
    # # test action
    # def setUp(self) -> None:
    #     self.object_type: ObjectType = ObjectType.PLAYER
    #     self.functional: bool = True
    #     self.player: Player = Player()
    #     self.actions: list[ActionType] = []
    #     self.team_name: str | None = ""
    #     self.avatar: TeamManager | None = TeamManager()
    #     self.utils = game.test_suite.utils
    #
    # def test_actions_empty_list(self):
    #     # accepts a list of ActionType
    #     self.actions = []
    #     self.player.actions = self.actions
    #     self.assertEqual(self.player.actions, self.actions)
    #
    # def test_actions_fail_none(self):
    #     value: list = None
    #     with self.assertRaises(ValueError) as e:
    #         self.player.actions = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.action must be an empty list or a list '
    #                                        f'of action types.'
    #                                        f' It is a(n) {value.__class__.__name__} and has the value of {value}.'
    #                                            , False))
    #
    #     def test_actions_fail_not_action_type(self):
    #         value: int = 10
    #         with self.assertRaises(ValueError) as e:
    #             self.player.actions = value
    #
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.action must be an empty list or a list '
    #                                        f'of action types. It is a(n) {value.__class__.__name__} and has the value '
    #                                        f'of {value}.', False))
    #
    # # test functional
    # def test_functional_true(self):
    #     # functional can only be a boolean
    #     self.player.functional = True
    #     self.functional = True
    #     self.assertEqual(self.player.functional, self.functional)
    #
    # def test_functional_false(self):
    #     self.player.functional = False
    #     self.functional = False
    #     self.assertEqual(self.player.functional, self.functional)
    #
    # def test_functional_fail_int(self):
    #     value: str = 'Strig'
    #     with self.assertRaises(ValueError) as e:
    #         self.player.functional = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.functional must be a boolean.'
    #                                        f' It is a(n) {value.__class__.__name__} and has the value of {value}.'
    #                                            , False))
    #
    # # team name
    # def test_team_name(self):
    #     # if it is a string it passes
    #     self.team_name = ""
    #     self.player.team_name = ""
    #     self.assertEqual(self.player.team_name, self.team_name)
    #
    # def test_team_name_none(self):
    #     # if it is none it passes
    #     self.team_name = None
    #     self.assertEqual(self.player.team_name, self.team_name)
    #
    # def test_team_name_fail_int(self):
    #     # if it is not a string it fails
    #     value: int = 1
    #     with self.assertRaises(ValueError) as e:
    #         self.player.team_name = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.team_name must be a String or None.'
    #                                        f' It is a(n) {value.__class__.__name__} and has the value of {value}.'
    #                                            , False))
    #
    # # test avatar
    # def test_avatar(self):
    #     self.avatar = TeamManager()
    #     self.player.avatar = self.avatar
    #     self.assertEqual(self.player.avatar, self.avatar)
    #
    # def test_avatar_none(self):
    #     self.avatar = None
    #     self.assertEqual(self.player.avatar, self.avatar)
    #
    # def test_avatar_fail_string(self):
    #     value: int = 10
    #     with self.assertRaises(ValueError) as e:
    #         self.player.avatar = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.avatar must be Avatar or None. It is a(n)'
    #                                                              f' {value.__class__.__name__} and has the value of '
    #                                                              f'{value}.', False))
    #
    # # test object type
    # def test_object_type(self):
    #     # object type only accepts object type
    #     self.object_type = ObjectType.PLAYER
    #     self.player.object_type = self.object_type
    #     self.assertEqual(self.player.object_type, self.object_type)
    #
    # def test_object_type_fail_none(self):
    #     value: ObjectType = None
    #     with self.assertRaises(ValueError) as e:
    #         self.player.object_type = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.object_type must be ObjectType. It is '
    #                                                              f'a(n) {value.__class__.__name__} and has the value '
    #                                                              f'of {value}.', False))
    #
    # def test_object_type_fail_int(self):
    #     value: int = 10
    #     with self.assertRaises(ValueError) as e:
    #         self.player.object_type = value
    #     self.assertTrue(self.utils.spell_check(str(e.exception), f'Player.object_type must be ObjectType. It is '
    #                                                              f'a(n) {value.__class__.__name__} and has the value '
    #                                                              f'of {value}.', False))
    #
    # # test to json
    # def test_player_json(self):
    #     data: dict = self.player.to_json()
    #     player: Player = Player().from_json(data)
    #     self.assertEqual(self.player.object_type, player.object_type)
    #     self.assertEqual(self.player.functional, player.functional)
    #     self.assertEqual(self.player.team_name, player.team_name)
    #     self.assertEqual(self.player.actions, player.actions)
    #     self.assertEqual(self.player.avatar, player.avatar)
