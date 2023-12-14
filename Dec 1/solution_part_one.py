def find_first_and_last_digit(text: str):
	for char in text:
		if char.isdigit():
			first = int(char)
			break

	for i in range(len(text)-1, -1, -1):
		if text[i].isdigit():
			last = int(text[i])
			break

	number = first * 10 + last
	return number

def main():
	with open("input.txt") as f:
		lines = f.readlines()
	
	_sum = 0

	for line in lines:
		number = find_first_and_last_digit(line)
		_sum += number

	return _sum


_sum = main()
print(_sum)



