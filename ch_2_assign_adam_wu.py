
teams = {};
#empty team that will be the value for given team number
team_menu = {
	'1': 'location',
	'2':'program_language',
	'3':'width', 
	'4':'length',
	'5':'camera_vision_system',
	'6':'number_drivetrain_motor',
	'0':'exit program'
	}
#entering team number and updating the teams dict
team_number = int(input('Please enter team number:\n'))
teams.update({team_number:{}})

user_input = '1'
while True: 

	for key in team_menu.keys():
		print(key+': '+team_menu[key])

	#user_input will allow you to exit the program
	user_input = str(input('enter number corresponding to what you would like to add/change \n'))
	key_entered = user_input

	if user_input == '0':
		break

	#val_change is the variable for new values
	val_change = str(input('what is the new value for ' + team_menu[key_entered]+'\n'))
	teams[team_number][team_menu[key_entered]] = user_input



	print(teams)