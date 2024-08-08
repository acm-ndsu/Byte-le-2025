import unittest

from game.byte_2025.moves.moves import *
from game.byte_2025.moves.effects import *
from game.common.enums import *


class TestMove(unittest.TestCase):
    """
    `Test Move Notes:`

        This class tests the different methods in the Move class.
        This class tests that, along with the other values, effects nests properly, including in jsons.
    """

    def setUp(self) -> None:
        self.move: Move = Move()
        self.effect: Effect = Effect()
        self.attack_effect: AttackEffect = AttackEffect()
        self.debuff_effect: DebuffEffect = DebuffEffect()
        self.attack: Attack = Attack(name='Basic Attack', damage_points=1)
        self.heal: Heal = Heal(name='Basic Heal', heal_points=1)
        self.buff: Buff = Buff('Big Buff', target_type=TargetType.ALL_ALLIES, stage_amount=2,
                               effect=self.debuff_effect)
        self.debuff: Debuff = Debuff(name='Big Debuff', cost=2, stage_amount=-2, effect=self.attack_effect,
                                     stat_to_affect=ObjectType.SPEED_STAT)

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
            self.move.effect = 12
        self.assertEqual(str(e.exception), f'{self.move.__class__.__name__}.effect must be a Move or None. '
                                           f'It is a(n) {int.__name__} and has the value of {12}.')

        # test setting stage amount to 0
        with self.assertRaises(ValueError) as e:
            self.buff.stage_amount = 0
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.stage_amount must be > 0 and <= '
                                           f'{STAGE_MAX}. The value 0 was given')

        # test setting stage amount to a negative number
        with self.assertRaises(ValueError) as e:
            self.buff.stage_amount = -1
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.stage_amount must be > 0 and <= '
                                           f'{STAGE_MAX}. The value -1 was given')

        # test setting stage amount above the max value
        with self.assertRaises(ValueError) as e:
            self.buff.stage_amount = STAGE_MAX + 1
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.stage_amount must be > 0 and <= '
                                           f'{STAGE_MAX}. The value {STAGE_MAX + 1} was given')

        # test setting stage amount to 0
        with self.assertRaises(ValueError) as e:
            self.debuff.stage_amount = 0
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.stage_amount must be >= {STAGE_MIN} '
                                           f'and < 0 . The value 0 was given')

        # test setting stage amount to a positive value
        with self.assertRaises(ValueError) as e:
            self.debuff.stage_amount = 1
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.stage_amount must be >= {STAGE_MIN} '
                                           f'and < 0 . The value 1 was given')

        # test setting stage amount below the min value
        with self.assertRaises(ValueError) as e:
            self.debuff.stage_amount = STAGE_MIN - 1
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.stage_amount must be >= {STAGE_MIN} '
                                           f'and < 0 . The value {STAGE_MIN - 1} was given')

    def test_attack_init(self) -> None:
        self.assertEqual(self.attack.name, 'Basic Attack')
        self.assertEqual(self.attack.move_type, MoveType.ATTACK)
        self.assertEqual(self.attack.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.attack.cost, 0)
        self.assertEqual(self.attack.effect, None)
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
        self.assertEqual(self.heal.target_type, TargetType.ALL_ALLIES)
        self.assertEqual(self.heal.cost, 0)
        self.assertEqual(self.heal.effect, None)
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
        self.assertEqual(self.buff.target_type, TargetType.ALL_ALLIES)
        self.assertEqual(self.buff.stage_amount, 2)
        self.assertEqual(self.buff.cost, 0)
        self.assertEqual(self.buff.effect, self.debuff_effect)
        self.assertEqual(self.buff.stage_amount, 2.0)
        self.assertEqual(self.buff.stat_to_affect, ObjectType.DEFENSE_STAT)

    def test_buff_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.buff.stage_amount = '12'
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.stage_amount must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.buff.stage_amount = None
        self.assertEqual(str(e.exception), f'{self.buff.__class__.__name__}.stage_amount must be an int. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_debuff_init(self) -> None:
        self.assertEqual(self.debuff.name, 'Big Debuff')
        self.assertEqual(self.debuff.move_type, MoveType.DEBUFF)
        self.assertEqual(self.debuff.target_type, TargetType.SINGLE_OPP)
        self.assertEqual(self.debuff.cost, 2)
        self.assertEqual(self.debuff.effect, self.attack_effect)
        self.assertEqual(self.debuff.stage_amount, -2)
        self.assertEqual(self.debuff.stat_to_affect, ObjectType.SPEED_STAT)

    def test_debuff_setter(self) -> None:
        with self.assertRaises(ValueError) as e:
            self.debuff.stage_amount = '12'
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.stage_amount must be an int. '
                                           f'It is a(n) {str.__name__} and has the value of {12}.')
        with self.assertRaises(ValueError) as e:
            self.debuff.stage_amount = None
        self.assertEqual(str(e.exception), f'{self.debuff.__class__.__name__}.stage_amount must be an int. '
                                           f'It is a(n) NoneType and has the value of {None}.')

    def test_base_json(self) -> None:
        data: dict = self.move.to_json()
        move: Move = Move().from_json(data)
        self.assertEqual(move.name, self.move.name)
        self.assertEqual(move.move_type, self.move.move_type)
        self.assertEqual(move.target_type, self.move.target_type)
        self.assertEqual(move.cost, self.move.cost)
        self.assertEqual(move.effect, self.move.effect)

    def test_attack_json(self) -> None:
        data: dict = self.attack.to_json()
        attack: Attack = Attack().from_json(data)
        self.assertEqual(attack.name, self.attack.name)
        self.assertEqual(attack.move_type, self.attack.move_type)
        self.assertEqual(attack.target_type, self.attack.target_type)
        self.assertEqual(attack.cost, self.attack.cost)
        self.assertEqual(attack.effect, self.attack.effect)
        self.assertEqual(attack.damage_points, self.attack.damage_points)

    def test_heal_json(self) -> None:
        data: dict = self.heal.to_json()
        heal: Heal = Heal().from_json(data)
        self.assertEqual(heal.name, self.heal.name)
        self.assertEqual(heal.move_type, self.heal.move_type)
        self.assertEqual(heal.target_type, self.heal.target_type)
        self.assertEqual(heal.cost, self.heal.cost)
        self.assertEqual(heal.effect, self.heal.effect)
        self.assertEqual(heal.heal_points, self.heal.heal_points)

    def test_buff_json(self) -> None:
        data: dict = self.buff.to_json()
        buff: Buff = Buff().from_json(data)
        self.assertEqual(buff.name, self.buff.name)
        self.assertEqual(buff.move_type, self.buff.move_type)
        self.assertEqual(buff.target_type, self.buff.target_type)
        self.assertEqual(buff.cost, self.buff.cost)
        self.assertEqual(buff.effect.to_json(), self.buff.effect.to_json())
        self.assertEqual(buff.stage_amount, self.buff.stage_amount)
        self.assertEqual(buff.stat_to_affect, self.buff.stat_to_affect)

    def test_debuff_json(self) -> None:
        data: dict = self.debuff.to_json()
        debuff: Debuff = Debuff().from_json(data)
        self.assertEqual(debuff.name, self.debuff.name)
        self.assertEqual(debuff.move_type, self.debuff.move_type)
        self.assertEqual(debuff.target_type, self.debuff.target_type)
        self.assertEqual(debuff.cost, self.debuff.cost)
        self.assertEqual(debuff.effect.to_json(), self.debuff.effect.to_json())
        self.assertEqual(debuff.stage_amount, self.debuff.stage_amount)
        self.assertEqual(debuff.stat_to_affect, self.debuff.stat_to_affect)
