teams = []

Robot_Team_A = {'1678': {'Number': '1678', 'Name': 'Citrus Circuits', 'Prog. Language': 'Java', 'Width': '15 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera vision system',
	'Drivetrain Motors': '12 drivetrain motors'}}
Robot_Team_B = {'744': {'Number': '744', 'Name': 'Shark Attack', 'Prog. Language': 'C++', 'Width': '13 inches', 'Length': '15 inches', 'Camera Vision?': 'Does have camera vision system',
	'Drivetrain Motors': '10 drivetrain motors'}}
Robot_Team_C = {'5852': {'Number': '5852', 'Name': 'Illusion Robotics', 'Prog. Language': 'C+', 'Width': '17 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera video system',
	'Drivetrain Motors': '9 drivetrain motors'}}

Robot_Team_all = {'1678': {'Number': '1678', 'Name': 'Citrus Circuits', 'Prog. Language': 'Java', 'Width': '15 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera vision system',
	'Drivetrain Motors': '12 drivetrain motors'},
	'744': {'Number': '744', 'Name': 'Shark Attack', 'Prog. Language': 'C++', 'Width': '13 inches', 'Length': '15 inches', 'Camera Vision?': 'Does have camera vision system',
	'Drivetrain Motors': '10 drivetrain motors'},
	'5852': {'Number': '5852', 'Name': 'Illusion Robotics', 'Prog. Language': 'C+', 'Width': '17 inches', 'Length': '16 inches', 'Camera Vision?': 'Does not have camera video system',
	'Drivetrain Motors': '9 drivetrain motors'}}

def list_teams(list_of_teams):
	for team in list_of_teams:
		print(str(team) + "\n")	

def add():
	Player_Add = input("Let's add a team! Choose any team.")
	if Player_Add.isalpha and Player_Add != None:
		teams.append(Player_Add)
		print(teams)

def remove():
	Player_Delete = input("Let's see. What team do you want to delete?")
	if Player_Delete.isalpha and Player_Delete != None:
		if Player_Delete in teams:
			teams.remove(Player_Delete)
			print(teams)
		else:
			print("Sorry. That's not in the database. Try again.")

def view():
	view_input = input("Whose data do you want to view?: ")
	team_information_input = input("What datapoint would you like to see?: ")
	if view_input in Robot_Team_all and team_information_input in Robot_Team_all[view_input]:	
		print(Robot_Team_all[view_input][team_information_input])
	else:
		print("Sorry. I don't think your value is in the data files. Make sure your values are strings and try again.")

def modify():
	modifier_team = input("\n Whose team's data would you like to modify?: ")
	modifier_datapoint = input("\nWhat datapoint would you like to modify?: ")
	if modifier_team in Robot_Team_all and modifier_datapoint in Robot_Team_all[modifier_team]:
		print("The current value for " + str(modifier_datapoint) + " of team " + str(modifier_team) + " is " + Robot_Team_all[modifier_team][modifier_datapoint])
		modifiee_datapoint = input("\nWhat value would you like to change it to?: ")
		Robot_Team_all[modifier_team][modifier_datapoint] = modifiee_datapoint
		print("The new value has been changed to: " + str(modifiee_datapoint))
	else:
		print("Sorry. I'm afraid your input is not in the database. Try again")

def search():
	search_team = input("Which team do you want to look for? ")
	name_team = input("What is the name of the team, for safety measures? ")
	if search_team in Robot_Team_all and name_team in Robot_Team_all[search_team]['Name']:
		print(str(search_team in Robot_Team_all))
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