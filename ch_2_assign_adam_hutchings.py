master_dictionary = {} #Setting up the master el dictionario
input_list = ['menu', 'view', 'remove', 'search', 'modify']
statistic_list = ['tm', 'n', 'pl', 'w', 'l', 'cv', 'dt']
#Translating user inputs into functions

def remove_function():
	while True: #Idiotproofing code
		removal = input("Which team would you like to remove? This action cannot be undone!")
		if ("statistics" + removal) in master_dictionary:
			master_dictionary[removal] = {}
			break
	valid_input_5 = False
	while valid_input_5 == False:
		menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
			'remove' to remove more, 'search' to search the teams, or 'modify' to modify the information.""")
		if menu_selection in input_list:
			if menu_selection == 'menu':
				valid_input_5 = True
				menu_function()
			if menu_selection == 'view':
				valid_input_5 = True
				view_function()
			if menu_selection == 'remove':
				valid_input_5 = True
				remove_function()
			if menu_selection == 'search':
				valid_input_5 = True
				search_teams()
			if menu_selection == 'modify':
				valid_input_5 = True
				modification_function()

def view_function():
	valid_input_6 = False #This, and all other such "shells", is safeproofing so the code doesn't die if the user enters an invalid input.
	while valid_input_6 == False:
		viewing_selection = input("Which team's statistics would you like to view? ")
		if "statistics" + str(viewing_selection) in master_dictionary:
			valid_input_6 = True
	valid_input_7 = False
	while valid_input_7 == False:
		statistic_selection = input("""Which statistic would you like to view? Please type one of
		tm (team number), n (name), pl (programming language), w or l (width or a length for your robot), 
		cv (whether or not your robot has a camera vision system),or dt (the number of drivetrain motors on your robot). """)
		if statistic_selection in statistic_list and master_dictionary["statistics" + viewing_selection][statistic_selection] != '':
			print (master_dictionary["statistics" + viewing_selection][statistic_selection])
			valid_input_7 = True
		elif master_dictionary["statistics" + viewing_selection][statistic_selection] == '':
			print("That hasn't been added yet. Try something else.")
			valid_input_7 = True
	else:
		valid_input_5 = False
		while valid_input_5 == False:
			menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
			'remove' to remove data, 'search' to search the teams, or 'modify' to modify the information.""")
			if menu_selection == 'menu':
				valid_input_5 = True
				menu_function()
			if menu_selection == 'view':
				valid_input_5 = True
				view_function()
			if menu_selection == 'remove':
				valid_input_5 = True
				remove_function()
			if menu_selection == 'search':
				valid_input_5 = True
				search_teams()
			if menu_selection == 'modify':
				valid_input_5 = True
				modification_function()

def search_teams(): #Searching teams
	valid_input_4 = False
	while valid_input_4 == False:
		team_search = input("What team would you like to search for?")
		if team_search.isdigit() == True: #If the search is all digits
			valid_input_4 = True
		for search in master_dictionary: #Checking every master_dict key to see if it's equal to the search
			if search == ("statistics" + team_search):
				print("A match has been found!")
				valid_input_5 = False
				while valid_input_5 == False:
					menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
						'remove' to remove data, 'search' to search the teams again, or 'modify' to modify the information.""")
					if menu_selection in input_list:
						if menu_selection == 'menu':
							valid_input_5 = True
							menu_function()
						if menu_selection == 'view':
							valid_input_5 = True
							view_function()
						if menu_selection == 'remove':
							valid_input_5 = True
							remove_function()
						if menu_selection == 'search':
							valid_input_5 = True
							search_teams()
						if menu_selection == 'modify':
							valid_input_5 = True
							modification_function()
	else:
		print("A match has not been found.")
		valid_input_5 = False
		while valid_input_5 == False:
			menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
				'remove' to remove data, 'search' to search the teams again, or 'modify' to modify the information.""")
			if menu_selection in input_list:
				if menu_selection == 'menu':
					valid_input_5 = True
					menu_function()
				if menu_selection == 'view':
					valid_input_5 = True
					view_function()
				if menu_selection == 'remove':
					valid_input_5 = True
					remove_function()
				if menu_selection == 'search':
					valid_input_5 = True
					search_teams()
				if menu_selection == 'modify':
					valid_input_5 = True
					modification_function()

def add_team(): #How to add a new team
			print("You are adding a new file. The first step is to name your team.")
			valid_team_name = False
			while valid_team_name == False:
				team_name = input("What would you like your team to be named? Make sure it's all numbers! ") #Getting a name for the team
				if team_name.isdigit() == True: #Checking if a team name is all digits
					valid_team_name = True #Breaking the infinite loop
					master_dictionary["statistics" + str(team_name)] = {} #Making a dictionary entry for the team
					for yeet in statistic_list:
						master_dictionary["statistics" + str(team_name)][yeet] = ''
			valid_input_5 = False
			while valid_input_5 == False:
				menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
					'remove' to remove data, 'search' to search the teams, or 'modify' to modify the information again.""")
				if menu_selection in input_list:
					if menu_selection == 'menu':
						valid_input_5 = True
						menu_function()
					if menu_selection == 'view':
						valid_input_5 = True
						view_function()
					if menu_selection == 'remove':
						valid_input_5 = True
						remove_function()
					if menu_selection == 'search':
						valid_input_5 = True
						search_teams()
					if menu_selection == 'modify':
						valid_input_5 = True
						modification_function()

def add_statistic(): #How to add a statistic for a team
	team_name = '' #Setting variables empty
	datapoint = ''
	team_name_validity = False
	while team_name_validity == False:
		team_name = input("Please select a team whose information you would like to modify.") #Finding the team
		if ("statistics" + str(team_name)) in master_dictionary:
			team_name_validity = True
	statistic_validity = False
	while statistic_validity == False:
		statistic_added = input("""You may add a team number (tm), a name (n), a programming language (pl),
		a width or a length for your robot (w or l), whether or not your robot has a camera vision system (cv),
		and the number of drivetrain motors on your robot (dt). Which one of these options would you like
		to edit? Enter your options as the parenthetical after the option you have selected. """) #Note the shorthands like 'pl' here.
		if  statistic_added in statistic_list:
			statistic_validity = True
	for statistic_name in statistic_list: #For all possible statistic names
		if statistic_added == statistic_name: #If the statistic selected has been found:
			datapoint = (input("What would you like to set this team's " + statistic_added + "?")) #What data the user wants to add.
			master_dictionary["statistics" + str(team_name)][statistic_added] = datapoint
	valid_input_5 = False
	while valid_input_5 == False:
		menu_selection = input("""Type 'menu' to go back to the main menu, 'view' to view more, 
			'remove' to remove data, 'search' to search the teams, or 'modify' to modify the information again.""")
		if menu_selection in input_list:
			if menu_selection == 'menu':
				valid_input_5 = True
				menu_function()
			if menu_selection == 'view':
				valid_input_5 = True
				view_function()
			if menu_selection == 'remove':
				valid_input_5 = True
				remove_function()
			if menu_selection == 'search':
				valid_input_5 = True
				search_teams()
			if menu_selection == 'modify':
				valid_input_5 = True
				modification_function()

def modification_function(): #Modifying data in this program.
		valid_input_3 = False
		while valid_input_3 == False:
			adding_teams = input("Would you like to add a new team or a new statistic? Please type 'team' or 'statistic'. ") #Whether new team files are still being created
			if adding_teams == 'team': #Getting other functions to run
				add_team()
				valid_input_3 = True
			if adding_teams == 'statistic' and master_dictionary != {}: #Checking if there are any teams for statistics to be added to
				add_statistic()
				valid_input_3 = True

def menu_function():
	if master_dictionary == {}:
		valid_input = False
		while valid_input == False:
			first_input = input("You don't seem to have any data. Enter 'yes' to add some. ")
			if first_input == 'yes':
				modification_function()
				valid_input = True
	else: #If information has already been saved.
		valid_input_5 = False
		while valid_input_5 == False:
			menu_selection = input("""Type 'view' to view more, 
				'remove' to remove, 'search' to search the teams, or 'modify' to modify the information.""")
			if menu_selection == 'view':
				valid_input_5 = True
				view_function()
			if menu_selection == 'remove':
				valid_input_5 = True
				remove_function()
			if menu_selection == 'search':
				valid_input_5 = True
				search_teams()
			if menu_selection == 'modify':
				valid_input_5 = True
				modification_function()

menu_function()