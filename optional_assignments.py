"""
#1 assignment
def divisible(x, y):
	if x % y == 0:
		return True
	else:
		return False
"""
"""
#2 assignment
def cent_change(cents):
	dollars = cents // 100
	a = cents % 100
	quarters = a // 25
	b = a % 25
	dimes = b // 10
	c = b % 10
	nickels = c // 5
	d = c % 5
	pennies = d
"""
"""
#3 assignment
def fibonacci():
	a = 0
	b = 1
	for i in range(1, 20):
		c = a + b
		a = b
		b = c
		print(a)		
fibonacci()
"""

#4 assignment
def int_check(user_input):
	while True:
		if user_input.isdigit():
			return(int(user_input))
		else:
			user_input = input("This is not a numeral value for your input. Try again. ")


def factorial(number):
	a = number
	b = number - 1
	for cat in range(1, number):
		c = a * b
		a = c
		b = b - 1
	return(a)
	

def calculating_e():
	a = 1
	for yowl in range(1, 20):
		a += 1 / factorial(yowl)
	return(a)


purr = input("Input a number. ")
meow = int_check(purr)
print(factorial(meow))
print(calculating_e())
