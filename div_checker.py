def div_checker():
	input1 = int(input("What is the first #? "))
	input2 = int(input("What is the second #? "))
	answer1 = input1 / input2
	answer2 = input2 / input1
	for answer in [answer1, answer2]:
		if isinstance(answer,float):
			answer_int = int(answer)
			answer_check = answer - answer_int
			if answer_check == 0.0:
				print("Yes they are divisable")
				print(answer)
				break
		else:
			break
	else:
		print("No they aren't divisable")

div_checker()