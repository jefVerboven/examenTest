from Player import Player
from Match import Match


class Tournament:
    def __init__(self, name: str):
        self.name = name
        self.__players: list[Player] = []
        self.__matches: list[Match] = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, value: str) -> None:
        if isinstance(value, str) and value.strip() != "":
            self.__name = value.strip()
        else:
            raise ValueError("Invalid tournament name")

    
    def add_player(self, player: Player) -> None:
        if not isinstance(player, Player):
         raise ValueError("Invalid player")
        if player in self.__players:
           raise ValueError("Player already added")
        self.__players.append(player)

    def schedule_match(self, player1: Player, player2: Player) -> Match:
        if not isinstance(player1, Player) or not isinstance(player2, Player):
            raise ValueError("Invalid players")
        if player1 == player2:
            raise ValueError("Players must be different")
        m = Match(player1, player2)
        self.__matches.append(m)
        return m

    
    def active_players(self) -> list[Player]:
        output = []
        for p in self.__players:
            if not p.is_exhausted():
                output.append(p)
        return output
    
    @property
    def total_matches(self) -> int:
        return len(self.__matches)