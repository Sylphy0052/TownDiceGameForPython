from enum import Enum

class LandmarkType(Enum):
    TrainStation = 1
    ShoppingMall = 2
    AmusementPark = 3
    RadioTower = 4

class Landmark:
    def __init__(self, landmark_type):
        self.landmark_type = landmark_type

    def play(self):
        pass

    def get_name(self):
        return self.landmark_type.name
