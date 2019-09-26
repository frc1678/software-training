teams = {}

def add_team():
	temp_team_dictionary = {}

	team_number = input("What is your team's team number?")
	team_name = input("What is your team's name?")
	robot_name = input("What is your robot's name?")
	robot_p_language = input("What is your robot's programming language?")
	robot_width = input("What is your robot's width?")
	robot_height = input("What is your robot's height?")
	robot_camera = input("Does your robot have a camera vision system?")
	robot_drivetrain = input("How many drivetrain motors does your robot have?")
	
	temp_team_dictionary["team_name"] = team_name
	temp_team_dictionary["robot_name"] = robot_name
	temp_team_dictionary["robot_p_language"] = robot_p_language
	temp_team_dictionary["robot_width"] = robot_width
	temp_team_dictionary["robot_height"] = robot_height
	temp_team_dictionary["robot_camera"] = robot_camera
	temp_team_dictionary["robot_drivetrain"] = robot_drivetrain
	
	teams[team_number] = temp_team_dictionary

initial_user_request = input("choose_from:_'add',_'view',_'modify',_'remove',_'search',_'list',_'return'")
if initial_user_request == "add":
    add_team();
elif initial_user_request == "view":
	print("Nothing"),
elif initial_user_request == "modify":
	print("Nothing"),
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
 


