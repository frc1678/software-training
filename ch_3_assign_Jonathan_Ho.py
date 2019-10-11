Team_DataA = []

Team_DataB = {'1678': {'Name': 'Citrus Circuits', 'Location': 'Davis, CA, USA', 'Rookie': '2005', 
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
	for Team_DataA in list_of_teams:
		print(str(Team_DataA) + "\n")

def add_team():
	Player_Add = input("Alright, let's add a some teams to our database! Choose a team or piece of info to place in the database. ")
	if Player_Add.isalpha and Player_Add != None:
		Team_DataA.append(Player_Add)

def delete_team():
	Player_Delete = input("As you wish it. Which team would you like to remove from the database? ")
	if Player_Delete.isalpha and Player_Delete != None:
		Team_DataA.remove(Player_Delete)

def view_info():
	#view_list = input("Sure! What list would you like to see?")
	view_team = input("Now, which team would you like to view? ")
	view_data = input("What would you like to know about it? ")
	print(str(Team_DataB[view_team][view_data]))

def modify_info():
	#change_list = input("\n Which list do you need to find your team?")
	change_team = input("\n What team's data would you like to modify? ")
	change_data = input("\n What datapoint would you like to change? ")
	print("This team's current value for " + change_data + " is " + Team_DataB[change_team][change_data])
	change_datapoint = input("\n So what do you want to change about " + change_data + "? ")
	Team_DataB[change_team][change_data] = change_datapoint
	print("Drumroll! The team's new value has been modified to... " + str(change_datapoint) + "!")

def search():
	team_search = input("What team would ya like to look for? ")
	print("Let's see... is " + str(team_search) + " anywhere in our database? " + str(team_search in Team_DataA and team_search in Team_DataB))

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
		list_teams_all(Team_DataA)
	elif Player_Control == 'quit':
		print("Gotcha! See ya around!")
		break;
	else:
		print("Sorry! Did you say something else? I don't have that in my files. Please try again! :)")
