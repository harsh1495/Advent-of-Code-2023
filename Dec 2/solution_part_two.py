import re


TOTAL_RED = 12
TOTAL_GREEN = 13
TOTAL_BLUE = 14

# game id: red: int, blue: int, green: int
result = {}

# regex pattern for fetching number of balls for each color in a game set
pattern = r'((\d+)\sred)|((\d+)\sblue)|((\d+)\sgreen)'

def find_power(result):
	return result["red"] * result["blue"] * result["green"]

def bootstrap_result():
	return {
		"red": 0,
		"blue": 0,
		"green": 0
	}


def find_number_of_each_color(game_set: str, game_result: dict):
	red = blue = green = 0
	groups = re.findall(pattern, game_set)

	for group in groups:
		for idx in range(len(group)):
			if 'red' in group[idx]:
				red = int(group[idx+1])
				
				if red > game_result["red"]:
					game_result["red"] = red

			elif 'blue'  in group[idx]:
				blue = int(group[idx+1])
				if blue > game_result["blue"]:
					game_result["blue"] = blue

			elif 'green' in group[idx]:
				green = int(group[idx+1])
				if green > game_result["green"]:
					game_result["green"] = green

			else:
				continue

	return game_result

def parse_input():
	with open("input.txt") as f:
		lines = f.readlines()

	return lines

def main():
	games = parse_input()
	game_id = 1

	for game in games:
		game_result = bootstrap_result()
		game_set = game.split(";")

		for _set in game_set:
			game_result = find_number_of_each_color(_set, game_result)

		result.update({game_id: game_result})
		game_id += 1

	_sum = 0
	for game_id in result:
		power = find_power(result[game_id])
		_sum += power

	return _sum

_sum = main()
print(_sum)



