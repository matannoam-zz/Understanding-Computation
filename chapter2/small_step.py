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


class Add(ExpressionMixin):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    @property
    def clean_repr(self):
        return f'{self.left.clean_repr} + {self.right.clean_repr}'
