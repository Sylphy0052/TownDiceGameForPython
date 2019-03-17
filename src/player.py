from src.facility import *
from src.landmark import Landmark, LandmarkType
from src.facility_factory import FacilityFactory

import random, sys

'''
所持金
施設
ランドマーク
'''
class Player:
    def __init__(self, num):
        self.ff = FacilityFactory(self)
        self.num = num
        # 初期所持金
        self.money = 3
        # 初期施設
        self.green_facility = []
        self.red_facility = []
        self.blue_facility = []
        self.purple_facility = []
        self.having_purple_facility = {}

        # ランドマーク
        self.landmark = {}
        self.init_facility()

        # self.print_having_facility()
        # self.print_having_money()
        # print(self.create_facility_list())
        # print(self.create_landmark_list())

    def create_facility_list(self):
        return [self.ff.create_facility(e) for e in FacilityType]
        # return [[e.name, self.ff.create_facility(FacilityType(e.value)).get_cost()] for e in FacilityType]

    def create_landmark_list(self):
        return [self.ff.create_landmark(e) for e in LandmarkType]
        # return [[e.name, self.ff.create_landmark(LandmarkType(e.value)).get_cost()] for e in LandmarkType]

    def purchase(self, players):
        if self.money == 0:
            print("You got 1 coin!")
            self.money += 1
        else:
            print("You have {} coins!".format(self.money))
        facility_list = self.create_facility_list()
        number = 1
        print("0: None")
        for fl in facility_list:
            if fl.get_color() == Color.Purple and self.having_purple_facility[fl.get_name().replace(' ', '')]:
                pass
            elif self.money < fl.get_cost():
                pass
            else:
                print("{}: {} - {}".format(number, fl.get_name(), fl.get_cost()))
            number += 1

        # ランドマーク表示
        landmark_list = self.create_landmark_list()
        for l in landmark_list:
            landmark_number = number - len(FacilityType)
            # 所持金が足りない
            if self.money < l.get_cost():
                pass
            # すでに所持している
            elif self.landmark[l.get_name().replace(' ', '')] == True:
                pass
            else:
                print("{}: {} - {}".format(number, l.get_name(), l.get_cost()))
            number += 1

        # プレイヤーの所持金表示
        self.print_having_money()

        # プレイヤーの所持施設表示
        self.print_having_facility()

        input_num = input("Select number what you want facility! > ")
        while(True):
            if input_num == "":
                input_num = input("Select number what you want facility! > ")
            else:
                input_num = int(input_num)
                # 施設購入
                if input_num > 0 and input_num <= len(FacilityType):
                    # 購入できない時
                    if facility_list[input_num - 1].get_color() == Color.Purple and self.having_purple_facility[facility_list[input_num - 1].get_name().replace(' ', '')]:
                        print("You can't buy the facility...")
                        input_num = input("Select number what you want facility! > ")
                    elif self.money < facility_list[input_num - 1].get_cost():
                        print("You can't buy the facility...")
                        input_num = input("Select number what you want facility! > ")
                    # 購入できる時
                    else:
                        break
                # ランドマーク建設
                elif input_num > len(FacilityType) and input_num <= len(FacilityType) + len(LandmarkType):
                    # 購入できない時
                    if self.money < landmark_list[input_num - len(FacilityType) - 1].get_cost() or self.landmark[LandmarkType(input_num - len(FacilityType)).name] == True:
                        print("You can't buy the landmark...")
                        input_num = input("Select number what you want facility! > ")
                    # 購入できる時
                    else:
                        break
                else:
                    break

        if not input_num == 0:
            # Facility
            if input_num > 0 and input_num <= len(FacilityType):
                get_facility = FacilityType(input_num)
                self.add_facility(get_facility)
                print("You got {}.".format(get_facility.name))
            # Landmark
            elif input_num > len(FacilityType) and input_num <= len(FacilityType) + len(LandmarkType):
                input_num = input_num - len(FacilityType)
                get_landmark = LandmarkType(input_num)
                self.add_landmark(get_landmark)
                print("You got {}.".format(get_landmark.name))
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
            self.having_purple_facility[facility_type.name] = True

    def add_landmark(self, landmark_type):
        purchased_landmark = self.ff.create_landmark(landmark_type)
        self.money -= purchased_landmark.get_cost()
        self.landmark[landmark_type.name.replace(' ', '')] = True

    def init_facility(self):
        self.blue_facility.append(self.ff.create_facility(FacilityType.WheatField))
        self.green_facility.append(self.ff.create_facility(FacilityType.Bakery))
        for pf in PurpleFacilityType:
            self.having_purple_facility[pf.name] = False

        for l in LandmarkType:
            self.landmark[l.name] = False

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
        money = 0
        for pf in self.purple_facility:
            if dice in pf.get_pip():
                pass

    def shake_dice(self):
        dice_num = 1
        if self.landmark["TrainStation"]:
            dice_num = input("How many dice do you shake?(1 or 2) > ")
            while(True):
                if not dice_num in ["1", "2"]:
                    print("Please input 1 or 2")
                    dice_num = input("How many dice do you shake?(1 or 2) > ")
                else:
                    break
        dice = random.randint(1, 6)
        dice_num = int(dice_num)
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
        print("-----")
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
        for l, flag in self.landmark.items():
            if flag:
                print(l)

        print("-----")

    def get_money(self):
        return self.money
