import unittest

from game.byte_2025.moves.moves import *
from game.byte_2025.moves.submoves import *
from game.common.enums import *


class TestMove(unittest.TestCase):
    """
    `Test Move Notes:`

        This class tests the different methods in the Move class.
        This class tests that, along with the other values, submoves nests properly, including in jsons.
    """
    # NEED TO TEST THE USE ACTION METHODS WHEN FULLY IMPLEMENTED
    def setUp(self) -> None:
        self.move: Move = Move()
        self.submove: Submove = Submove()
        self.subattack: AttackSubmove = AttackSubmove()
        self.subdebuff: DebuffSubmove = DebuffSubmove()
        self.attack: Attack = Attack(name='Basic Attack', damage_points=1)
        self.heal: Heal = Heal(name='Basic Heal', heal_points=1)
        self.buff: Buff = Buff('Big Buff', target_type=TargetType.ALL_ALLY, buff_amount=2.0, submove=self.subdebuff)
        self.debuff: Debuff = Debuff(name='Big Debuff', cost=2, debuff_amount=2.0, submove=self.subattack)

    def test_base_setters(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.move.name = 12
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.name must be a string. It is a(n) '
                                           f'{int.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.move.name = None
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.name must be a string. It is a(n) '
                                           f'NoneType and has the value of {None}.')
        with self.assertRaises(ValueError) as e:
            self.move.cost = '12'
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.cost must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.move.cost = None
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.cost must be an int. '
                                           f'It is a(n) NoneType and has the value of {None}.')
        with self.assertRaises(ValueError) as e:
            self.move.submove = 12
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.submove must be a Move or None. '
                                           f'It is a(n) {int.__name__} and has the value of {12}.')

    def test_attack_init(self) -> None:
        self.assertEqual(self.attack.name, 'Basic Attack')
        self.assertEqual(self.attack.move_type, MoveType.ATTACK)
        self.assertEqual(self.attack.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.attack.cost, 0)
        self.assertEqual(self.attack.submove, None)
        self.assertEqual(self.attack.damage_points, 1)

    def test_attack_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.attack.damage_points = '12'
        self.assertEqual(str(e.exception), f'{self.attack.__class__.__name__}.damage_points must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.attack.damage_points = None
        self.assertEqual(str(e.exception), f'{self.attack.__class__.__name__}.damage_points must be an int. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_heal_init(self) -> None:
        self.assertEqual(self.heal.name, 'Basic Heal')
        self.assertEqual(self.heal.move_type, MoveType.HEAL)
        self.assertEqual(self.heal.target_type, TargetType.SINGLE_ALLY)
        self.assertEqual(self.heal.cost, 0)
        self.assertEqual(self.heal.submove, None)
        self.assertEqual(self.heal.heal_points, 1)

    def test_heal_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.heal.heal_points = '12'
        self.assertEqual(str(e.exception), f'{self.heal.__class__.__name__}.heal_points must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.heal.heal_points = None
        self.assertEqual(str(e.exception), f'{self.heal.__class__.__name__}.heal_points must be an int. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_buff_init(self) -> None:
        self.assertEqual(self.buff.name, 'Big Buff')
        self.assertEqual(self.buff.move_type, MoveType.BUFF)
        self.assertEqual(self.buff.target_type, TargetType.ALL_ALLY)
        self.assertEqual(self.buff.cost, 0)
        self.assertEqual(self.buff.submove, self.subdebuff)
        self.assertEqual(self.buff.buff_amount, 2.0)

    def test_buff_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.buff.buff_amount = '12'
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.buff_amount must be a float. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.buff.buff_amount = None
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.buff_amount must be a float. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_debuff_init(self) -> None:
        self.assertEqual(self.debuff.name, 'Big Debuff')
        self.assertEqual(self.debuff.move_type, MoveType.DEBUFF)
        self.assertEqual(self.debuff.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.debuff.cost, 2)
        self.assertEqual(self.debuff.submove, self.buff)
        self.assertEqual(self.debuff.submove.submove, self.subattack)
        self.assertEqual(self.debuff.debuff_amount, 2.0)

    def test_debuff_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.debuff.debuff_amount = '12'
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.debuff_amount must be a float. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.debuff.debuff_amount = None
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.debuff_amount must be a float. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_base_json(self) -> None:
        data: dict = self.move.to_json()
        move: Move = Move().from_json(data)
        self.assertEqual(move.name, self.move.name)
        self.assertEqual(move.move_type, self.move.move_type)
        self.assertEqual(move.target_type, self.move.target_type)
        self.assertEqual(move.cost, self.move.cost)
        self.assertEqual(move.submove, self.move.submove)

    def test_attack_json(self) -> None:
        data: dict = self.attack.to_json()
        attack: Attack = Attack().from_json(data)
        self.assertEqual(attack.name, self.attack.name)
        self.assertEqual(attack.move_type, self.attack.move_type)
        self.assertEqual(attack.target_type, self.attack.target_type)
        self.assertEqual(attack.cost, self.attack.cost)
        self.assertEqual(attack.submove, self.attack.submove)
        self.assertEqual(attack.damage_points, self.attack.damage_points)

    def test_heal_json(self) -> None:
        data: dict = self.heal.to_json()
        heal: Heal = Heal().from_json(data)
        self.assertEqual(heal.name, self.heal.name)
        self.assertEqual(heal.move_type, self.heal.move_type)
        self.assertEqual(heal.target_type, self.heal.target_type)
        self.assertEqual(heal.cost, self.heal.cost)
        self.assertEqual(heal.submove, self.heal.submove)
        self.assertEqual(heal.heal_points, self.heal.heal_points)

    def test_buff_json(self) -> None:
        data: dict = self.buff.to_json()
        buff: Buff = Buff().from_json(data)
        self.assertEqual(buff.name, self.buff.name)
        self.assertEqual(buff.move_type, self.buff.move_type)
        self.assertEqual(buff.target_type, self.buff.target_type)
        self.assertEqual(buff.cost, self.buff.cost)
        self.assertEqual(buff.submove.to_json(), self.buff.submove.to_json())
        self.assertEqual(buff.buff_amount, self.buff.buff_amount)

    def test_debuff_json(self) -> None:
        data: dict = self.debuff.to_json()
        debuff: Debuff = Debuff().from_json(data)
        self.assertEqual(debuff.name, self.debuff.name)
        self.assertEqual(debuff.move_type, self.debuff.move_type)
        self.assertEqual(debuff.target_type, self.debuff.target_type)
        self.assertEqual(debuff.cost, self.debuff.cost)
        self.assertEqual(debuff.submove.to_json(), self.debuff.submove.to_json())
        self.assertEqual(debuff.debuff_amount, self.debuff.debuff_amount)
