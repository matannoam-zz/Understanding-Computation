from unittest import TestCase
from nose.tools import eq_

from small_step import Number


class NumberTests(TestCase):

    def test_not_reducible(self):
        number = Number(1)
        eq_(number.is_reducible(), False)

    def test_stores_value(self):
        number = Number(1)
        eq_(number.value, 1)
