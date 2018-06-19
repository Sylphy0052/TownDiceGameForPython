from enum import Enum

'''
施設カード
play:効果を発揮
'''

class FacilityType(Enum):
    WheatField = 1
    Ranch = 2
    Bakery = 3
    Cafe = 4
    ConvenienceStore = 5
    Forest = 6
    Stadium = 7
    TVStation = 8
    BusinessCenter = 9
    CheeseFactory = 10
    FurnitureFactory = 11
    Mine = 12
    FamilyRestaurant = 13
    AppleOrchard = 14
    FruitAndVegetableMarket = 15

class Color(Enum):
    Red = 1
    Green = 2
    Blue = 3
    Purple = 4

class Facility:
    def __init__(self, name, pip, cost, color):
        self.name = name
        self.pip = pip
        self.cost = cost
        self.color = color

    def get_name(self):
        return self.name

    def get_pip(self):
        return self.pip

    def get_cost(self):
        return self.cost

    def get_color(self):
        return self.color

class WheatField(Facility):
    def __init__(self):
        super().__init__("Wheat Field", [1], 1, Color.Blue)

    def play(self):
        return 1

class Bakery(Facility):
    def __init__(self):
        super().__init__("Bakery", [2, 3], 1, Color.Green)

    def play(self):
        return 1
