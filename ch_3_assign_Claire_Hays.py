teams = {}
while True:
	command = input("""Enter the command (add a team, remove a team, search for a team, list all teams, 
view team's information, modify team's information, view all teams and information, or quit): """)
	def check_if_int(a):
		while True:
			if a == 'quit':
				return None
			elif a.isdigit() == True:
				a = int(a)
				return a
			else:
				a = input("Please type attribute as an integer: ")
	def check_if_bool(b):
		while True:
			if b == 'quit':
				return None
			elif b.lower() == 'yes':
				b = True
				return b
			elif b.lower() == 'no':
				b = False
				return b
			else:
				b = input("Please type either 'yes' or 'no': ")
	def check_if_quit(c):
		if c == 'quit':
			return True 

	if command.lower() == "add a team":
		team_num = input("What is the team number? ") 
		team_num = check_if_int(team_num)
		if team_num is None: # User entered 'quit'
			break

		location = input("What is the location of the team? ")
		if check_if_quit(location) == True:
			break

		rookie_year = input("What was the team's rookie year? ")
		rookie_year = check_if_int(rookie_year)
		if rookie_year is None: # User entered 'quit'
			break
		

		compete_2019 = input("Did the team compete in 2019? ")
		if check_if_quit(compete_2019) == True:
			break
		compete_2019 = check_if_bool(compete_2019)
		if compete_2019 is None: # User entered 'quit'
			break

		num_of_comp = input("How many competitions did the team compete in during the 2019 season? ")
		if check_if_quit == True:
			break
		num_of_comp = check_if_int(num_of_comp)
		if num_of_comp is None: # User entered 'quit'
			break
		competitions = {}
		while num_of_comp > 0:
			comp_name = input("What is the name of the competition? ")
			if check_if_quit(comp_name) == True:
				break
			else:
				comp_loc = input("What is the location of the competition? ")
			comp = {comp_name: comp_loc}
			competitions.update(comp)
			num_of_comp -= 1

		num_of_awards = input("How many awards did the team earn during the 2019 season? ")
		if check_if_quit(num_of_awards) == True:
			break
		num_of_awards = check_if_int(num_of_awards)
		if num_of_awards is None: # User entered 'quit'
			break
		awards = []
		while num_of_awards > 0:
			award = input("What is the name of the award? ")
			if check_if_quit(award) == True:
				break
			awards.append(award)
			num_of_awards -= 1

		attributes = {'location': location, 
			'rookie year': rookie_year, 
			'2019 compete': compete_2019, 
			'names and locations of 2019 competitions': competitions, 
			'2019 awards': awards}
		new_team = {team_num: attributes}
		teams.update(new_team)
		

	elif command == "remove a team":
		remove_team_num = input("What team number would you like to remove? ")
		if check_if_quit(remove_team_num) == True:
			break
		remove_team_num = check_if_int(remove_team_num)
		if remove_team_num is None: # User entered 'quit'
			break
		teams.pop(remove_team_num)
		print("Team number successfully removed. To view new team list, type 'list all teams'")


	elif command == "search for a team":
		team_search = input("What team would you like to search for? ")
		if check_if_quit(team_search) == True:
			break
		team_search = check_if_int(team_search)
		if team_search is None: # User entered 'quit'
			break
		print(teams.get(team_search))
					   

	elif command == "list all teams":
			print(teams.keys())


	elif command == "view team's information":
		view_team_num = input("What team's information would you like to view? ")
		if check_if_quit(view_team_num) == True:
			break
		view_team_num = check_if_int(view_team_num)
		if view_team_num is None: # User entered 'quit'
			break
		view_team_attribute = str(input("""What attribute would you like to view (location, rookie year, 2019 compete,
names and locations of 2019 competitions, or 2019 awards)? """))
		if check_if_quit(view_team_attribute) == True:
			break
		print(teams[view_team_num][view_team_attribute])


	elif command == "modify team's information":
		chng_team_num = input("What team number's information would you like to change? ")
		if check_if_quit(chng_team_num) == True:
			break
		chng_team_num = check_if_int(chng_team_num)
		if chng_team_num is None: # User entered 'quit'
			break
		chng_attribute = input("""What attribute would you like to change (location, rookie year, 2019 compete,
names and locations of 2019 competitions, or 2019 awards)? """)
		if check_if_quit(chng_attribute) == True:
			break	

		if chng_attribute == 'location':
			new_location = input("What is the location of the team? ")
			if check_if_quit(new_location) == True:
				break
			new_rookie_year = teams[chng_team_num]['rookie year']
			new_compete_2019 = teams[chng_team_num]['2019 compete']
			new_competitions = teams[chng_team_num]['names and locations of 2019 competitions']
			new_awards = teams[chng_team_num]['2019 awards']

		elif chng_attribute == 'rookie year':
			new_rookie_year = input("What was the team's rookie year? ")
			new_rookie_year = check_if_int(new_rookie_year)
			if new_rookie_year is None: # User entered 'quit'
				break
			new_location = teams[chng_team_num]['location']
			new_compete_2019 = teams[chng_team_num]['2019 compete']
			new_competitions = teams[chng_team_num]['names and locations of 2019 competitions']
			new_awards = teams[chng_team_num]['2019 awards']
		
		elif chng_attribute == '2019 compete':
			new_compete_2019 = input("Did the team compete in 2019? ")
			if check_if_quit(new_compete_2019) == True:
				break
			new_compete_2019 = check_if_bool(new_compete_2019)
			if new_compete_2019 is None: # User entered 'quit'
				break
			new_location = teams[chng_team_num]['location']
			new_rookie_year = teams[chng_team_num]['rookie year']
			new_competitions = teams[chng_team_num]['names and locations of 2019 competitions']
			new_awards = teams[chng_team_num]['2019 awards']

		elif chng_attribute == 'names and locations of 2019 competitions':
			new_num_of_comp = input("How many competitions did the team compete in during the 2019 season? ")
			if check_if_quit(new_num_of_comp) == True:
				break
			new_num_of_comp = check_if_int(new_num_of_comp)
			if new_num_of_comp is None: # User entered 'quit'
				break
			new_competitions = {}
			while new_num_of_comp > 0:
				new_comp_name = input("What is the name of the competition? ")
				if check_if_quit(new_comp_name) == True:
					break
				else:
					new_comp_loc = input("What is the location of the competition? ")
					new_comp = {new_comp_name: new_comp_loc}
					new_competitions.update(new_comp)
					new_num_of_comp -= 1
			new_location = teams[chng_team_num]['location']
			new_rookie_year = teams[chng_team_num]['rookie year']
			new_compete_2019 = teams[chng_team_num]['2019 compete']
			new_awards = teams[chng_team_num]['2019 awards']

		elif chng_attribute == '2019 awards':
			new_num_of_awards = input("How many awards did the team earn during the 2019 season? ")
			if check_if_quit(new_num_of_awards) == True:
				break
			new_num_of_awards = check_if_int(new_num_of_awards)
			if new_num_of_awards is None: # User entered 'quit'
				break
			new_awards = []
			while new_num_of_awards > 0:
				new_award = input("What is the name of the award? ")
				if check_if_quit(new_award) == True:
					break
				new_awards.append(new_award)
				new_num_of_awards -= 1
			new_location = teams[chng_team_num]['location']
			new_rookie_year = teams[chng_team_num]['rookie year']
			new_compete_2019 = teams[chng_team_num]['2019 compete']
			new_competitions = teams[chng_team_num]['names and locations of 2019 competitions']

		new_attributes = {'location': new_location, 
			'rookie year': new_rookie_year, 
			'2019 compete': new_compete_2019, 
			'names and locations of 2019 competitions': new_competitions, 
			'2019 awards': new_awards}
		teams[chng_team_num] = new_attributes    

	elif command == "view all teams and information":
		print(teams)

	elif command == "quit":
			break



