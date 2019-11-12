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

	input_prog_lang = input("Please enter the programming language.\n==>")
	if isinstance(input_name, str):
		team_dict["prog_lang"] = input_prog_lang
	else:
		print("Invalid input.")
		return

	while True:
		input_w = input("Please enter the width.\n==>")
		if (input_w.isdigit()):
			team_dict["w"] = input_w
			break
		else:
			print("Invalid input.")

	while True:
		input_l = input ("Please enter the length.\n==>")
		if (input_l.isdigit()):
			team_dict["l"] = input_l
			break
		else:
			print("Invalid input.")

	while True:
		input_cam_vision = input("Does it have a camera vision system? Please answer 'true' or 'false'.\n==>")
		if input_cam_vision == 'true':
			team_dict["cam_vision"] = input_cam_vision
			break
		elif input_cam_vision == 'false':
			team_dict["cam_vision"] = input_cam_vision
			break
		else: 
			print("Invalid input.")

	while True:
		input_motors = input("Please enter the number of drivetrain motors.\n==>")
		if (input_motors.isdigit()):
			team_dict["motors"] = input_motors
			break
		else:
			print("Invalid input.")
			
	all_team_dict.update( {input_num : team_dict} )
	print("Successfully added team " + input_num + "!") 

def search_team():
	if len(team_dict) == 0:
		print("No teams found.")
		return
	input_searchteam = input("Please enter a team number to check if it exists or 0 to exit.\n==>")
	if input_searchteam == '0':
		print("Exiting...")
		return
	elif input_searchteam in all_team_dict.keys():
		print("Yes, team " + input_searchteam + " does exist.")
	elif input_searchteam == team_dict["name"]:
		print("Yes, team " + input_searchteam + " does exist.")
	else:
		print("Team " + input_searchteam + " does not exist!")

def view_team():
	input_viewteam = input("Please enter a team number to view or 0 to exit.\n==>")
	if input_viewteam == '0': 
		print("Exiting...")
		return 

	elif input_viewteam in all_team_dict.keys():
		team_dict = all_team_dict.get(input_viewteam)
		print("     Number = " + team_dict ["number"] + '\n' +
			  "     Name = " + team_dict ["name"] + '\n' +
			  "     Programming Language = " + team_dict ["prog_lang"] + '\n' + 
			  "     Width = " + team_dict ["w"] + '\n' +
			  "     Length = " + team_dict ["l"] + '\n' + 
			  "     Camera Vision System = " + team_dict ["cam_vision"] + '\n' + 
			  "     Number of drivetrain motors = " + team_dict ["motors"] + '\n' 
		)

	else:
		print("Team " + input_viewteam + " not found!")
	
def remove_team():
	input_removeteam = input("Please enter a team number to delete or 0 to exit. \n==>")
	if input_removeteam == '0': 
		print("Exiting...")
		return
	elif input_removeteam in all_team_dict.keys():
		all_team_dict.pop(input_removeteam) 
		print("Team " + input_removeteam + " removed!")
	else:
		print("Team " + input_removeteam + " not found!")


def list_teams():
	big_list = all_team_dict.values()
	for team_dict in big_list:
			print("     Number = " + team_dict ["number"] + '\n' +
			  	  "     Name = " + team_dict ["name"] + '\n' +
			  	  "     Programming Language = " + team_dict ["prog_lang"] + '\n' + 
			 	  "     Width = " + team_dict ["w"] + '\n' +
			 	  "     Length = " + team_dict ["l"] + '\n' + 
			 	  "     Camera Vision System = " + team_dict ["cam_vision"] + '\n' + 
			 	  "     Number of drivetrain motors = " + team_dict ["motors"] + '\n' +
			 	  "------------------------------------------------"
			  	 )
			return 
	else: 
		print("No teams found!")
		return 

while True:
	print("MAIN MENU:")
	selection = input("Press \n     1 to add/update a team,\n     2 to search for a team,\n     3 to view a team's information,\n     4 to remove a team,\n     5 to list all teams.\n==>")
	if selection == '1':
		add_team()
	elif selection == '2':
		search_team()
	elif selection == '3': 
		view_team()
	elif selection == '4':
		remove_team()
	elif selection == '5':
		list_teams()
	else:
		print("I'm sorry, I did not understand that.")




