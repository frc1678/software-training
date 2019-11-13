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

while on:
    print(allowed_actions_1)
    request = input('What would you like to do?: ')
    request = request.lower()
    while request == 'add team':
        while True:
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
                break
            except:
                print("Enter the team number with no letters.")
                request = 'add team'
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
                    camera = False
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
            request = 'o'
        elif uncontinue.lower() == 'yes':
            request = 'add team'
        else:
            print('That is not a valid entry. You will be automatically sent back to the main menu.')
            reqest = 'o'
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
            request = 'o'
        elif uncontinue.lower() == 'yes':
            request = 'remove team'
        else:
            print('That is not a valid entry. You will be automatically sent back to the main menu.')
            request = 'o'
    while request == 'view team information':
        while True:
            requested_team = input('Input team number: ')
            try:
                requested_team = int(requested_team)
                break
            except:
                print("Enter the team number with no letters.")
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
            request = 'o'
        elif uncontinue.lower() == 'yes':
            request = 'view team information'
        else:
            print('That is not a valid entry. You will be automatically sent back to the main menu.')
            request = 'o'
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
                teams[requested_team]['Name'] = name
            elif change == 'program':
                program = input('What program is the team using?: ')
                teams[requested_team]['Program'] = program
            elif change == 'Width':
                while True:
                    width = input('What width is the robot in centimeters?: ')
                    try:
                        width = int(width)
                        break
                    except:
                        print("Please use numbers.")
                teams[requested_team]['Width'] = width
            elif change == 'length':
                while True:
                    length = input('What length is the robot in centimeters?: ')
                    try:
                        length = int(length)
                        break
                    except:
                        print("Please use numbers.")
                teams[requested_team]['Length'] = length
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
                        camera = False
                        break
                    else:
                        print("Please enter 'Yes' or 'No'")
                teams[requested_team]['Camera'] = camera
            elif change == 'drivetraincount':
                while True:
                    drivetrain = input('How many drivetrains is the robot using?: ')
                    try:
                        drivetrain = int(drivetrain)
                        break
                    except:
                        print("Please use numbers.")
                teams[requested_team]['Drivetraincount'] = drivetrain
        else:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        while True:
            uncontinue = input("Would you like to modify another team? Enter 'Yes' 'No': ")
            try:
                uncontinue = uncontinue.lower()
                break
            except:
                print("Enter 'Yes' or 'No' with no numbers.")
        if uncontinue.lower() == 'no':
            request = 'o'
        elif uncontinue.lower() == 'yes':
            request = 'modify team information'
        else:
            print('That is not a valid entry. You will be automatically sent back to the main menu.')
            request = 'o'

    while request == 'search for team':
        while True:
            requested_team = input("Which team would you like to confirm is in our database? If no response is given from your entry, the team is not in our database.: ")
            try:
                requested_team = int(requested_team)
                if requested_team in teams:
                    print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
                break
            except:
                requested_team.lower()
                for team in teams.values():
                    if team['Name'] == requested_team:
                        print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
                break
        while True:
            uncontinue = input("Would you like to search for another team? Enter 'Yes' 'No': ")
            try:
                uncontinue = uncontinue.lower()
                break
            except:
                print("Enter 'Yes' or 'No' with no numbers.")
        if uncontinue.lower() == 'no':
            request = 'o'
        elif uncontinue.lower() == 'yes':
            request = 'search for team'
        else:
            print('That is not a valid entry. You will be automatically sent back to the main menu.')
            request = 'o'
    if request == 'list all teams':
        print(teams.keys())
        request = 'o'