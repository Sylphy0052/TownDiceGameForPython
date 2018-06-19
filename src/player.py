from src.facility import Facility, FacilityType

'''
所持金
施設
ランドマーク
'''
class Player:
    def __init__(self, num):
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

        self.print_having_facility()
        self.print_having_money()

    def init_facility(self):
        self.blue_facility.append(Facility(FacilityType.WheatField))
        self.green_facility.append(Facility(FacilityType.Bakery))

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
