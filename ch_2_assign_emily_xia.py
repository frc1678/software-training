team_dictionary = {}
user_action = input("""Enter the number of the action you want to do
	1	add a team
	2	view a team
	3	remove a team
	4	search a team
	5	list all teams 
	6	leave \n """)
while True:  
	if user_action == "0":
	#returning to main menu
		user_action = input("""Enter the number of the action you want to do
			1	add a team
			2	view a team
			3	remove a team
			4	search a team
			5	list all teams
			6	leave \n """)
	elif user_action == "1":
	#adding a team	
		number = input("What is your team number? \n")
		name = input("What is the name of your team? \n")
		programming_language = input("What is the programming language of your team? \n")
		width = input("What is the width of your robot? \n")
		length = input("What is the length of your robot? \n")
		camera_vision_system = input("True or False, your robot has a camera vision system? \n")
		number_of_motors = input("How many motors does your robot have? \n")
		added_team_information = {
			"number": number,
			"name": name,
			"programming_language": programming_language,
			"width": width,
			"length": length, 
			"camera_vision_system": camera_vision_system, 
			"number_of_motors": number_of_motors}
		team_dictionary.update({number:added_team_information})
		user_action = input("""If you want to continue, press 1. \nIf you want to exit the "add" function, press 0. \n """)
	elif user_action == "2":
	#viewing a team
		view_team = int(input("What is the number of the team you want to view? \n "))
		if view_team in team_dictionary:
			print(team_dictionary[view_team])
		elif view_team not in team_dictionary:
				print("I'm sorry, the team you are looking for does not exist.")
		user_action = input("""If you want to continue, press 2. \nIf you want to exit the "view" function, press 0. \n """)
	elif user_action == "3":
	#removing a team
		print(team_dictionary)
		remove_team = int(input("What is the number of the team you want to remove? \n "))
		if remove_team in team_dictionary:
			team_dictionary.pop(remove_team)
			print("Team" +remove_team+ "has been removed from the team dictionary!")
		elif remove_team not in team_dictionary:
				print("I'm sorry, the team you are looking for does not exist.")
		user_action = input("""If you want to continue, press 3. \nIf you want to exit the "remove" function, press 0. \n """)
	elif user_action == "4":
	#searching for a team
		search_team = input("What is the number of the team you want to search for? \n")
		if search_team in team_dictionary:
			print("Yes, the team you are looking for is in the team dictionary")
		else:
			result=None
			for key in team_dictionary:
				if team_dictionary[key]["name"] == search_team:
					print("Yes, the team you are looking for is in the team dictionary")
					result=team_dictionary[key]
					break  
			if not result:
				print("""I'm sorry, but the team you are looking for is not in the team dictionary.
				Please make sure that your input is an integer.""")
		user_action = input("""If you want to continue, press 4. \n If you want to exit the "search" function, press 0. \n """)
	elif user_action == "5":
	#listing all teams
		print(team_dictionary)
		user_action = input("""If you want to continue, press 5. \nIf you want to exit the "list" function, press 0. \n """)
	elif user_action not in ["0", "1", "2", "3", "4", "5", "6"]:
	#returning to main menu if user_action is not a known value
		print("I'm sorry, could you please re-enter your command?")
		user_action = input("""Enter the number of the action you want to do
			1	add a team
			2	view a team
			3	remove a team
			4	search a team
			5	list all teams
			6	leave \n""")
	elif user_action == "6":
		break
