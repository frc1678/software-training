def int_check(user_input):
	while True:
		if user_input.isdigit():
			return(int(user_input))
		else:
			user_input = input("This is not a numeral value for your input. Try again. ")

def bool_check(user_input):
	while True:
		if user_input.upper() == "TRUE":
			return(True)
		elif user_input.upper() == "FALSE":
			return(False)
		else:
			user_input = input("This is not a boolean value for your input. Try again. (Input 'True' or 'False') ")

teams = {}

while True:
	initial_user_request = input("Choose from: 'add' 'view_or_modify' 'remove' 'search' 'list' ")
	if initial_user_request == "add":
		temp_team_dictionary = {}

		team_number = input("What is your team's team number? ")
		team_number = int_check(team_number)

		temp_team_dictionary["team_name"] = input("What is your team's name? ")
		temp_team_dictionary["robot_name"] = input("What is your robot's name? ")
		temp_team_dictionary["robot_p_language"] = input("What is your robot's programming language? ")
		robot_width = input("What is your robot's width? ")
		temp_team_dictionary["robot_width"] = int_check(robot_width)
		robot_height = input("What is your robot's height? ")
		temp_team_dictionary["robot_height"] = int_check(robot_height)
		robot_camera = input("Does your robot have a camera vision system? (Input 'True' or 'False') ")
		temp_team_dictionary["robot_camera"] = bool_check(robot_camera)
		robot_drivetrain = input("How many drivetrain motors does your robot have? ")
		temp_team_dictionary["robot_drivetrain"] = int_check(robot_drivetrain)
	
		teams[team_number] = temp_team_dictionary
	
	elif initial_user_request == "view_or_modify":
		team_view_uncheck = input("Which team would you like to view? ")
		team_view = int_check(team_view_uncheck)
		
		if team_view in teams:
			information_category = input("What category would you like to view or modify? ")
			integer_inputs = ["robot_width", "robot_height", "robot_drivetrain"]
			if information_category in teams[team_view]:
				if information_category in integer_inputs:
					print(teams[team_view][information_category])
					new_info_uncheck = input("What would you like to change this value to? ")
					new_info = int_check(new_info_uncheck)
					teams[team_view][information_category] = new_info
				elif information_category == "robot_camera":
					print(teams[team_view][information_category])
					new_info_uncheck = input("What would you like to change this value to? ")
					new_info = bool_check(new_info_uncheck)
					teams[team_view][information_category] = new_info
				else:
					print(teams[team_view][information_category])
					new_info = input("What would you like to change this value to? ")
					teams[team_view][information_category] = new_info
			else:
				print("This is not an information category.")
		else:
			print("This is not an existing team number.")

	elif initial_user_request == "remove":
		delete_team_uncheck = input("Which team would you like to remove? ")
		delete_team = int_check(delete_team_uncheck)

		if delete_team in teams:
			teams.pop(delete_team, None)
		else:
			print("This is not an existing team number.")

	elif initial_user_request == "search":
		search_teams = input("Which team would you like to see? (By name or number) ")
		if teams == {}:
			print("There are no teams in the dictionary.")
		else:
			for team, category in teams.items():
				found_team = False
				if search_teams == category["team_name"]:
					print("This is an existing team in the dictionary.")
					found_team = True
					break
				elif search_teams[0].isdigit() and int(search_teams) == team:
					print("This is an existing team in the dictionary.")
					found_team = True
					break
			if found_team != True:
				print("This is not an existing team.")

	elif initial_user_request == "list":
		for team in teams.keys():
			print(team)
		print("These are the current teams in the dictionary.")

	else:
		print("That is not a search option.")

