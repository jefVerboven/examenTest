from Player import Player
from Tournament import Tournament




t = Tournament("Summer Cup")
p1 = Player("Alex", 50, 80)
p2 = Player("Jordan", 60, 75)

t.add_player(p1)
t.add_player(p2)

m = t.schedule_match(p1, p2)
print(m)

print("Total matches:", t.total_matches)
print("Active players:", t.active_players())
