from src.player import Player

class GameManager:
    def __init__(self):
        self.player_num = int(input("How many player? > "))
        player = []
        for i in range(self.player_num):
            player.append(Player(i + 1))
