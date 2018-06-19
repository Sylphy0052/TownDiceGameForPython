from src.facility import *

class FacilityFactory:
    def __init__(self, player):
        self.player = player

    def create_facility(self, facility_type):
        if facility_type is FacilityType.WheatField:
            return WheatField(self.player)
        elif facility_type is FacilityType.Ranch:
            return Ranch(self.player)
        elif facility_type is FacilityType.Bakery:
            return Bakery(self.player)
        elif facility_type is FacilityType.Cafe:
            return Cafe(self.player)
        elif facility_type is FacilityType.ConvenienceStore:
            return ConvenienceStore(self.player)
        elif facility_type is FacilityType.Forest:
            return Forest(self.player)
        elif facility_type is FacilityType.Stadium:
            return Stadium(self.player)
        elif facility_type is FacilityType.TVStation:
            return TVStation(self.player)
        elif facility_type is FacilityType.BusinessCenter:
            return BusinessCenter(self.player)
        elif facility_type is FacilityType.CheeseFactory:
            return CheeseFactory(self.player)
        elif facility_type is FacilityType.FurnitureFactory:
            return FurnitureFactory(self.player)
        elif facility_type is FacilityType.Mine:
            return Mine(self.player)
        elif facility_type is FacilityType.FamilyRestaurant:
            return FamilyRestaurant(self.player)
        elif facility_type is FacilityType.AppleOrchard:
            return AppleOrchard(self.player)
        elif facility_type is FacilityType.FruitAndVegetableMarket:
            return FruitAndVegetableMarket(self.player)

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
