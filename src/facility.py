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

class Facility:
    def __init__(self, facility_type):
        num = 0
        self.facility_type = facility_type

    def play(self):
        pass

    def get_name(self):
        return self.facility_type.name
