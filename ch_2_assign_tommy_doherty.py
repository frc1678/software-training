teams = {}
command = ''
while command != 'quit':
    command = input ('What would you like to do"(add a team, update a team, search a team, delete a team, list all teams, quit) ')
    if command == 'add a team': #if you type add a team into menu
        team_number = input('Team Number ') #makes team_number equal to user input
        if team_number.isnumeric():    
            teams[team_number] = {}                                                      #add team 7-20
            team_name = input ('Team Name ')
            teams[team_number]["Team Name"] = team_name
            programming_language = input ('Programming Language ')
            teams[team_number]['Programming Language'] = programming_language
            width = input ('Width ')
            if width.isnumeric():    
                teams[team_number]['Width'] = width 
                length = input ('Length ')                                                  
                if length.isnumeric():  
                    teams[team_number]['Length'] = length
                    has_camera_vision = input ('Camera Vision, Enter Yes or No ')
                    if has_camera_vision == 'Yes' or has_camera_vision == 'No':
                        teams[team_number]['Camera Vision'] = has_camera_vision
                        number_of_drivetrain_motors = input ('Number of Drivetrain Motors ')
                        if number_of_drivetrain_motors.isnumeric():   
                            teams[team_number]['Number of Drivetrain Motors'] = number_of_drivetrain_motors
                        else:
                            print('Bruh')
                    else:
                        print('Bruh')
                else:
                    print('Bruh')
            else:
                print('Bruh')
        else:
            print('Bruh')
    
    if command == 'update a team':                                              #update a team 21-42
        team_number = input('What team would you like to change? ')
        if team_number.isnumeric():  
            if team_number in teams.keys():
                attribute = input('What attribute would you like to change? ')
                if attribute == 'team name' or attribute == 'programming language' or attribute == 'width' or attribute == 'length' or attribute == 'has camera vision' or attribute == 'number of drivetrain motors':    
                    if attribute == 'team name':
                        team_name = input('Enter Team Name ')
                        if not team_name.isnumeric():
                            teams[team_number]['Team Name'] = team_name
                        else:
                            print('Bruh')
                    if attribute == 'programming language':
                        programming_language = input('Enter Programming Language ') 
                        if not programming_language.isnumeric():                             #team name, team number, language, length, width 
                            teams[team_number]['Programming Language'] = programming_language
                        else:
                            print('Bruh')
                    if attribute == 'width':
                        width = input('Enter Width ')
                        if width.isnumeric():
                            teams[team_number]['Width'] = width
                        else:
                            print('bruh')
                    if attribute == 'length':
                        length = input('Enter Length ')
                        if length.isnumeric():
                            teams[team_number]['Length'] = length
                        else:
                            print('Bruh')
                    if attribute == 'has camera vision':
                        has_camera_vision = input('Enter Yes or No ')
                        if has_camera_vision == 'Yes' or has_camera_vision == 'No':
                            teams[team_number]['Camera Vision'] = has_camera_vision
                        else:
                            print('Bruh')
                    if attribute == 'number of drivetrain motors':
                        number_of_drivetrain_motors = input('Number of Drivetrain Motors ')
                        if number_of_drivetrain_motors.isnumeric():
                            teams[team_number]['Number of Drivetrain Motors'] = number_of_drivetrain_motors
                        else:
                            print('Bruh')
                else:
                    print('Bruh')
            else:
                print('this is not an existing team')
        else:
            print('Bruh')
            #end of update teams lines



    if command == 'list all teams':                                             #list all teams 43-44
        print(teams)
    if command == 'search for a team':                                            #search for a team
        search_team = input("What is the team you want to search? ")        
        if search_team not in teams:
            print('Not In Dictionary')
        if search_team in teams:
            print("Yes, the team you are looking is in the dictionary")
            print(teams[search_team])
    if command == 'delete a team':
        delete_a_team = input('Which team would you like to delete?')
        if delete_a_team not in teams:
            print('Not in Dictionary')
        if delete_a_team in teams:
            teams.pop(delete_a_team)
#end of code








            




            


