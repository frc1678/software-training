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
	user_remove = (input("What team do you want to remove? "))
	for x in teams:
		if teams[x]["name"] == user_remove:
			team_name_remove = x
			remove_team(team_name_remove)
		elif user_remove.isnumeric():
			if int(user_remove) == x:
				team_name_remove = x
				remove_team(team_name_remove)

def remove_team(team_name_remove):
	teams.pop(team_name_remove)

	main_function()

def modify_team_name_number():
	user_modify = input("What team do you want to modify? ")
	for x in teams:
		if teams[x]["name"] == user_modify:
			team_name_modify = x
			modify_team(team_name_modify)
		elif user_modify.isnumeric():
			if int(user_modify) == x:
				team_name_modify = x
				modify_team(team_name_modify)

def modify_team(team_name_modify):
	print("Options:")
	print(team_aspects)
	team_attribute_modify = input("What would you like to modify about the team? ")
	#how do i make this work? will this work?
	'''for team_aspect in team_aspects:
		if team_attribute_modify == team_aspect:
			new_attribute = input("What is the team's updated attribute? ")
			teams[team_name_modify][team_aspect] = new_attribute
			break
		else:
			print("Input Unknown")
			modify_team(team_name_modify)'''
	if team_attribute_modify == "Team Name":
		new_name = input("What is the new team name? ")
		teams[team_name_modify]["name"] = new_name
	elif team_attribute_modify == "Programming Language":
		new_p_language = input("What is the team's new programming language? ")
		teams[team_name_modify]["programming language"] = new_p_language
	elif team_attribute_modify == "Robot Width":
		new_width = input("What is the Robot's updated width? ")
		teams[team_name_modify]["width"] = new_width
	elif team_attribute_modify == "Robot Length":
		new_length = input("What is the robot's updated length?")
		teams[team_name_modify]["length"] = new_length
	elif team_attribute_modify == "Camera Vision System":
		new_cam_vis_system = input("Does the team have a camera vision system? ")
		teams[team_name_modify]["camera vision system"] = new_cam_vis_system
	elif team_attribute_modify == "Drivetrain Motors":
		new_drive_motors = input("What is the team's updated drivetrain motors? ")
		teams[team_name_modify]["drivetrain motors"] = new_drive_motors
	elif team_attribute_modify == "Team Number":
		new_team_number = int(input("What is the team's new team number? "))
		teams[new_team_number] = teams.pop(team_name_modify)
	
	main_function()

def add_team():
	temp_team_dictionary = {}

	name = input("What is the name of your team? ")
	p_language = input("What is your team's programming language? ")
	width = int(input("What is your team's robot's width? "))
	length = int(input("Wnat is your team's robot's length? "))
	cam_vision = input("Does your team's robot's have a camera vision system? ")
	drive_motors = int(input("How many drivetrain motors does your team have? "))

	temp_team_dictionary["name"] = name
	temp_team_dictionary["programming language"] = p_language
	temp_team_dictionary["width"] = width
	temp_team_dictionary["length"] = length
	temp_team_dictionary["camera vision system"] = cam_vision
	temp_team_dictionary["drivetrain motors"] = drive_motors

	team_number_input = int(input("Add a team number "))
	teams[team_number_input] = temp_team_dictionary

	main_function()

def search_team_name_number():
	user_search = (input("What team do you want to search? "))
	for x in teams:
		if teams[x]["name"] == user_search:
			team_name_search = x
			search_team(team_name_search)
		elif user_search.isnumeric():
			if int(user_search) == x:
				team_name_search = x
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
	user_exit = input("Are you sure you want to leave? ")
	if user_exit == "Yes":
		"You are now leaving the program"
		return None
	elif user_exit == "No":
		"You chose to stay in the program"
		main_function()
	else:
		print("Input is unknown. Please input Yes or No")
		exit_program()

def main_function():
	print("Options:")
	print("Add Team, Remove Team, Modify Team, List of Teams, Search for Team, Exit")
	user_question_1 = input("What would you like to do? ")
	if user_question_1 == "Add Team":
		add_team()
	elif user_question_1 == "Modify Team":
		modify_team_name_number()
	elif user_question_1 == "Remove Team":
		remove_team_name_number()
	elif user_question_1 == "Search for Team":
		search_team_name_number()
	elif user_question_1 == "List of Teams":
		list_team()
	elif user_question_1 == "Exit":
		exit_program()
	else:
		print("Input is unknown.")
		main_function()

main_function()