all_team_dict = {}
team_dict = {}
def add_team():
	input_num = input("Please enter a team number to add/update or 0 to exit.\n(If the team already exists, the information will be updated.)\n==>")
	if input_num == '0':
		print("Exiting...")
		return
	elif (input_num.isdigit()):
		team_dict["number"] = input_num
	else: 
		print("Invalid input.")
		return

	input_name = input("Please enter the team name.\n==>")
	if isinstance(input_name, str):
		team_dict["name"] = input_name
	else: 
		print("Invalid input.")
		return 

	input_prog_lang = input("Please enter the programming language.\n==>")
	if isinstance(input_name, str):
		team_dict["prog_lang"] = input_prog_lang
	else:
		print("Invalid input.")
		return

	input_w = input("Please enter the width.\n==>")
	if (input_w.isdigit()):
		team_dict["w"] = input_w
	else:
		print("Invalid input.")
		return 

	input_l = input ("Please enter the length.\n==>")
	if (input_l.isdigit()):
		team_dict["l"] = input_l
	else:
		print("Invalid input.")
		return 

	input_cam_vision = input("Does it have a camera vision system? Please answer 'true' or 'false'.\n==>")
	if input_cam_vision == 'true':
		team_dict["cam_vision"] = input_cam_vision
	elif input_cam_vision == 'false':
		team_dict["cam_vision"] = input_cam_vision
	else: 
		print("Invalid input.")
		return

	input_motors = input("Please enter the number of drivetrain motors.\n==>")
	if (input_motors.isdigit()):
		team_dict["motors"] = input_motors
	else:
		print("Invalid input.")
		return

	all_team_dict.update( {input_num : team_dict} )
	print("Successfully added team " + input_num + "!") 

def view_team():
	input_viewteam = input("Please enter a team number to view or 0 to exit.\n==>")
	if input_viewteam == '0': 
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
	input_viewteam = input("Please enter a team number to delete or 0 to exit. \n==>")
	if input_viewteam == '0': 
		return
	elif input_viewteam in all_team_dict.keys():
		all_team_dict.pop(input_viewteam) 
		print("Team " + input_viewteam + " removed!")
	else:
		print("Team " + input_viewteam + " not found!")


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




