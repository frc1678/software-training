on = True
#teams is a dictionary with teams numbers as the keys and their information as the definitions.
teams = {}
#team_names is a list containing the names of the teams.
allowed_actions = [
    'Add team',
    'Remove team',
    'View team information',
    'Modify team information',
    'Search for team',
]
while on:
    print(teams.keys())
    print(allowed_actions)
    request = input('What would you like to do? Please enter exactly as shown: ')
    while request == 'Add team':
        requested_team = input('Input team number: ')
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
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Remove team':
        print(teams.keys())
        requested_team = input('Input team number: ')
        if requested_team in teams:
            teams.pop(requested_team)
        else:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to remove another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'View team information':
        requested_team = input('Input team number: ')
        if requested_team in teams:
            print(teams[requested_team])
        else:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to view another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Modify team information':
        print(teams.keys())
        requested_team = input("What team's information would you like to edit?: ")
        if requested_team in teams:
            change = input("What would you like to change for this team? Enter 'Name' 'Program' 'Width' 'Length' 'Camera' 'Drivetrain#': ")
            if change == 'Name':
                name = input('What is the team name?: ')
                teams[requested_team].pop('Name')
                teams[requested_team]['Name'] = name
            if change == 'Program':
                program = input('What program is the team using?: ')
                teams[requested_team].pop('Program')
                teams[requested_team]['Program'] = program
            if change == 'Width':
                width = input('What width is the robot?: ')
                teams[requested_team].pop('Width')
                teams[requested_team]['Width'] = width
            if change == 'Length':
                length = input('What length is the robot?: ')
                teams[requested_team].pop('Length')
                teams[requested_team]['Length'] = length
            if change == 'Camera':
                camera = input('Does the robot have a camera system?: ')
                teams[requested_team].pop('Camera')
                teams[requested_team]['Camera'] = camera
            if change == 'Drivetrain#':
                drivetrain = input('How many drivetrains is the robot using?: ')
                teams[requested_team].pop('Drivetrain#')
                teams[requested_team]['Drivetrain#'] = drivetrain
        elif requested_team not in teams:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to modify another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Search for team':
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
        if uncontinue == 'No':
            request = 'Done'