Team_Data = {'1678': {'Name': 'Citrus Circuits', 'Location': 'Davis, CA, USA', 'Rookie': '2005', 
	'Competition Names': [
		'Central Valley Regional',
		'Sacramento Regional',
		'Aerospace Valley Regional', 
		'Carver Division', 
		'Einstein Field', 
		'RCC Qianjiang International Robotics Invitational'
	], 
 
	'Competition Location': [
		'Fresno, CA, USA', 
		'Davis, CA, USA', 
		'Lancaster, CA, USA', 
		'Houston, TX, USA', 
		'Houston TX, USA', 
		'Hangzhou, Zhejiang, China'
	],
	'Awards': [
		'Regional Chairman`s Award and Regional Winners', 
		'FIRST Dean`s List Finalist Award (Katie Stachowicz), Regional Winners, and Industrial Design Award sponsored by General Motors',
		'Regional Winners and Excellence in Engineering Award sponsored by Delphi', 'Championship Subdivision Winner and Entrepreneurship Award sponsored by Kleiner Perkins Caufield and Byers'
	,]}, 

	'41': {'Name': 'RoboWarriors', 'Location': 'Warren, NJ, USA', 'Rookie': '1997', 
	'Competition Names': [
		'FMA District Mount Olive Event',
		'FMA District Montgomery Event',
		'FIRST Mid-Atlantic District Championship'
	],
	'Competition Location': [
		'Flanders, NJ, USA',
		'Skillman, NJ, USA',
		'Bethlehem, PA, USA'
	],
	'Awards': 'Innovation in Control Award sponsored by Rockwell Automation',
	},

	'7823': {'Name': 'Double Negative', 'Location': 'Rogers City, MI, USA', 'Rookie': '1997', 
	'Competition Names': [
		'FIM District Alpena Event #1',
		'FIM District Alpena Event #2',
		'Michigan State Championship - Ford Division', 
	],
	'Competition Location': [
		'Alpena, MI, USA',
		'Alpena, MI, USA',
		'University Center, MI, USA'
	],
	'Awards': [
		'Highest Rookie Seed and Rookie Inspiration Award sponsored by National Instruments',
		'Rookie All Star Award and District Event Finalist',
		'Judges` Award'
	],}
	}



def list_teams_all(list_of_teams):
	for Team_Data in list_of_teams:
		print(str(Team_Data) + "\n")

def add_team():
	Player_Add = input("Alright, let's add a some teams to our database! Choose a team or piece of info to place in the database. ")
	if Player_Add.isdigit and Player_Add != None:
		Team_Data[Player_Add] = {}

def delete_team():
	Player_Delete = input("As you wish it. Which team would you like to remove from the database? ")
	if Player_Delete.isdigit and Player_Delete != None:
		Team_Data.pop(Player_Delete)

def view_info():
	print("Just a head's up. Everything in the database for each team shown here is capitalized, so make sure the letter is uppercase for the second question. :P")
	view_team = input("Now, which team would you like to view? ")
	view_data = input("What would you like to know about it? ")
	if view_team in Team_Data and view_data in Team_Data[view_team]:
		print(Team_Data[view_team][view_data])
	else:
		print("Sorry. This isn't in the data files. Try again.")


def modify_info():
	print("Just a head's up. Everything in the database for each team shown here is capitalized, so make sure the letter is uppercase for the second question. :P")
	change_team = input("What team's data would you like to modify? ")
	change_data = input("What datapoint would you like to change? ")
	if change_team in Team_Data and change_data in Team_Data[change_team]:
		print("This team's current value for " + change_data + " is " + Team_Data[change_team][change_data])
		change_datapoint = input("\n So what do you want to change about " + change_data + "? ")
		Team_Data[change_team][change_data] = change_datapoint
		print("Drumroll! The team's new value has been modified to... " + str(change_datapoint) + "!")
	else:
		print("Sorry. What you want to modify is not in our files. Try again.")

def search():
	team_search = input("What team would ya like to look for? ")
	print("Let's see... is " + str(team_search) + " anywhere in our database? " + str(team_search in Team_Data))

while True:
	Player_Control = input('''Good morning, afternoon, and evening to all! Welcome to our FIRST Robotics Menu! What would you like to do here? Type in 'add' to add a team to the database, 'remove' to remove it
		'view' to check a team's data, 'modify' to change the data of the team, 'search' to ensure the teams you added to the database are in there, and 'see all teams' to look at the data in 
		the database. To leave, just type 'quit'.
		''')
	if Player_Control == 'add' or Player_Control == 'Add':
		add_team()
	elif Player_Control == 'remove' or Player_Control == 'delete':
		delete_team()
	elif Player_Control == 'view' or Player_Control == 'View':
		view_info()
	elif Player_Control == 'modify' or Player_Control == 'change':
		modify_info()
	elif Player_Control == 'search' or Player_Control == 'Search':
		search()
	elif Player_Control == 'see all teams':
		list_teams_all(Team_Data)
	elif Player_Control == 'quit':
		print("Gotcha! See ya around!")
		break;
	else:
		print("Sorry! Did you say something else? Your reply is not valid. Please try again! :)")
