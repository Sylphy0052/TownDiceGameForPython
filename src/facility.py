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

class Ranch(Facility):
    def __init__(self):
        super().__init__("Ranch", [2], 1, Color.Blue)

    def play(self):
        return 1

class Bakery(Facility):
    def __init__(self):
        super().__init__("Bakery", [2, 3], 1, Color.Green)

    def play(self):
        return 1

class Cafe(Facility):
    def __init__(self):
        super().__init__("Cafe", [3], 1, Color.Red)

    def play(self):
        return 1

class ConvenienceStore(Facility):
    def __init__(self):
        super().__init__("Convenience Store", [4], 2, Color.Green)

    def play(self):
        return 3

class Forest(Facility):
    def __init__(self):
        super().__init__("Forest", [5], 3, Color.Blue)

    def play(self):
        return 1

class Stadium(Facility):
    def __init__(self):
        super().__init__("Stadium", [6], 6, Color.Purple)

    def play(self):
        return 1

class TVStation(Facility):
    def __init__(self):
        super().__init__("TV Station", [6], 7, Color.Purple)

    def play(self):
        return 1

class BusinessCenter(Facility):
    def __init__(self):
        super().__init__("Business Center", [6], 8, Color.Purple)

    def play(self):
        return 1

class CheeseFactory(Facility):
    def __init__(self):
        super().__init__("Cheese Factory", [7], 5, Color.Green)

    def play(self):
        return 3

class FurnitureFactory(Facility):
    def __init__(self):
        super().__init__("Furniture Factory", [8], 3, Color.Green)

    def play(self):
        return 3

class Mine(Facility):
    def __init__(self):
        super().__init__("Mine", [9], 6, Color.Blue)

    def play(self):
        return 5

class FamilyRestaurant(Facility):
    def __init__(self):
        super().__init__("Family Restaurant", [9, 10], 3, Color.Red)

    def play(self):
        return 2

class AppleOrchard(Facility):
    def __init__(self):
        super().__init__("Apple Orchard", [10], 3, Color.Blue)

    def play(self):
        return 3

class FruitAndVegetableMarket(Facility):
    def __init__(self):
        super().__init__("Fruit and Vegetable Market", [11, 12], 2, Color.Green)

    def play(self):
        return 2
