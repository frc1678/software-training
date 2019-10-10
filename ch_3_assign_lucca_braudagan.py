def add_team():
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

def view_or_modify_team(team_view):
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

def remove_team(delete_team):
	if delete_team in teams:
		teams.pop(delete_team, None)
	else:
		print("This is not an existing team number.")

def search_team(search_teams):
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

def list_team():
	for team in teams.keys():
		print(team)
	print("These are the current teams in the dictionary.")

teams = {
	1678 : {
		"team_name" : "Citrus Circuits",
		"location" : "Davis, CA", 
		"rookie_year" : 2005, 
		"competed_in_2019_season" : True, 
		"2019_competition_names_and_locations" : {
			"Central Valley Regional" : "Fresno, CA",
			"Sacramento Regional" : "Davis, CA",
			"Aerospace Valley Regional" : "Lancaster, CA",
			"Carver Division" : "Houston, TX",
			"Einstein Field" : "Houston, TX",
			"RCC Qianjiang International Robotics Invitational" : "Hangzhou, Zhejiang, China",
			"Chezy Champs" : "San Jose, CA"
		},
		"2019_season_awards" : [
			"Regional Chairman's Award At Central Valley Regional",
			"Regional Winners At Central Valley Regional",
			"FIRST Dean's List Finalist Award",
			"Regional Winners At Sacramento Regional",
			"Industrial Design Award Sponsored By General Motors",
			"Regional Winners At Aerospace Valley Regional",
			"Excellence In Engineering Award Sponsered By Delphi",
			"Championship Subdivision Winner In Carver Divison",
			"Entrepreneurship Award Sponsored By Kleiner Perkins Caufield And Byers"]
	},
	4322 : {
		"team_name" : "Clockwork Oranges",
		"location" : "Orange, CA",
		"rookie_year" : 2012,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"San Diego Regional Presented By Qualcomm" : "Del Mar, CA",
			"Las Vegas Regional" : "Las Vegas, NV",
			"Einstein Field" : "Houston, TX",
			"Battleship Blast Monday" : "San Pedro, CA",
			"Beach Blitz" : "Huntington Beach, CA"
		},
		"2019_season_awards" : [
			"FIRST Dean's List Finalist Award",
			"FIRST Dean's List Award"]
	},
	5458 : {
		"team_name" : "Digital Minds",
		"location" : "Woodland, CA",
		"rookie_year" : 2015,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"Central Valley Regional" : "Fresno, CA",
			"Sacramento Regional" : "Davis, CA"
		},
		"2019_season_awards" : "None"
	},
	1 : {
		"team_name" : "The Juggernauts",
		"location" : "Pontiac, MI",
		"rookie_year" : 1997,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"FIM District Center Line Event" : "Center Line, MI",
			"FIM District Troy Event" : "Troy, MI"
		},
		"2019_season_awards":"Imagery Award In Honor Of Jack Kamen"
	},
	7229 : {
		"team_name" : "Electronic Eagles",
		"location" : "Sacramento, CA",
		"rookie_year" : 2018,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"Sacramento Regional" : "Davis, CA"
		}, 
		"2019_season_awards" : "None"
	}
}

while True:
	initial_user_request = input("Choose from: 'add' 'view_or_modify' 'remove' 'search' 'list' ")
	if initial_user_request == "add":
		add_team()
	
	elif initial_user_request == "view_or_modify":
		team_view = int(input("Which team would you like to view? "))
		view_or_modify_team(team_view)

	elif initial_user_request == "remove":
		delete_team = int(input("Which team would you like to remove? "))
		remove_team(delete_team)

	elif initial_user_request == "search":
		search_teams = input("Which team would you like to see? (By name or number) ")
		search_team(search_teams)

	elif initial_user_request == "list":
		list_team()

	else:
		print("That is not a search option.")
