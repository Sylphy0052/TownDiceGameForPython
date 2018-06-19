from src.facility import Facility, FacilityType
from src.landmark import Landmark, LandmarkType
from src.facility_factory import FacilityFactory

import random

'''
所持金
施設
ランドマーク
'''
class Player:
    def __init__(self, num):
        self.ff = FacilityFactory()
        self.num = num
        # 初期所持金
        self.money = 3
        # 初期施設
        self.green_facility = []
        self.red_facility = []
        self.blue_facility = []
        self.purple_facility = []
        self.init_facility()
        # ランドマーク
        self.landmark = []
        self.landmark_type = []

        # self.print_having_facility()
        # self.print_having_money()

    def init_facility(self):
        self.blue_facility.append(self.ff.create_facility(FacilityType.WheatField))
        self.green_facility.append(self.ff.create_facility(FacilityType.Bakery))

    def play_red_facility(self, dice):
        money = 0
        for f in self.red_facility:
            if dice in f.get_pip():
                money += f.play()

        return money

    def play_blue_facility(self, dice):
        money = 0
        for f in self.blue_facility:
            if dice in f.get_pip():
                self.money += f.play()

    def play_green_facility(self, dice):
        money = 0
        for f in self.green_facility:
            if dice in f.get_pip():
                self.money += f.play()

    def play_purple_facility(self, dice):
        pass

    def shake_dice(self):
        dice_num = 1
        if LandmarkType.TrainStation in self.landmark_type:
            dice_num = int(input("How many dice do you shake?(1 or 2) > "))
            while(True):
                if not dice_num == 1 and not dice_num == 2:
                    print("Please input 1 or 2")
                    dice_num = int(input("How many dice do you shake?(1 or 2) > "))
                else:
                    break
        dice = random.randint(1, 6)
        if dice_num == 2:
            dice += random.randint(1, 6)
        return dice

    def add_money(self, money):
        self.money += money

    def sub_money(self, money):
        if money > self.money:
            self.money = 0
            return self.money
        else:
            self.money -= money
            return money

    def print_having_money(self):
        print("Player{}".format(self.num))
        print("Money {}".format(self.money))
        print("-----")

    def print_having_facility(self):
        print("Player{}".format(self.num))
        # Blue
        for f in self.blue_facility:
            print(f.get_name())
        # Green
        for f in self.green_facility:
            print(f.get_name())
        # Red
        for f in self.red_facility:
            print(f.get_name())
        # Purple
        for f in self.purple_facility:
            print(f.get_name())
        # Landmark
        for l in self.landmark:
            print(l.get_name())

        print("-----")
