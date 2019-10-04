robotics_teams = {}
starting_sequence = False
edited = False
activity_choice = ""
while starting_sequence == False:
	state_variable = 'menu';
	print("Main Menu")
	if edited == False:
		activity_choice = input("There is nothing saved. Would you like to add/edit/remove/view information, 'yes' or 'no'")
		print("act: " + str(activity_choice))
		if activity_choice == 'no':
			activity_choice = True;
			print("Great job. You are now finished")
			state_variable = 'menu'  
		if activity_choice == 'yes':
			activity_choice = True;
			state_variable = 'modify'
			activity_choice = input("Would you like to 'add', 'edit', 'remove', or 'view' information")
			print("act: " + str(activity_choice))
			if activity_choice == 'add':
				activity_choice = True;
				state_variable = 'modify'
				robotics_teams = {
					int(): {
						'programing language':
						'',
						'width':'',
						'length':'',
						'camera vision':'',
						'number of drivetrain motors':'',

					}}
			if activity_choice == 'view':
				activity_choice  = True;
				state_variable = 'view'
				user_team_number_question = int(input('Type which the number of the team you would like to edit'))
				user_team_section_question = int(input('Which information from this team would you like to access, programing language, width, length, camera vision, or number of drivetrain motors.'))
				print(robotics_teams[user_team_number_question][user_team_section_question])
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while user_team_number != int:
						user_team_number_question = int(input('Type which the number of the team you would like to edit'))
						user_team_section_question = int(input('Which information from this team would you like to access, programing language, width, length, camera vision, or number of drivetrain motors.'))
			print(robotics_teams[user_team_number_question][user_team_section_question])
			if activity_choice == 'remove':
				robotics_team_number = []
				user_team_number_question = int(input('Type which the number of the team you would like to remove'))
				print(robotics_teams[user_team_number_question])
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while robotics_team_number != int:
						user_team_number_question = int(input('Type which the number of the team you would like to view'))
				print(robotics_teams[user_team_number_question])
			if activity_choice == 'edit':
				activity_choice = True;
				state_variable = 'modify'
				user_team_number_question = int(input('Type which the number of the team you would like to edit'))
				user_team_section_question = int(input('Which information from this team would you like to edit, programing language, width, length, camera vision, or number of drivetrain motors.'))
				print(robotics_teams[user_team_number_question][user_team_section_question])
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while user_team_number != int:
						user_team_number_question = int(input('Type which the number of the team you would like to edit'))
						user_team_section_question = int(input('Which information from this team would you like to edit, programing language, width, length, camera vision, or number of drivetrain motors.'))
				print(robotics_teams[user_team_number_question][user_team_section_question])
			if activity_choice == 'return to menu':
				activity_choice = True;
				state_variable = 'menu'
			if activity_choice == 'quit':
				break
  










                          



