all_team_dict = {}
team_dict = {}
def add_team():
	while True: 
		input_num = input("Please enter a team number to add/update or 0 to exit.\n(If the team already exists, the information will be updated.)\n==>")
		if input_num == '0':
			print("Exiting...")
			return 
		elif (input_num.isdigit()):
			team_dict["number"] = input_num
			break
		else: 
			print("Invalid input.")

	while True:
		input_name = input("Please enter the team name.\n==>")
		if (input_name.isdigit()):
			print("Invalid input.")
		else:
			team_dict["name"] = input_name
			break

	while True:
		input_location = input("Please enter the location of the team.\n==>")
		if (input_location.isdigit()):
			print("Invalid input.")
		else:
			team_dict["location"] = input_location
			break

	while True:
		input_rookie_year = input("Please enter the rookie year of the team.\n==>")
		if (input_rookie_year.isdigit()):
			team_dict["rookie year"] = input_rookie_year
			break
		else:
			print("Invalid input.")

	while True:
		input_2019_season = input("Did this team compete in the 2019 season? Please answer 'true' or 'false'.\n==>")
		if input_2019_season == 'true':
			input_2019_season = input("Which 2019 competitions did this team compete in? \n==>")
			team_dict["2019 competitions"] = input_2019_season
			break
		elif input_2019_season == 'false':
			team_dict["2019 competitions"] = input_2019_season
			break
		else: 
			print("Invalid input.")

	while True: 
		input_2019_awards = input("Did this team win any awards in the 2019 season? Please answer 'true or 'false' \n==>")
		if input_2019_awards == 'true':
			input_awards_won = input("Which awards did this team win? \n==>")
			team_dict["2019 awards"] = input_awards_won
			break
		elif input_2019_awards == 'false':
			team_dict["2019 awards"] = input_2019_awards
			break
		else: 
			print("Invalid input.")
	
	all_team_dict.update( {input_num : team_dict} )
	print("Successfully added team " + input_num + "!") 

def view_team():
	input_viewteam = input("Please enter a team number to view or 0 to exit.\n==>")
	if input_viewteam == '0': 
		print("Exiting...")
		return 
	elif input_viewteam in all_team_dict.keys():
		team_dict = all_team_dict.get(input_viewteam)
		print("     Number = " + team_dict["number"] + '\n' +
			  "     Name = " + team_dict["name"] + '\n' +
			  "     Location = " + team_dict["location"] + '\n' + 
			  "     Rookie Year = " + team_dict["rookie year"] + '\n' + 
			  "     2019 competitions = " + team_dict["2019 competitions"] + '\n' + "     2019 awards = " + team_dict["2019 awards"] + '\n'
		)
	else:
		print("Team " + input_viewteam + " not found!")
	
def remove_team():
	input_viewteam = input("Please enter a team number to delete or 0 to exit. \n==>")
	if input_viewteam == '0': 
		print("Exiting...")
		return
	elif input_viewteam in all_team_dict.keys():
		all_team_dict.pop(input_viewteam) 
		print("Team " + input_viewteam + " removed!")
	else:
		print("Team " + input_viewteam + " not found!")


def list_teams():
	big_list = all_team_dict.values()
	for team_dict in big_list:
			print("     Number = " + team_dict["number"] + '\n' + 
				  "     Name = " + team_dict["name"] + '\n' + 
				  "     Location = " + team_dict["location"] + '\n' + 
				  "     Rookie Year = " + team_dict["rookie year"] + '\n' + 
				  "     2019 competitions = " + team_dict["2019 competitions"] + '\n' + "     2019 awards = " + team_dict["2019 awards"] + '\n' +
				  "--------------------------------------------------"
			  	 )
	else: 
		print("No teams found!")
		return 

while True:
	print("MAIN MENU:")
	selection = input("Press \n     1 to add/update a team,\n     2 to view a team,\n     3 to remove a team,\n     4 to list all teams.\n==>")
	if selection == '1':
		add_team()
	elif selection == '2': 
		view_team()
	elif selection == '3':
		remove_team()
	elif selection == '4':
		list_teams()
	else:
		print("I'm sorry, I did not understand that.")




