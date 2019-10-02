teams = {}

initial_user_request = input("Choose from: 'add' 'view_or_modify' 'remove' 'search' 'list'")
if initial_user_request == "add":
	temp_team_dictionary = {}

	team_number= int(input("What is your team's team number?"))
	
	temp_team_dictionary["team_name"] = input("What is your team's name?")
	temp_team_dictionary["robot_name"] = input("What is your robot's name?")
	temp_team_dictionary["robot_p_language"] = input("What is your robot's programming language?")
	temp_team_dictionary["robot_width"] = input("What is your robot's width?")
	temp_team_dictionary["robot_height"] = input("What is your robot's height?")
	temp_team_dictionary["robot_camera"] = input("Does your robot have a camera vision system?")
	temp_team_dictionary["robot_drivetrain"] = int(input("How many drivetrain motors does your robot have?"))
	
	teams[team_number] = temp_team_dictionary
	
	
elif initial_user_request == "view_or_modify":
	print(teams)
	team_view = int(input("Which team would you like to see from these options?"))
	if team_view in teams:
		information_category = input("What category would you like to view or modify?")
		if information_category in team_view:
			new_info = input("What would you like to change this value to?")
			str.replace(information_category, new_info)
# I don't think the above line is right, I don't know what to do here
# I need to have the person change the existing data
	else:
		print("This is not an existing team number.")
elif initial_user_request == "remove":
	print(teams)
	delete_team = int(input("Which team would you like to remove from these options?"))
	if delete_team in teams:
		print("?")
# I don't know what to do here
# I need to have the team dictionary they specify be removed
elif initial_user_request == "search":
	print(teams)
	search_teams = input("Which team would you like to see from these options?")
	if search_teams in teams:
		print(search_teams)
# I don't know what to do here
# Are they supposed to be able to go into a team here? Isn't that view_or_modify?
	else:
		print("That is not an existing team number.")
elif initial_user_request == "list":
	print(teams)
	print("These are the current teams in the dictionary.")
else:
	print("That is not a search option.")

# How do I make it return to initial_user_request?
# How can I return to main menu from an if, elif, or else?
# How do I make it so I could perform a second action and actually have something in teams{}, i.e. not restart the whole code to do something else?