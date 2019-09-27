teams = {}

initial_user_request = input("choose_from:_'add',_'view_or_modify',_'remove',_'search',_'list',_'return'")
if initial_user_request == "add":
	temp_team_dictionary = {}

	teams["team_number"] = int(input("What is your team's team number?"))
	
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
	if team_view in teams
	information_category = input()
elif initial_user_request == "remove":
	print("Nothing"),
elif initial_user_request == "search":
	print("Nothing"),
elif initial_user_request == "list":
	print("Nothing"),
elif initial_user_request == "return":
	print("Nothing"),
else:
	print("Nothing"),


#add_team() citrus circuits, c++, 1678

#{1678 : {"name" : "citrus circuits", "p_l" : "c++"}}
 


