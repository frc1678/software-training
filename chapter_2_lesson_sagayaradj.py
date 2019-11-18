teams = {}
# chapter_2_lesson_sagayaradj.py
def addDictionary():
	robotics_teams = {}
	user_team_name = input('what is the team name')
	user_team_number = int(input('what is the team number'))
	user_programing_language = input('what is the programing language')
	user_width = int(input('what is the width'))
	user_length = int(input('what is the lenght'))
	user_camera_vision = input('what is the camera vision')
	user_number_of_drivetrain_motors = int(input('what is the number of drivetrain motors'))
	robotics_teams = {
		"number": user_team_number,
		"language": user_programing_language,
		"width": user_width,
		"length": user_length,
		"camera vision": user_camera_vision,
		"drivetrain motors": user_number_of_drivetrain_motors}
	teams[user_team_name] = robotics_teams	
# chapter_2_lesson_sagayaradj.py
def viewDictionary():
	user_team_name_question = int(input('Type which the name of the team you would like to view')),
	user_team_section_question = input("Which information from this team would you like to access, 'programing language', 'width', 'length', 'camera vision', 'number of drivetrain motors'."),
	print(robotics_teams[user_team_name_question][user_team_section_question])
# chapter_2_lesson_sagayaradj.py
def removeDictionary():
	user_team_name_question = int(input('Type what is the name of the team you would like to remove'))
	print(robotics_teams[user_team_name_question])
# chapter_2_lesson_sagayaradj.py
def editDictionary():
	user_team_name_question = int(input('Type what is the name of the team you would like to edit'))
	user_team_section_question = input("Which information from this team would you like to edit, 'programing language', 'width', 'length', 'camera vision', or 'number of drivetrain motors'")
	print(robotics_teams[user_team_name_question][user_team_section_question])
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
				addDictionary();
			if activity_choice == 'view':
				activity_choice  = True;
				state_variable = 'view'
				viewDictionary()
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while user_team_number != int:
						viewDictionary()
			if activity_choice == 'remove':
				activity_choice = True;
				state_variable = 'edit'
				removeDictionary()
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while robotics_team_number != int:
						removeDictionary()
			if activity_choice == 'edit':
				activity_choice = True;
				state_variable = 'edit'
				editDictionary()
				if user_team_number != int:
					print("The input is not valid, please type an interger")
					while user_team_number != int:
						editDictionary()
			if activity_choice == 'return to menu':
				activity_choice = True;
				state_variable = 'menu'
			if activity_choice == 'quit':
				break
  










                          



