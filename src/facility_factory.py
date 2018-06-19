from src.facility import *

class FacilityFactory:
    def __init__(self):
        pass

    def create_facility(self, facility_type):
        if facility_type is FacilityType.WheatField:
            return WheatField()
        elif facility_type is FacilityType.Ranch:
            return Ranch()
        elif facility_type is FacilityType.Bakery:
            return Bakery()
        elif facility_type is FacilityType.Cafe:
            return Cafe()
        elif facility_type is FacilityType.ConvenienceStore:
            return ConvenienceStore()
        elif facility_type is FacilityType.Forest:
            return Forest()
        elif facility_type is FacilityType.Stadium:
            return Stadium()
        elif facility_type is FacilityType.TVStation:
            return TVStation()
        elif facility_type is FacilityType.BusinessCenter:
            return BusinessCenter()
        elif facility_type is FacilityType.CheeseFactory:
            return CheeseFactory()
        elif facility_type is FacilityType.FurnitureFactory:
            return FurnitureFactory()
        elif facility_type is FacilityType.Mine:
            return Mine()
        elif facility_type is FacilityType.FamilyRestaurant:
            return FamilyRestaurant()
        elif facility_type is FacilityType.AppleOrchard:
            return AppleOrchard()
        elif facility_type is FacilityType.FruitAndVegetableMarket:
            return FruitAndVegetableMarket()

    def get_facility_list(self):
        return [
            ["Wheat Field", 1],
            ["Ranch", 1],
            ["Bakery", 1],
            ["Cafe", 2],
            ["Convenience Store", 2],
            ["Forest", 3],
            ["Stadium", 6],
            ["TV Station", 7],
            ["Business Center", 8],
            ["Cheese Factory", 5],
            ["Furniture Factory", 3],
            ["Mine", 6],
            ["Family Restaurant", 3],
            ["Apple Orchard", 3],
            ["Fruit and Vegetable Market", 2],
        ]
