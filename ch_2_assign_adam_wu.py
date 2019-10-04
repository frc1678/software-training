teams = {};
user_menu = {
	1: 'add/change_team_info', 
	2: 'Remove_team', 
	3: 'search_team', 
	4: 'show_all_teams', 
	0: 'quit'}
team_menu = {
	1: {'property': 'team_name','type':'str'},
	2: {'property': 'location','type':'str'},
	3: {'property': 'program_language', 'type':'str'},
	4: {'property': 'camera_vision_system','type':'bool'},
	5: {'property': 'width','type':'int'}, 
	6: {'property': 'length','type':'int'},
	7: {'property': 'number_drivetrain_motor','type':'int'},
	0: {'property': 'main_menu'}}

user_menu_selection = ''
while user_menu_selection != 0: 

	for key in user_menu.keys():
		print(str(key) + ': ' +user_menu[key])
			
	user_menu_selection = str(input('please enter number of selection you would like to make \n'))
		
	if user_menu_selection == '0':
		break
	if user_menu_selection == '1':
		team_number = int(input('Please enter team number:\n'))
		teams.update({team_number:{}})

		user_input = '1'
		while True: 

			for key in team_menu.keys():
				print(str(key) +': '+team_menu[key]['property'])

				#user_input will allow you to exit the program
			user_input = int(input('enter number corresponding to what you would like to add/change \n'))
			key_entered = user_input

			if user_input == 0:
				break

			want_to_change = team_menu[key_entered]

				#val_change is the variable for new values
			val_change = input('what is the new value for ' + want_to_change['property']+'\n')
			try:
				if want_to_change['type'] == 'str':
					try:
						if val_change.isnumeric():
							print('please enter a number')
					except:
						print("Oops! please make sure you enter a " + want_to_change['type'])
						print("Next entry.")

				elif want_to_change['type'] == 'int':
					val_change = int(val_change)
				elif want_to_change['type'] == 'bool':
					val_change = int(val_change)
					val_change = val_change == 1
				teams[team_number][want_to_change['property']] = val_change

			except:
				print("Oops! please make sure you enter a " + want_to_change['type'])
				print("Next entry.")
				
			print(teams)

	if user_menu_selection == '2':	
		team_name = input('delete which team? \n')
		if team_name.isnumeric():
			team_name = int(team_name)
			if team_name in teams.keys():
				print(teams.keys())
				teams.pop(team_name)
				print(teams.keys())
			else:
				print('team ' + team_name +' does not exist')
		else:
			print('please enter an integer \n')

	if user_menu_selection == '3':
		team_search = str(input('what team would you like to search? \n'))
		for team_number, team_name in teams.items():
			if team_search.isnumeric():
				if int(team_search) == team_number:
					print(teams[team_number])
			elif team_search == team_name['team_name']:
				print(teams[team_number])
			else:
				print('not ok')	
	if user_menu_selection == '4':
		for key, value in teams.items():
			print (key)
			for subkey, subvalue in value.items():
				print('  '+ subkey + ' = ' + subvalue)



		"""if team_search in teams.keys():
			print("Present, ") 
			print("value =", teams[key]) 
		else: 
			print("Not present") """

		
	#entering team number and updating the teams dict

		   


		"""elif want_to_change['type'] == 'int':
			val_change = input('what is the new integer value for ' + want_to_change['property'] + '\n')
		elif want_to_change['type'] == 'bool':
			val_change = input('''please enter 'true' or 'false' ''' + want_to_change['property'] + '\n')"""

		"""if want_to_change['type'] == 'bool':
			val_change = input('''type "true" or "false" if they have a ''' + want_to_change['property']+'\n')
			val_change = bool(val_change)
		
		if want_to_change['type'] == 'int':
			val_change = input('please enter new number value of ' + want_to_change['property']+'\n')
			val_change = int(val_change)"""

		
