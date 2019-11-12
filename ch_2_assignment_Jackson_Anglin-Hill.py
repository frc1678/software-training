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
            request = request.lower()
        except:
            print('Enter the command without numbers.')
            break
        while request == 'add team':
            while True:
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
                while True:
                    width = input('What is the width of the robot in centimeters?: ')
                    try:
                        width = int(width)
                        break
                    except:
                        print("Please use numbers.")
                while True:
                    length = input('What is the length of the robot in centimeters?: ')
                    try:
                        length = int(length)
                        break
                    except:
                        print("Please use numbers.")
                while True:
                    camera = input('Do they have a camera system?: ')
                    try:
                        camera = camera.lower()
                    except:
                        print("Please enter 'Yes' or 'No'")
                    if camera == 'yes':
                        camera = True
                        break
                    elif camera == 'no':
                        camera == False
                        break
                    else:
                        print("Please enter 'Yes' or 'No'")
                while True:
                    drivetrain = input('How many drivetrain motors do they have?: ')
                    try:
                        drivetrain = int(drivetrain)
                        break
                    except:
                        print("Please use numbers.")
                teams[requested_team] = {}
                teams[requested_team]['Name'] = name
                teams[requested_team]['Program'] = program
                teams[requested_team]['Width'] = width
                teams[requested_team]['Length'] = length
                teams[requested_team]['Camera'] = camera
                teams[requested_team]['Drivetrain#'] = drivetrain
            while True:
                uncontinue = input("Would you like to add another team? Enter 'Yes' 'No': ")
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
                print('That is not a valid entry. You will be automatically sent back to the main menu.')
                spacer = 'go back to main'
                break
        while request == 'remove team':
            print(teams.keys())
            while True:
                requested_team = input('Input team number: ')
                try:
                    requested_team = int(requested_team)
                    break
                except:
                    print('Enter team number without letters.')
            if requested_team in teams:
                teams.pop(requested_team)
            else:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            while True:
                uncontinue = input("Would you like to remove another team? Enter 'Yes' 'No': ")
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
                print('That is not a valid entry. You will be automatically sent back to the main menu.')
                spacer = 'go back to main'
                break
        while request == 'view team information':
            while True:
                try:
                    requested_team = int(requested_team)
                    break
                except:
                    print("Enter the team number with no letters.")
                    request = 'view team information'
                    break
            if requested_team in teams:
                print(teams[requested_team])
            else:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            while True:
                uncontinue = input("Would you like to view another team? Enter 'Yes' 'No': ")
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
                print('That is not a valid entry. You will be automatically sent back to the main menu.')
                spacer = 'go back to main'
                break
        while request == 'modify team information':
            print(teams.keys())
            while True:
                requested_team = input('Input team number: ')
                try:
                    requested_team = int(requested_team)
                    break
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
                    while True:
                        width = input('What width is the robot in centimeters?: ')
                        try:
                            width = int(width)
                            break
                        except:
                            print("Please use numbers.")
                    teams[requested_team]['width'] = width
                elif change == 'length':
                    while True:
                        length = input('What length is the robot in centimeters?: ')
                        try:
                            length = int(length)
                            break
                        except:
                            print("Please use numbers.")
                    teams[requested_team]['length'] = length
                elif change == 'camera':
                    while True:
                        camera = input('Do they have a camera system?: ')
                        try:
                            camera = camera.lower()
                        except:
                            print("Please enter 'Yes' or 'No'")
                        if camera == 'yes':
                            camera = True
                            break
                        elif camera == 'no':
                            camera == False
                            break
                        else:
                            print("Please enter 'Yes' or 'No'")
                    teams[requested_team]['camera'] = camera
                elif change == 'drivetraincount':
                    while True:
                        drivetrain = input('How many drivetrains is the robot using?: ')
                        try:
                            drivetrain = int(drivetrain)
                            break
                        except:
                            print("Please use numbers.")
                    teams[requested_team]['drivetraincount'] = drivetrain
            elif requested_team not in teams:
                print('Team not found. Try another team or make sure you entered the team number correctly.')
            while True:
                uncontinue = input("Would you like to modify another team? Enter 'Yes' 'No': ")
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
                print('That is not a valid entry. You will be automatically sent back to the main menu.')
                spacer = 'go back to main'
                break

        while request == 'search for team':
            while True:
                requested_team = input("Which team would you like to confirm is in our database?: ")
                try:
                    requested_team = int(requested_team)
                    break
                except:
                    print("Please use numbers.")
            if requested_team in teams:
                print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
            if requested_team not in teams:
                print('Requested team is not in our database. Make sure you entered it correctly or search for another team.')
            while True:
                uncontinue = input("Would you like to search for another team? Enter 'Yes' 'No': ")
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
                print('That is not a valid entry. You will be automatically sent back to the main menu.')
                spacer = 'go back to main'
                break
        if request == 'list all teams':
            print(teams.keys())
            spacer = 'go back to main'
            request = 'o'
        if request not in allowed_actions_2:
            spacer = 'go back to main'
            request = 'o'