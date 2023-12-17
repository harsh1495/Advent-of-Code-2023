import re


TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

# game id: valid or not
result = {}

# regex pattern for fetching number of balls for each color in a game set
pattern = r'((\d+)\sred)|((\d+)\sblue)|((\d+)\sgreen)'

def find_number_of_each_color(game_set: str):
	red = blue = green = 0
	groups = re.findall(pattern, game_set)

	for group in groups:
		for idx in range(len(group)):
			if 'red' in group[idx]:
				red = int(group[idx+1])
			elif 'blue'  in group[idx]:
				blue = int(group[idx+1])
			elif 'green' in group[idx]:
				green = int(group[idx+1])
			else:
				continue

	return red, blue, green

def parse_input():
	with open("input.txt") as f:
		lines = f.readlines()

	return lines

def main():
	games = parse_input()
	game_id = 1

	for game in games:
		game_set = game.split(";")
		result[game_id] = True

		for _set in game_set:
			red, blue, green = find_number_of_each_color(_set)

			if red > TOTAL_RED or blue > TOTAL_BLUE or green > TOTAL_GREEN:
				result[game_id] = False
				break
		
		game_id += 1

	_sum = 0
	for game_id in result:
		if result[game_id]:
			_sum += game_id

	return _sum

_sum = main()
print(_sum)



