from src.facility import *
from src.landmark import *

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

    def create_landmark(self, landmark_type):
        if landmark_type is LandmarkType.TrainStation:
            return TrainStation(self.player)
        elif landmark_type is LandmarkType.ShoppingMall:
            return ShoppingMall(self.player)
        elif landmark_type is LandmarkType.AmusementPark:
            return AmusementPark(self.player)
        elif landmark_type is LandmarkType.RadioTower:
            return RadioTower(self.player)
