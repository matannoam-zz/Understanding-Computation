class ExpressionMixin:
    def __repr__(self):
        return f'«{self.clean_repr}»'


class Number(ExpressionMixin):

    def __init__(self, value):
        self.value = value

    def is_reducible(self):
        return False

    @property
    def clean_repr(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Add(ExpressionMixin):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self):
        return Number(self.left.value + self.right.value)

    @property
    def clean_repr(self):
        return f'{self.left.clean_repr} + {self.right.clean_repr}'

    def is_reducible(self):
        return True
