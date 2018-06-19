from src.facility import *
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

    def purchase(self):
        if self.money == 0:
            print("You got 1 coin!")
            self.money += 1
        else:
            print("You have {} coins!".format(self.money))
        facility_list = self.ff.get_facility_list()
        number = 1
        print("0: None")
        for fl in facility_list:
            if self.money < fl[1]:
                pass
            else:
                print("{}: {} - {}".format(number, fl[0], fl[1]))
            number += 1

        input_num = input("Select number what you want facility! > ")
        while(True):
            if input_num == "":
                input_num = input("Select number what you want facility! > ")
            else:
                input_num = int(input_num)
                if self.money < facility_list[input_num - 1][1]:
                    print("You can't buy the facility...")
                    input_num = input("Select number what you want facility! > ")
                else:
                    break
        if not input_num == 0:
            self.add_facility(FacilityType(input_num))
        else:
            print("You didn't buy anything...")

    def add_facility(self, facility_type):
        purchased_facility = self.ff.create_facility(facility_type)
        self.money -= purchased_facility.get_cost()
        if purchased_facility.get_color() is Color.Blue:
            self.blue_facility.append(purchased_facility)
        elif purchased_facility.get_color() is Color.Green:
            self.green_facility.append(purchased_facility)
        elif purchased_facility.get_color() is Color.Red:
            self.red_facility.append(purchased_facility)
        elif purchased_facility.get_color() is Color.Purple:
            self.purple_facility.append(purchased_facility)

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

    def get_money(self):
        return self.money
