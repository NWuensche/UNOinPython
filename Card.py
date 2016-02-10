from enum import Enum


class Color(Enum):
    blue = 0
    red = 1
    yellow = 2
    green = 3


class Value(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    draw2 = 11
    skip = 12
    revese = 13


class Card():
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def getColor(self):
        return self.color.value

    def getValue(self):
        return self.value
