team_dictionary = {}
user_action = int(input("""Enter the number of the action you want to do
	1	add a team
	2	view a team
	3	remove a team
	4	list all teams \n """))
while True:  
	if user_action == 0:
	#returning to main menu
		user_action = int(input("""Enter the number of the action you want to do
			1	add a team
			2	view a team
			3	remove a team
			4	list all teams \n """))
	elif user_action == 1:
	#adding a team	
		number = int(input("What is your team number? \n"))
		name = str(input("What is the name of your team? \n"))
		programming_language = str(input("What is the programming language of your team? \n"))
		width = int(input("What is the width of your robot? \n"))
		length = int(input("What is the length of your robot? \n"))
		camera_vision_system = bool(input("True or False, your robot has a camera vision system? \n"))
		number_of_motors = int(input("How many motors does your robot have? \n"))
		added_team_information = {
			"number": number,
			"name": name,
			"programming_language": programming_language,
			"width": width,
			"length": length, 
			"camera_vision_system": camera_vision_system, 
			"number_of_motors": number_of_motors}
		team_dictionary.update({number:added_team_information})
		print(team_dictionary) 
		user_action = int(input("""If you want to continue, press 1. \nIf you want to exit the "add" function, press 0. \n """))
	elif user_action == 2:
	#viewing a team
		view_team = int(input("What is the number of the team you want to view? \n "))
		if view_team in team_dictionary == True:
			print(team_dictionary[view_team])
		if view_team in team_dictionary == False:
				print("I'm sorry, the team you are looking for does not exist.")
				view_team = int(input("What is the number of the team you want to view? \n ")) 
		user_action = int(input("""If you want to continue, press 2. \nIf you want to exit the "view" function, press 0. \n """))
	elif user_action == 3:
	#removing a team
		print(team_dictionary)
		remove_team = int(input("What is the number of the team you want to remove? \n "))
		if remove_team in team_dictionary == True:
			team_dictionary.pop(remove_team)
			print("Team" +remove_team+ "has been removed from the team dictionary!")
		if remove_team in team_dictionary == False:
				print("I'm sorry, the team you are looking for does not exist.")
				remove_team = int(input("What is the number of the team you want to view? \n ")) 
		user_action = int(input("""If you want to continue, press 3. \nIf you want to exit the "remove" function, press 0. \n """))
	elif user_action == 4:
	#listing all teams
		print(team_dictionary)
		user_action = int(input("""If you want to continue, press 4. \nIf you want to exit the "list" function, press 0. \n """))
	elif user_action not in [0, 1, 2, 3, 4]:
	#returning to main menu if user_action is not a known value
		print("I'm sorry, could you please re-enter your command?")
		user_action = int(input("""Enter the number of the action you want to do
			1	add a team
			2	view a team
			3	remove a team
			4	search a team
			5	list all teams \n"""))