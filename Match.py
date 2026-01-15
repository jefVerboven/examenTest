from Player import Player
import random

class Match:
    def __init__(self, player1: Player, player2: Player):
        if not isinstance(player1, Player) or not isinstance(player2, Player):
            raise ValueError("Match requires two Players")
        self.__player1 = player1
        self.__player2 = player2
        self.__duration = random.randint(5, 20)
        self.__player1.stamina -= self.__duration
        self.__player2.stamina -= self.__duration
        self.__winner = self.Winner()
    
    @property
    def druation(self) -> int:
     return self.__duration
    
    def Winner(self) -> Player:
        if self.__player1.skill > self.__player2.skill:
           return self.__player1
        elif self.__player1.skill < self.__player2.skill:
            return self.__player2
        else:
           return random.choice([self.__player1, self.__player2])
    def __str__(self):
       return f"Match {self.__player1.name} vs {self.__player2.name} (duration: {self.druation}) - winner : {self.__winner.name}"