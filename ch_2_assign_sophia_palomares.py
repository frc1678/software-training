teams = {}
team_aspects = ["name", "programming language", "width", "length", "camera vision system", "drivetrain motors", "team number"]


#List of Function Operations:
#name_number functions: make team names and number interchangeable for specified functions
#remove_team: removes a team
#modify_team: modifies an attribute of a team
#search_team: searches for an attribute of a team
#add_team: adds a team to the main teams dictionary
#list_team: lists the team #, or keys in the teams dictionary
#exit_program: leaves the program
#main_function: The "main menu" for the other operations

def remove_team_name_number():
	user_remove = input("What team do you want to remove? ")
	for team_name_remove in teams:
		if teams[team_name_remove]["name"] == user_remove:
			remove_team(team_name_remove)
		elif user_remove.isnumeric():
			if int(user_remove) == team_name_remove:
				remove_team(team_name_remove)

def remove_team(team_name_remove):
	teams.pop(team_name_remove)

	main_function()

def modify_team_name_number():
	user_modify = input("What team do you want to modify? ")
	for team_name_modify in teams:
		if teams[team_name_modify]["name"] == user_modify:
			modify_team(team_name_modify)
		elif user_modify.isnumeric():
			if int(user_modify) == team_name_modify:
				modify_team(team_name_modify)

def modify_team(team_name_modify):
	print("Options:")
	print(team_aspects)
	team_attribute_modify = input("What would you like to modify about the team? ")
	for team_aspect in team_aspects:
		if team_attribute_modify == team_aspect:
			new_attribute = input("What is the team's updated attribute? ")
			teams[team_name_modify][team_aspect] = new_attribute
			break
	else:
		print("Input Unknown")
		modify_team(team_name_modify)

	validation_modify_team(team_name_modify)
	main_function()

def validation_modify_team(team_name_modify):
	for digit_answers in team_digit_answers:
		if digit_answers[0].isdigit():
			digit_answers = int(digit_answers)
			team_name_modify[digit_answer] = digit_answers
		else:
			print("Input wasn't a number, please enter number")
			print(digit_answers)
			digit_answer = int(input("Please enter the new answer "))
			team_name_modify[digit_answers] = digit_answer

def add_team():
	temp_team_dictionary = {}

	name = input("What is the name of your team? ")
	p_language = input("What is your team's programming language? ")
	width = input("What is your team's robot's width? ")
	length = input("Wnat is your team's robot's length? ")
	cam_vision = input("Does your team's robot's have a camera vision system? ")
	drive_motors = input("How many drivetrain motors does your team have? ")

	temp_team_dictionary["name"] = name
	temp_team_dictionary["programming language"] = p_language
	temp_team_dictionary["width"] = width
	temp_team_dictionary["length"] = length
	temp_team_dictionary["camera vision system"] = cam_vision
	temp_team_dictionary["drivetrain motors"] = drive_motors

	team_number_input = input("Add a team number ")
	
	if team_number_input[0].isdigit():
		team_number_input = int(team_number_input)
		teams[team_number_input] = temp_team_dictionary
	
	else:
		print("Input wasn't a number, please enter a team number")
		team_number_input = int(input("Add a team number "))
		teams[team_number_input] = temp_team_dictionary

	validation_add_team(team_number_input)
	main_function()

def validation_add_team(team_number_input):
	for data_field in ["width", "length", "drivetrain motors"]:
		if teams[team_number_input][data_field].isdigit():
			teams[team_number_input][data_field] = int(teams[team_number_input][data_field])
		else:
			print("Input wasn't a number, please enter number")
			print(data_field)
			data_field = int(input("Please enter the new answer "))
			teams[team_number_input][data_field] = data_fields

def search_team_name_number():
	user_search = input("What team do you want to search? ")
	for team_name_search in teams:
		if teams[team_name_search]["name"] == user_search:
			search_team(team_name_search)
		elif user_search.isnumeric():
			if int(user_search) == team_name_search:
				search_team(team_name_search)

def search_team(team_name_search):
	print("Options:")
	print(team_aspects)
	user_search_specific = input("What would you like to look up about a team? ")
	for team_aspect in team_aspects:
		if user_search_specific == team_aspect:
			print(user_search_specific)
			print(teams[team_name_search][user_search_specific])
			break
	else:
		print("Unknown Input")
		search_team(team_name_search)

	main_function()

def list_team():
	print(teams.keys())

	main_function()

def exit_program():
	print("You are choosing to exit the program")
	user_exit = input("Are you sure you want to leave? (y/n) ")
	if user_exit == "y":
		"You are now leaving the program"
		return
	elif user_exit == "n":
		"You chose to stay in the program"
		main_function()
	else:
		print("Input is unknown. Please input y or n")
		exit_program()

def main_function():
	print("Options:")
	print("add team, remove team, modify team, list of teams, search for team, exit")
	user_question_1 = input("What would you like to do? ")
	if user_question_1 == "add team":
		add_team()
	elif user_question_1 == "modify team":
		modify_team_name_number()
	elif user_question_1 == "remove team":
		remove_team_name_number()
	elif user_question_1 == "search for team":
		search_team_name_number()
	elif user_question_1 == "list of teams":
		list_team()
	elif user_question_1 == "exit":
		exit_program()
	else:
		print("Input is unknown.")
		main_function()

main_function()