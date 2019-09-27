team_dictionary = {}
user_input = "yeet"
user_action = input("""What action do you want to take:
	add a team,
	view a team's information,
	remove a team,
	search for a team,
	list all teams,
	or return to main menu? \n""")
if user_action == "add a team":
	while user_input != "nah": 	
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
		user_input = input("Do you want to continue? yeet or nah? \n")
if user_input == "nah":
	user_action = input("""What action do you want to take:
		add a team,
		view a team's information,
		remove a team,
		search for a team,
		list all teams,
		or return to main menu? \n""")
elif user_action == "view a team's information":
	view_team = int(input("What is the number of the team you want to view?"))
	print(team_dictionary[view_team])



