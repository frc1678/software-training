team_dictionary={
	1678:{
		"Name":"Citrus Circuits",
		"Location":"Davis_CA",
		"Rookie_year":2005, 
		"Competition_Status_2019":True, 
		"Names_of_Competitions":{
			"Central_Valley_Regional":"Fresno_CA", 
			"Sacramento_Regional":"Davis_CA", 
			"Aerospace_Valley_Regional":"Lancaster_CA",
			"Carver_Division":"Houston_TX",
			"Einstein_Field":"Houston_TX",
			"RCC_Qianjiang_International_Robotics_Invitational":"Hangzhou_CN",
			"Chezy_Champs":"San_Jose_CA"}, 
		"Competition_Awards":[
			"Regional_Chairmans_Award", 
			"Regional_Winner",
			"Deans_List",
			"Regional_Winner",
			"Industrial_Design_Award",
			"Excellence_in_Engineering",
			"Championship_Subdivision_Winner",
			"Entrepreneurship-Award"]},
	3132:{
		"Name":"Thunder Down Under",
		"Location":"Sydney_Australia",
		"Rookie_year":2010,
		"Competition_Status_2019":True,
		"Names_of_Competitions":{
			"Southern_Cross_Regional":"Sydeny_Olympic_Park",
			"South_Pacific_Regional":"Sydeny_Olympic_Park",
			"Carver_Division":"Houston_TX",
			"Einstein_Field":"Houston_TX"},
		"Competition_Awards":[
			"Woodie_Flowers",
			"Gracious_Professionalism",
			"Regional_Engineering_Inspiration",
			"Safety_Award"]},
	1902:{
		"Name":"Exploding Bacon",
		"Location":"Orlando_FL",
		"Rookie_year":2006, 
		"Competition_Status-2019":True, 
		"Names_of_Competitions":{
			"Palmetto_Regional":"Myrtle_Beach", 
			"Orlando_Regional":"Orlando_FL", 
			"Newton_Division":"Houston_TX",
			"Einstein_Field":"Houston_TX"}, 
		"Competition_Awards":[
			"Regional_Chairmans_Award", 
			"Deans_List",
			"Entrepreneurship-Award",
			"Chairmans_Award_Finalist"]},
	5458:{
		"Name":"Digital Minds",
		"Location":"Woodland_CA",
		"Rookie_year":2015,
		"Competition_Status_2019":True,
		"Names_of_Competitions":{
			"Central_Valley_Regional":"Fresno_CA",
			"Sacramento_Regional":"Davis_CA"},
		"Competition_Awards":[
			"None"]},
	6174:{
		"Name":"Kaprekar's Constants",
		"Location":"Winters_CA",
		"Rookie_year":2016,
		"Competition_Status_2019":True,
		"Names_of_Competitions":{
			"Sacramento_Regional":"Davis_CA"},
		"Competition_Awards":[
			"None"]}}

main_menu = """\nEnter the number of the action you want to do
				0   return to main menu
				1   add a team
				2   modify a team
				3   view a team
				4   remove a team
				5   search a team
				6   list all teams 
				7   leave \n """
def defining_team_number():
	return input("Enter the number of your team \n")
def get_user_action():
	return int(input(main_menu))
def new_action():
	return input()
def not_available():
	print("I'm sorry the information you are looking for is not available")
def number_validation():
	return team_number.isdigit()
def team_number_validation(team):
	return team in team_dictionary

user_action = get_user_action()
while True:
	if user_action == 0:
	#return to main menu
		user_action = get_user_action()
	elif user_action == 1:
	#add a team
		team_number = defining_team_number()
		if number_validation() == True:
			team_number = int(team_number)
			if team_number_validation(team_number) == False: 
				Name = input("What is the name of your team?\n")
				Location = input("What is the location of your team? \n")
				Rookie_year = input("What is the rookie year of your team? \n")
				Competition_Status_2019 = input("What is the 2019 competition status of your team? \n")
				Names_of_Competitions = input("What are the names of the competitions of your team? \n")
				Competition_Awards = input("What are the names of the competition awards of your team? \n")
				added_team_information = {
					"Name":Name,
					"Location":Location,
					"Rookie_year":Rookie_year,
					"Competition_Status_2019": Competition_Status_2019,
					"Names_of_Competitions": Names_of_Competitions,
					"Competition_Awards": Competition_Awards}
				team_dictionary.update({team_number:added_team_information})
				user_action = get_user_action()
			elif team_number_validation(team_number) == True: 
				print("The team you want to add is already in the dictionary")
				user_action = get_user_action()
		elif number_validation() == False:
			print("Your input is not an integer, please ensure that you input an integer")
			user_action = get_user_action()
	elif user_action == 2:
	#modify a team
		team_number = defining_team_number()
		if number_validation() == True:
			team_number = int(team_number)
			if team_number_validation(team_number) == True:
				modify_attribute = input("What is the attribute that you want to modify?\n")
				if modify_attribute in team_dictionary[team_number]:
					new_attribute = input("What do you want the new " +modify_attribute+ " to be?\n")
					team_dictionary[team_number].update({modify_attribute:new_attribute})
					print(team_dictionary[team_number])
					user_action = get_user_action()
				elif modify_attribute not in team_dictionary[team_number]:
					not_available()
					user_action = get_user_action()
			elif team_number_validation(team_number) == False:
				not_available()
				user_action = get_user_action()
		elif number_validation() == False: 
			print("Your input is not an integer, please ensure that you input an integer")
			user_action = get_user_action()
	elif user_action == 3: 
	#view a team
		team_number = defining_team_number()
		if number_validation() == True:
			team_number = int(team_number)
			if team_number_validation(team_number) == True:
				print(team_dictionary[team_number])
				user_action = get_user_action()
			elif team_number_validation(team_number) == False:
				not_available()
				user_action = get_user_action()
		elif number_validation() == False:
			print("Your input is not an integer, please ensure that you input an integer")
			user_action = get_user_action()
	elif user_action == 4:
	#remove a team
		team_number = defining_team_number()
		if number_validation() == True:
			team_number = int(team_number)
			if team_number_validation(team_number) == True:
				team_dictionary.pop(team_number)
				print(team_dictionary)
				user_action = get_user_action()
			elif team_number_validation(team_number) == False:
				not_available()
				user_action = get_user_action()
		elif number_validation() == False:
			print("Your input is not an integer, please ensure that you input an integer")
			user_action = get_user_action()
	elif user_action == 5:
	#search a team
		team_number = input("Enter the number or name of your team\n")
		if number_validation() == True:
			team_number = int(team_number)
			if team_number_validation(team_number) == True:
				print(team_dictionary[team_number])
				user_action = get_user_action()
			elif team_number_validation(team_number) == False:
				not_available()
				user_action = get_user_action()
		elif number_validation() == False:
			for key in team_dictionary:
				if team_number == team_dictionary[key]["Name"]:
					team_number = str(team_number)
					print(team_dictionary[key])	
					user_action = get_user_action()
			else:
				not_available()
				user_action =get_user_action()
	elif user_action == 6:
	#list all teams
		for team_number, team_attributes in team_dictionary.items():
			print(team_number)
			for key, value in team_attributes.items():
				print(f"{key}: {value}")
		user_action = get_user_action()
	elif user_action == 7:
	#leave		
		break
	elif user_action not in [1, 2, 3, 4, 5, 6, 7]:
		not_available()
		user_action = get_user_action()