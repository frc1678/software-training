# chapter_2_lesson_sagayaradj.py
def addDictionary():
	return (
	robotics_teams == {
	int(): {
		'programing language':
		'',
		'width':'',
		'length':'',
		'camera vision':'',
		'number of drivetrain motors':'',
		}})
# chapter_2_lesson_sagayaradj.py
def viewDictionary():
	user_team_number_question = int(input('Type which the number of the team you would like to edit')),
	user_team_section_question = input('Which information from this team would you like to access, programing language, width, length, camera vision, or number of drivetrain motors.'),
	print(robotics_teams[user_team_number_question][user_team_section_question])
# chapter_2_lesson_sagayaradj.py
def removeDictionary():
	robotics_team_number = []
	user_team_number_question = int(input('Type which the number of the team you would like to remove'))
	print(robotics_teams[user_team_number_question])
# chapter_2_lesson_sagayaradj.py
def editDictionary():
	user_team_number_question = int(input('Type which the number of the team you would like to edit'))
	user_team_section_question = input('Which information from this team would you like to edit, programing language, width, length, camera vision, or number of drivetrain motors.')
	print(robotics_teams[user_team_number_question][user_team_section_question])
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
				addDictionary()
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
					print("The input is not valid, please tyxpe an interger")
					while user_team_number != int:
						editDictionary()
			if activity_choice == 'return to menu':
				activity_choice = True;
				state_variable = 'menu'
			if activity_choice == 'quit':
				break
  










                          



