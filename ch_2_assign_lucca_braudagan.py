teams = {}

while True:
	initial_user_request = input("Choose from: 'add' 'view_or_modify' 'remove' 'search' 'list' ")
	if initial_user_request == "add":
		temp_team_dictionary = {}

		team_number= int(input("What is your team's team number? "))
	
		temp_team_dictionary["team_name"] = input("What is your team's name? ")
		temp_team_dictionary["robot_name"] = input("What is your robot's name? ")
		temp_team_dictionary["robot_p_language"] = input("What is your robot's programming language? ")
		temp_team_dictionary["robot_width"] = input("What is your robot's width? ")
		temp_team_dictionary["robot_height"] = input("What is your robot's height? ")
		temp_team_dictionary["robot_camera"] = input("Does your robot have a camera vision system? ")
		temp_team_dictionary["robot_drivetrain"] = int(input("How many drivetrain motors does your robot have? "))
	
		teams[team_number] = temp_team_dictionary
	
	elif initial_user_request == "view_or_modify":
		team_view = int(input("Which team would you like to view? "))
		if team_view in teams:
			information_category = input("What category would you like to view or modify? ")
			if information_category in teams[team_view]:
				print(teams[team_view][information_category])
				new_info = input("What would you like to change this value to? ")
				teams[team_view][information_category] = new_info
			else:
				print("This is not an information category.")
		else:
			print("This is not an existing team number.")

	elif initial_user_request == "remove":
		delete_team = int(input("Which team would you like to remove? "))
		if delete_team in teams:
			teams.pop(delete_team, None)
		else:
			print("This is not an existing team number.")

	elif initial_user_request == "search":
		search_teams = input("Which team would you like to see? (By name or number) ")
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

