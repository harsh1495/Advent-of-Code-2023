import re

VALID_NUMBERS_MAPPING = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

def find_valid_digits(text: str):
	indexes = {}

	for i in range(len(text)):
		if text[i].isdigit():
			indexes[i] = int(text[i])

	for number in VALID_NUMBERS_MAPPING:
		matches = re.finditer(number, text)
		match_indexes = [match.start(0) for match in matches]

		for index in match_indexes:
			indexes[index] = VALID_NUMBERS_MAPPING[number]

	indexes = sorted(indexes.items())

	return indexes

def main():
	with open("input.txt") as f:
		lines = f.readlines()
	
	_sum = 0

	for line in lines:
		line = line.strip()
		valid_digits_indexes = find_valid_digits(line)
		number = valid_digits_indexes[0][1] * 10 + valid_digits_indexes[-1][1] 
		_sum += number

	return _sum


_sum = main()
print(_sum)