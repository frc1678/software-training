teams = {}
#make sure this is under 1 function

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
	else:
		print("Input is unknown. Please input Add Team, Remove Team, List of Teams, or Search for Team.")
		main_function()
def remove_teams():
	key = input("What team do you want to remove? ")
	teams.pop(key, value)

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
	team_search = input("What team do you want to search? ")
	#how do I fix this
	search = team_search.items()
	print(teams[search])

def list_team():
	print(teams.keys())

main_function()