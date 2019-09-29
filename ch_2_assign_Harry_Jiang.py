teams = {'teddy': {'number': '7', 'programming_language': '5', 'width': '5', 'length': '5', 'vision_system': 'yes', 'number_of_drivetrain_motors': '3'}, 'emily': {'number': '4', 'programming_language': 'c++', 'width': '3', 'length': '5', 'vision_system': 'no', 'number_of_drivetrain_motors': '9'}}
command = ''
while command != 'quit':
	command = input ("What is your command(add a team, update a team, search a team, delete a team, list all teams, quit)")
	#print(command);
	if command == 'add a team' :
	    team_name = input ("What is team name? ")
	    print(team_name)
	    # Number, name, programming language, width, length, has camera vision system, number of drivetrain motors
	    number = input('number:')
	    if not number.isnumeric():
	        print("your input for team number: "+ number + " is invalid")
	    else:
		    programming_language = input('progamming language:')
		        if value.lower() not in ['java', 'python', 'c++']:
		    		print("input is invalid")
		    		isInputValid = False
		    	else:
			    width = input('width:')
			    if not width.isnumeric():
			    	print("your input for width: "+ width +" is invalid")
			    else:
				    length = input('length:')
				    if not length.isnumeic():
				    	print("your input for length: "+ length +" is invalid")
				    else:
					    vision_system = input('has a camera vision system:')
					    if vision_system != 'yes' or vision_system != 'no':
					        print("your input for vision system: "+ vision_system +" is invalid")
					    else:
						    number_of_drivetrain_motors = input('number of drivetrain motors:')
						    team_info = {}
						    team_info.update(number = number)
						    team_info.update(programming_language = programming_language)
						    team_info.update(width = width)
						    team_info.update(length = length)
						    team_info.update(vision_system = vision_system)
						    team_info.update(number_of_drivetrain_motors = number_of_drivetrain_motors)
						    #print(team_info)
						    teams[team_name] = team_info
						    print('team ' + team_name + ' has created successfully.')
						    print(teams[team_name])
	if command == 'update a team':
		print('update a team')
		team_name = input('What team needs an update? ')
		print(teams[team_name])
		if team_name in teams.keys():
		    print("number, programming_language, width, length, vision_system, number_of_drivetrain_motors")
		    field = input('What field needs and update: ')
		    value = input('value: ')
		    isInputValid = True
		    if field in ['number','width', 'length', 'number_of_drivetrain_motors']:
		        if not value.isnumeric():
		            print('input is not valid')
		            isInputValid = False
		    elif field == "vision_system":
		        if value.lower() != 'yes' and value.lower() !='no':
		        	print("input is invalid")
		        	isInputValid = False
		    elif field == "programming_language":
		    	if value.lower() not in ['java', 'python', 'c++']:
		    		print("input is invalid")
		    		isInputValid = False
		    else:
		    	print("field you want to update is invalid")
		    	isInputValid = False


		    if isInputValid:
		        teams[team_name][field] = value
		        print("team updated successfully")
		        print(teams[team_name])


		else:
		    print('team does not exist')
	if command == 'search a team':
	    team_name = input('What team? ')
	    if team_name in teams.keys():
		    print(teams[team_name])
	    else:
		    print('team does not exist')
	if command == 'delete a team':
	    team_name = input('delete which team? ')
	    if team_name in teams.keys():
	        print(teams.keys())
	        teams.pop(team_name)
	        print(teams.keys())
	    else:
	        print('team ' + team_name +' does not exist')
	if command == 'list all teams':
	   print(teams)
print('end')