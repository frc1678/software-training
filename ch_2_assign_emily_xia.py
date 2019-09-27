team_dictionary = {}
user_input_add = "yeet"
user_input_view = "yeet"
user_input_remove = "yeet"
user_input_list = "yeet"
user_action = input("""What action do you want to take:
	add a team,
	view a team's information,
	remove a team,
	search for a team,
	list all teams? \n""")
if user_action == "add a team":
	while user_input_add != "nah": 	
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
		user_input_add = input("Do you want to continue? yeet or nah? \n")
	if user_input_add == "nah":
		user_action = input("""What action do you want to take:
			add a team,
			view a team's information,
			remove a team,
			list all teams? \n""")
if user_action == "view a team's information":
	while user_input_view != "nah":
		view_team = int(input("What is the number of the team you want to view?"))
		print(team_dictionary[view_team])
		user_input_view = input("Do you want to coninue? yeet or nah? \n")
	if user_input_view == "nah":
		user_action = input("""What action do you want to take:
			add a team,
			view a team's information,
			remove a team,
			list all teams? \n""")
if user_action == "remove a team":
	while user_input_remove != "nah":
		print(team_dictionary)
		remove_team = int(input("What team do you want to remove? \n "))
		team_dictionary.pop(remove_team)
		print(team_dictionary)
		user_input_remove = input("Do you want to continue? yeet or nah? \n")
	if user_input_remove == "nah":
		user_action = input("""What action do you want to take:
			add a team,
			view a team's information,
			remove a team,
			list all teams? \n""")
if user_action == "list all teams":
	while user_input_list != "nah":
		print(team_dictionary)
		user_input_list = input("Do you want to continue? yeet or nah? \n")
	if user_input_list == "nah":
		user_action = input("""What action do you want to take:
			add a team,
			view a team's information,
			remove a team,
			list all teams? \n""")
