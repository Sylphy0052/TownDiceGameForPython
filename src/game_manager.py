from src.player import Player
# import sys

class GameManager:
    def __init__(self):
        self.player_num = int(input("How many player? > "))
        while(True):
            if self.player_num < 1 or self.player_num > 4:
                print("Player number is from 1 to 4 !")
                self.player_num = int(input("How many player? > "))
            else:
                break
        self.player = []
        for i in range(self.player_num):
            self.player.append(Player(i + 1))

        while(True):
            for i in range(self.player_num):
                self.play_turn(i)

    def play_turn(self, player_num):
        main_player = self.player[player_num]
        print("Turn of Player{}!".format(player_num + 1))
        input("Shake dice! Please push EnterKey!")
        dice = main_player.shake_dice()
        print("The pip is {}!".format(dice))

        # 赤施設
        current_player_num = player_num + 1
        for i in range(self.player_num - 1):
            current_player_num = (current_player_num + i) % self.player_num
            current_player = self.player[current_player_num]
            move_money = current_player.play_red_facility(dice)
            sub_money = main_player.sub_money(move_money)
            current_player.add_money(sub_money)

        # 緑施設
        main_player.play_green_facility(dice)

        # 青施設
        current_player_num = player_num
        for i in range(self.player_num):
            current_player_num = (current_player_num + i) % self.player_num
            current_player = self.player[current_player_num]
            current_player.play_blue_facility(dice)

        # 紫施設

        # for p in self.player:
        #     p.print_having_money()
        #     p.print_having_facility()

        # 購入フェーズ
        print("Player{} Purchase Phase!".format(player_num + 1))
        main_player.purchase()

        main_player.print_having_money()
        main_player.print_having_facility()
