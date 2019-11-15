#def int_validation(prompt):
#	while True:
#		if prompt.isdigit():
#			return int(prompt)
#		else:
#			prompt = input("This is not a valid number. Try again. ")


def minimum(numbers):
	smallest_number = numbers[0]
	for index in range(1, 5):
		if smallest_number < numbers[index]:
			pass
		else:
			smallest_number = numbers[index]
	return smallest_number


def next_smallest(numbers):
	next_smallest_number = numbers[0]

