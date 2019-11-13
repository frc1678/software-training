teams = {}

'''
Robot_Team_all = {'1678': {'Number': '1678', 'Name': 'Citrus Circuits', 'Prog. Language': 'Java', 'Width': '15 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera vision system',
	'Drivetrain Motors': '12 drivetrain motors'},
	'744': {'Number': '744', 'Name': 'Shark Attack', 'Prog. Language': 'C++', 'Width': '13 inches', 'Length': '15 inches', 'Camera Vision?': 'Does have camera vision system',
	'Drivetrain Motors': '10 drivetrain motors'},
	'5852': {'Number': '5852', 'Name': 'Illusion Robotics', 'Prog. Language': 'C+', 'Width': '17 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera video system',
	'Drivetrain Motors': '9 drivetrain motors'}}
'''
def list_teams(list_of_teams):
	for team in list_of_teams:
		print(str(team) + "\n")	

def add():
	Player_Add = input("Let's add a team! Choose any team. ")
	if Player_Add.isalpha and Player_Add != None:
		teams[Player_Add] = {}
		# Add Number 
		num_question = input("Insert team Number ")
		# Add name
		name_question = input("Insert its name ")
		# Add Programming Language
		lang_question = input("Insert Programming Language ")
		# Add Width
		wide_question = input("Insert robot width (In inches) ")
		# Add Length
		long_question = input("Insert robot length (In inches) ")
		# Add Cam Vision
		cam_question = input("Insert Yes or No for Camera Vision on Robot ")
		# Add Drivetrain Motor Number
		drive_question = input("Insert Number of Drivetrain Motors on robot ")
		if num_question.isdigit() and wide_question.isdigit() and long_question.isdigit() and drive_question.isdigit() and (cam_question == "Yes" or cam_question == "No"):
			teams[Player_Add]["Number"] = str(num_question)
			teams[Player_Add]["Name"] = name_question
			teams[Player_Add]["Prog. Language"] = lang_question
			teams[Player_Add]["Width"] = str(wide_question)
			teams[Player_Add]["Length"] = str(long_question)
			teams[Player_Add]["Camera Vision?"] = cam_question
			teams[Player_Add]["Number of Drivetrain Motors"] = str(drive_question)
			print(teams)
		else:
			print("Uh oh! One of your inputs was invalid. Make sure that the questions involving numbers are actually numbers, 'kay?")

def remove():
	Player_Delete = input("Let's see. What team do you want to delete? ")
	if Player_Delete.isalpha and Player_Delete != None:
		if Player_Delete in teams:
			teams.pop(Player_Delete)
			print(teams)
		else:
			print("Sorry. That's not in the database. Try again.")

def view():
	view_input = input("Whose data do you want to view?: ")
	team_information_input = input("What datapoint would you like to see?: ")
	if view_input in teams and team_information_input in teams[view_input]:	
		print(teams[view_input][team_information_input])
	else:
		print("Sorry. I don't think your value is in the data files. Make sure your values are strings and try again.")

def modify():
	modifier_team = input("\n Whose team's data would you like to modify?: ")
	modifier_datapoint = input("\nWhat datapoint would you like to modify?: ")
	if modifier_team in teams:
		print("The current value for " + str(modifier_datapoint) + " of team " + str(modifier_team) + " is " + teams[modifier_team][modifier_datapoint])
		modifiee_datapoint = input("\nWhat value would you like to change it to?: ")
		teams[modifier_team][modifier_datapoint] = modifiee_datapoint
		print("The new value has been changed to: " + str(modifiee_datapoint))
	else:
		print("Sorry. I'm afraid your input is not in the database. Try again")

def search():
	search_team = input("Which team do you want to look for? ")
	name_team = input("What is the name of the team, for safety measures? ")
	if search_team in teams and name_team in teams[search_team]['Name']:
		print(str(search_team in teams))
	else:
		print(False)


while True: 
	Player_Use = input("Hello, User. Welcome to the FIRST Robotics Team Menu! What would you like to do? ")
	if Player_Use == 'add' or Player_Use == 'Add':
		add()
	elif Player_Use == 'view' or Player_Use == 'View':
		view()
	elif Player_Use == 'remove' or Player_Use == 'Remove':
		remove()
	elif Player_Use == 'search' or Player_Use == 'Search':
		search()
	elif Player_Use.lower() == "modify":
		modify()
	elif Player_Use.lower() == "view all teams":
		list_teams(teams)
	elif Player_Use == "quit":
		print("Thanks for using this! See ya real soon!")
		break;
	else:
		print("Sorry! I didn't get that! Please try again.")