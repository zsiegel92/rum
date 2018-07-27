from deck import deck,colors,banner
from random import choice, shuffle


shuffle(deck)
# print(deck)



print(banner)
print("Please resize window so that the screen is filled with 4 rows of PLAY RUM (any window width is fine)")



def card(tup):
	return f"|{tup[0]}---{tup[1]},{tup[2]}|"

def pprint(list_of_tuples):
	print("\n".join(card(tup) for tup in list_of_tuples))
	print()

def do_move():
	pass

def spacer(ch='\n'):
	print(ch*30)

while True:
	try:
		num_players = int(input("How many players?   "))
		assert 1 < num_players < 4
		break
	except:
		pass


print(f"{num_players} players")

hands = [[] for i in range(num_players)]
centers = [deck.pop() for i in range(3)]
points = [[] for i in range(num_players)]
open_points = [(color,1) for color in colors]

def printBoard(player=None,continuing=False):
	if player is not None:
		print(f"Player {player}'s turn {'(continued)' if continuing else ''}\n")
		spacer('-')
	for i,hand in enumerate(hands):
		print(f"Player {i}'s points: ")
		print(", ".join((str(pointpair) for pointpair in points[i])))
		print()
	print("Central cards:")
	pprint(centers)
	if player is not None:
		print("Your hand is:")
		pprint(hands[player])


done = False
while not done:
	for i,hand in enumerate(hands):
		input(f"(p{i}) Press ENTER to begin your turn.   ")
		printBoard(i)
		if len(hand)>0:
			if "y" not in input(f"(p{i}) Would you like to play any cards? (y/n)   "):
				hand.append(deck.pop())
				spacer()
				printBoard(i,continuing=True)
				print("You drew")
			else:
				do_move()
				print("doing a move")
				spacer()
				printBoard(i,continuing=True)
				print("You did a move")
		else:
			hand.append(deck.pop())
			spacer()
			printBoard(i)
			print("You had to draw.")
		input(f"(p{i}) Press ENTER to end your turn.   ")
		spacer()

