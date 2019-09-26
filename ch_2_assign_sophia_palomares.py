teams = {}

def main_function():
	user_question_1 = input("What would you like to do? ")
	if(user_question_1 == "Add Team"):
		add_team()
		main_function()
	elif(user_question_1 == "Remove Team"):
		print("Please use only the team's number")
		remove_teams()
		main_function()
	elif(user_question_1 == "Search for Team"):
		print("Please use only the team's number")
		search_team()
		main_function()
	elif(user_question_1 == "List of Teams"):
		list_team()
		main_function()
	elif(user_question_1 == "Exit"):
		exit_program()

	else:
		print("Input is unknown. Please input Add Team, Remove Team, List of Teams, Search for Team, or Exit.")
		main_function()
def remove_teams():
	key = int(input("What team do you want to remove? "))
	teams.pop(key)

def add_team():
	temp_team_dictionary = {}

	name = input("What is the name of your team? ")
	p_language = input("What is your team's programming language? ")
	width = int(input("What is your team's robot's width? "))
	length = int(input("Wnat is your team's robot's length? "))
	cam_vision = input("Does your team's robot's have a camera vision system? ")
	drive_motors = int(input("How many dritrain motors does your team have? "))

	temp_team_dictionary["name"] = name
	temp_team_dictionary["programming language"] = p_language
	temp_team_dictionary["width"] = width
	temp_team_dictionary["length"] = length
	temp_team_dictionary["camera vision system"] = cam_vision
	temp_team_dictionary["drivetrain motors"] = drive_motors

	team_number_input = int(input("Add a team number"))
	teams[team_number_input] = temp_team_dictionary

def search_team():
	user_search = int(input("What team do you want to search? "))
	print("Team Name:")
	print(teams[user_search]["name"])
	print("Programming Language:")
	print(teams[user_search]["programming language"])
	print("Robot's Width:")
	print(teams[user_search]["width"])
	print("Robot's Length:")
	print(teams[user_search]["length"])
	print("Y/N Camera Vision System:")
	print(teams[user_search]["camera vision system"])
	print("Number of Drivetrain Motors:")
	print(teams[user_search]["drivetrain motors"])

def list_team():
	print(teams.keys())

def exit_program():
	print("You are choosing to exit the program")
	user_exit = input("Are you sure you want to leave? ")
	if(user_exit == "Yes"):
		"You are now leaving the program"
	elif(user_exit == "No"):
		"You chose to stay in the program"
		main_function()
	else:
		"Input is unknown. Please input Yes or No"
		exit_program()

main_function()