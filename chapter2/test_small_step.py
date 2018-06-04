from unittest import TestCase
from nose.tools import eq_

from small_step import Number, Add


class NumberTests(TestCase):

    def test_not_reducible(self):
        number = Number(1)
        eq_(number.is_reducible(), False)

    def test_stores_value(self):
        number = Number(1)
        eq_(number.value, 1)

    def test_repr(self):
        number = Number(1)
        eq_(str(number), '«1»')

    def test_numbers_equal(self):
        eq_(Number(1), Number(1))

    def test_numbers_not_equal(self):
        self.assertNotEqual(Number(1), Number(2))


class AddTests(TestCase):
    def setUp(self):
        self.number1 = Number(1)
        self.number2 = Number(2)

    def test_repr(self):
        add = Add(self.number1, self.number2)
        eq_(str(add), '«1 + 2»')

    def test_add_is_reducible(self):
        add = Add(self.number1, self.number2)
        eq_(add.is_reducible(), True)

    def test_1_plus_2_reduces_to_3(self):
        add = Add(self.number1, self.number2)
        eq_(add.reduce(), Number(3))

    def test_add_reduces_add_expressions(self):
        add = Add(
            self.number1, Add(
                self.number2, self.number2
            )
        )
        eq_(add.reduce(), Number(5))
