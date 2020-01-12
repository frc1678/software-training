teams = {}
team_aspects = ["name", "programming language", "width", "length", "camera vision system", "drivetrain motors", "team number"]
number_aspects = ["width", "length", "drivetrain motors"]
word_aspects = ["name", "programming language", "camera vision system"]

#List of Function Operations:
#name_number functions: make team names and number interchangeable for specified functions
#remove_team: removes a team
#modify_team: modifies an attribute of a team
#search_team: searches for an attribute of a team
#add_team: adds a team to the main teams dictionary
#list_team: lists the team #, or keys in the teams dictionary
#exit_program: leaves the program
#validation: validates input for add team function
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
			for attribute in number_aspects:
				if team_attribute_modify == attribute:
					new_attribute = validation_number(new_attribute)
					break
			for attribute in word_aspects:
				if team_attribute_modify == attribute:
					new_attribute = validation_word(new_attribute)
					break
			teams[team_name_modify][team_aspect] = new_attribute
			break
	else:
		print("Input Unknown")
		modify_team(team_name_modify)

	main_function()

def add_team():
	temp_team_dictionary = {}

	name = input("What is the name of your team? ")
	val_name = validation_word(name)
	p_language = input("What is your team's programming language? ")
	val_p_language = validation_word(p_language)
	width = input("What is your team's robot's width? ")
	val_width = validation_number(width)
	length = input("Wnat is your team's robot's length? ")
	val_length = validation_number(length)
	cam_vision = input("Does your team's robot's have a camera vision system? ")
	val_cam_vision = validation_word(cam_vision)
	drive_motors = input("How many drivetrain motors does your team have? ")
	val_drive_motors = validation_number(drive_motors)

	temp_team_dictionary["name"] = val_name
	temp_team_dictionary["programming language"] = val_p_language
	temp_team_dictionary["width"] = val_width
	temp_team_dictionary["length"] = val_length
	temp_team_dictionary["camera vision system"] = val_cam_vision
	temp_team_dictionary["drivetrain motors"] = val_drive_motors

	team_number_input = input("Add a team number ")
	
	if team_number_input[0].isdigit():
		team_number_input = int(team_number_input)
		teams[team_number_input] = temp_team_dictionary
	
	else:
		print("Input wasn't a number, please enter a team number")
		team_number_input = int(input("Add a team number "))
		teams[team_number_input] = temp_team_dictionary

	main_function()

def validation_number(user_input):
	if user_input.isdigit():
		user_input = int(user_input)
		return user_input
	else:
		print("User input wasn't a number, please enter a number.")
		user_new_input = input("Please enter new answer: ")
		validation_number(user_new_input)
		return user_new_input

def validation_word(user_input):
	if user_input.isdigit() == False:
		return user_input
	else:
		print("User input wasn't a word, please enter a word")
		user_new_input = input("Please enter new answer: ")
		validation_word(user_new_input)
		return user_new_input

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