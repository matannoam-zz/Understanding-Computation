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


class AddTests(TestCase):

    def test_repr(self):
        number1 = Number(1)
        number2 = Number(2)

        add = Add(number1, number2)

        eq_(str(add), '«1 + 2»')
