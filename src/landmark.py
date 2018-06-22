from enum import Enum

class LandmarkType(Enum):
    TrainStation = 1
    ShoppingMall = 2
    AmusementPark = 3
    RadioTower = 4

class Landmark:
    def __init__(self, name, cost, player):
        self.name = name
        self.cost = cost
        self.player = player

    def play(self):
        pass

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

class TrainStation(Landmark):
    def __init__(self, player):
        super().__init__("Train Station", 4, player)

    def play(self):
        pass
class ShoppingMall(Landmark):
    def __init__(self, player):
        super().__init__("Shopping Mall", 10, player)

    def play(self):
        pass

class AmusementPark(Landmark):
    def __init__(self, player):
        super().__init__("Amusement Park", 16, player)

    def play(self):
        pass

class RadioTower(Landmark):
    def __init__(self, player):
        super().__init__("Radio Tower", 22, player)

    def play(self):
        pass
