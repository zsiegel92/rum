# Rules:
# https://unlimitedjoystudios.com/rum-pack-o-game-mini-card-game-review/

# 7 colors:
# blue, red, yellow, green, orange, purple, pink

# 21 bottle cards
# 3 of each color as a single bottle
# There are (6 choose 2)*7 (== 15 * 7) possible 3-way cards (== (7 choose 3)*3 == 35 * 3) == 105, so one-fifth are represented
# For each single, there are (6 choose 2) == 15 possible doubles to join them, but only 3 are represented. There are 21 possible doubles (7 choose 2) so perhaps each is represented exactly once. Each color appears the same total number of times in doubles...For each color, there are 18 cards (the non-singles of that color) in which that color can appear as a double, and it appears in 6 of them - presumably once with each other color. Is this possible?

from itertools import combinations,permutations
colors = ['red','yellow','blue','orange','green','purple','pink']

def pprint(dict_of_lists_of_tuples):
	for key in dict_of_lists_of_tuples:
		print(f"{key}: " + " , ".join(str(tup) for tup in dict_of_lists_of_tuples[key]))



def generate_deck():
	tups = {color:[] for color in colors}
	combs = list(combinations(colors,2))
	# print(f"All 2-tuples of colors: {list(combs)}")
	# print(list(combs))


	double_perms = permutations(combs)
	color_perms = permutations(colors)

	breaking = False

	for double_perm in double_perms:
			for color_perm in color_perms:
				triplets = []
				tups = {color:[] for color in colors}
				for comb in double_perm:
					for color in color_perm:
						if (color not in comb) and (len(tups[color]) < 3) and (not any(cnew in tup for tup in tups[color] for cnew in comb)) and (not set((color,) + comb) in triplets):
							tups[color].append(comb)
							triplets.append(set((color,) + comb))
							break
				if not any(len(finTups) < 3 for color,finTups in tups.items()):
					# print("SUCCESS! Breaking.")
					breaking = True
					break
			if breaking:
				break

	# print()
	# pprint(tups)

	# if any(len(finTups) < 3 for color,finTups in tups.items()):
	# 	print("FAILURE!")
	# else:
	# 	print("SUCCESS!")

	# total_triplets = combinations(colors,3)
	# unused_triplets = []

	# for trip in total_triplets:
	# 	if set(trip) not in triplets:
	# 		print(f"{trip} not in deck!")
	# 		unused_triplets.append(set(trip))

	# doub_scores = {comb:0 for comb in combs}
	# doub_unused_scores = {comb: 0 for comb in combs}

	# for comb in combs:
	# 	for trip in deck:
	# 		if set(comb) <= set(trip):
	# 			doub_scores[comb]+=1

	# for comb in combs:
	# 	for unused_trip in unused_triplets:
	# 		if set(comb) <= unused_trip:
	# 			doub_unused_scores[comb]+=1

	# print("NUMBER OF TIMES EACH 2-TUPLE APPEARS")
	# for k,v in doub_scores.items():
	# 	print(f"{k}: {v}")

	# print("NUMBER OF TIMES EACH 2-TUPE APPEARS IN AN UNUSED TRIPLE")
	# for k,v in doub_unused_scores.items():
	# 	print(f"{k}: {v}")


	# print(f"combs is: {list(combs)}")

	deck = [(k,) + t for k in tups for t in tups[k]]
	return deck


# print(deck)

deck = generate_deck()

# Every color is in 9 cards
# Every 2-tuple is in 3 cards
# Every tuple is in exactly 1 card as the "double"
# Not every triple appears even once, no triple appears twice.
# Every color appears in 6 unused triplets. There are 14 unused triplets out of 35 triplets.
# Every 2-tuple (there are 21) appears in 2 unused triples


banner = '''
 ____  _        _ __   __  ____  _   _ __  __
|  _ \\| |      / \\\\ \\ / / |  _ \\| | | |  \\/  |
| |_) | |     / _ \\\\ V /  | |_) | | | | |\\/| |
|  __/| |___ / ___ \\| |   |  _ <| |_| | |  | |
|_|   |_____/_/   \\_\\_|   |_| \\_\\\\___/|_|  |_|

 ____  _        _ __   __  ____  _   _ __  __
|  _ \\| |      / \\\\ \\ / / |  _ \\| | | |  \\/  |
| |_) | |     / _ \\\\ V /  | |_) | | | | |\\/| |
|  __/| |___ / ___ \\| |   |  _ <| |_| | |  | |
|_|   |_____/_/   \\_\\_|   |_| \\_\\\\___/|_|  |_|

 ____  _        _ __   __  ____  _   _ __  __
|  _ \\| |      / \\\\ \\ / / |  _ \\| | | |  \\/  |
| |_) | |     / _ \\\\ V /  | |_) | | | | |\\/| |
|  __/| |___ / ___ \\| |   |  _ <| |_| | |  | |
|_|   |_____/_/   \\_\\_|   |_| \\_\\\\___/|_|  |_|

 ____  _        _ __   __  ____  _   _ __  __
|  _ \\| |      / \\\\ \\ / / |  _ \\| | | |  \\/  |
| |_) | |     / _ \\\\ V /  | |_) | | | | |\\/| |
|  __/| |___ / ___ \\| |   |  _ <| |_| | |  | |
|_|   |_____/_/   \\_\\_|   |_| \\_\\\\___/|_|  |_|
'''
