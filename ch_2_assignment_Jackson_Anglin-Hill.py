on = True
#teams is a dictionary with teams numbers as the keys and their information as the definitions.
teams = {}
#team_names is a list containing the names of the teams.
allowed_actions_1 = [
    'Add team',
    'Remove team',
    'View team information',
    'Modify team information',
    'Search for team',
    'List all teams'
    ]
#allowed_actions_1 is for display, allowed_actions_2 is used for input validation
allowed_actions_2 = [
    'add team',
    'remove team',
    'view team information',
    'modify team information',
    'search for team',
    'list all teams'
    ]

while on:
    print(allowed_actions_1)
    request = input('What would you like to do?: ')
    spacer = 'O'
#spacer is used because if break command is used, it cycles back through to where request is reset instead of request remaining as defined in later code.
    while spacer == 'O':
        try:
            request = str(request.lower())
        except:
            print('Please enter a command without numbers.')
            spacer = 'back to main menu'
        request = request.lower()
        while request == 'add team':
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
            except:
                print("Enter the team number with no letters.")
                request = 'add team'
                break
            if requested_team in teams:
                print('This team is already in the system. Please add a different team, confirm you have entered the team number correctly, or edit the information already existing in this team.')
            else:
                name = input('What is the team name?: ')
                program = input('What programming language do they use?: ')
                width = input('What is the width of the robot?: ')
                length = input('What is the length of the robot?: ')
                camera = input('Do they have a camera system?: ')
                drivetrain = input('How many drivetrain motors do they have?: ')
                teams[requested_team] = {}
                teams[requested_team]['Name'] = name
                teams[requested_team]['Program'] = program
                teams[requested_team]['Width'] = width
                teams[requested_team]['Length'] = length
                teams[requested_team]['Camera'] = camera
                teams[requested_team]['Drivetrain#'] = drivetrain
            uncontinue = input("Would you like to add another team? Enter 'Yes' 'No': ")
#Returns to main menu
            while True:
                try:
                    uncontinue = uncontinue.lower()
                    break
                except:
                    print("Enter 'Yes' or 'No' with no numbers.")
            if uncontinue.lower() == 'no':
                spacer = 'go back to main'
                request = 'o'
            elif uncontinue.lower() == 'yes':
                request = 'add team'
            else:
                print('That is not a valid entry.')
                spacer = 'go back to main'
                break
        while request == 'remove team':
            print(teams.keys())
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
            except:
                print("Enter the team number with no letters.")
                request = 'remove team'
                break
            if requested_team in teams:
                teams.pop(requested_team)
            else:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            uncontinue = input("Would you like to remove another team? Enter 'Yes' 'No': ")
            while True:
                try:
                    uncontinue = uncontinue.lower()
                    break
                except:
                    print("Enter 'Yes' or 'No' with no numbers.")
            if uncontinue.lower() == 'no':
                spacer = 'go back to main'
                request = 'o'
            elif uncontinue.lower() == 'yes':
                request = 'remove team'
            else:
                print('That is not a valid entry.')
                spacer = 'go back to main'
                break
        while request == 'view team information':
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
            except:
                print("Enter the team number with no letters.")
                request = 'view team information'
                break
            if requested_team in teams:
                print(teams[requested_team])
            else:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            uncontinue = input("Would you like to view another team? Enter 'Yes' 'No': ")
            while True:
                try:
                    uncontinue = uncontinue.lower()
                    break
                except:
                    print("Enter 'Yes' or 'No' with no numbers.")
            if uncontinue.lower() == 'no':
                spacer = 'go back to main'
                request = 'o'
            elif uncontinue.lower() == 'yes':
                request = 'view team information'
            else:
                print('That is not a valid entry.')
                spacer = 'go back to main'
                break
        while request == 'modify team information':
            print(teams.keys())
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
            except:
                print("Enter the team number with no letters.")
                request = 'modify team information'
                break
            if requested_team in teams:
                change = input("What would you like to change for this team? Enter 'Name' 'Program' 'Width' 'Length' 'Camera' 'Drivetraincount': ")
                try:
                    change = str(change.lower())
                except:
                    print('Do not use numbers while entering the requested section')
                    request = 'modify team information'
                    break
                if change == 'name':
                    name = input('What is the team name?: ')
                    teams[requested_team]['name'] = name
                elif change == 'program':
                    program = input('What program is the team using?: ')
                    teams[requested_team]['program'] = program
                elif change == 'width':
                    width = input('What width is the robot?: ')
                    teams[requested_team]['width'] = width
                elif change == 'length':
                    length = input('What length is the robot?: ')
                    teams[requested_team]['length'] = length
                elif change == 'camera':
                    camera = input('Does the robot have a camera system?: ')
                    teams[requested_team]['camera'] = camera
                elif change == 'drivetraincount':
                    drivetrain = input('How many drivetrains is the robot using?: ')
                    teams[requested_team]['drivetraincount'] = drivetrain
            elif requested_team not in teams:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            uncontinue = input("Would you like to modify another team? Enter 'Yes' 'No': ")
            while True:
                try:
                    uncontinue = uncontinue.lower()
                    break
                except:
                    print("Enter 'Yes' or 'No' with no numbers.")
            if uncontinue.lower() == 'no':
                spacer = 'go back to main'
                request = 'o'
            elif uncontinue.lower() == 'yes':
                request = 'modify team information'
            else:
                print('That is not a valid entry.')
                spacer = 'go back to main'
                break

        while request == 'search for team':
            good = 'bad'
            requested_team = input("Which team would you like to confirm is in our database?: ")
            if requested_team in teams:
                print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
            for team in teams.values():
                if team['Name'] == requested_team:
                    print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
                    good = 'good'
            if requested_team not in teams and good != 'good':
                print('Requested team is not in our database. Make sure you entered it correctly or search for another team.')
            uncontinue = input("Would you like to search for another team? Enter 'Yes' 'No': ")
            while True:
                try:
                    uncontinue = uncontinue.lower()
                    break
                except:
                    print("Enter 'Yes' or 'No' with no numbers.")
            if uncontinue.lower() == 'no':
                spacer = 'go back to main'
                request = 'o'
            elif uncontinue.lower() == 'yes':
                request = 'search for team'
            else:
                print('That is not a valid entry.')
                spacer = 'go back to main'
                break
        if request == 'list all teams':
            print(teams.keys())
            spacer = 'go back to main'
            request = 'o'
        if request not in allowed_actions_2:
            spacer = 'go back to main'
            request = 'o'