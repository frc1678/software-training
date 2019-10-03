on = True
#teams is a dictionary with teams numbers as the keys and their information as the definitions.
teams = {}
#team_names is a list containing the names of the teams.
team_names = []
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
        requested_team_name = input('Input team name: ')
        team_info = input('Enter team information: ')
        teams[int(requested_team)] = team_info
        team_names.append(requested_team_name)
        uncontinue = input("Would you like to add another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Remove team':
        print(teams.keys())
        print(team_names)
        requested_team = int(input('Input team number: '))
        requested_team_name = str(input('Enter team name: '))
        if requested_team in teams:
            teams.pop(requested_team)
            team_names.remove(requested_team_name)
        else:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to remove another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'
        
    while request == 'View team information':
        requested_team = int(input('Input team number: '))
        if requested_team in teams:
            print(teams[requested_team])
        else:
            print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to view another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Modify team information':
        print(teams.keys())
        requested_team = int(input("What team's information would you like to edit? Enter the team number, not name: "))
        if requested_team in teams:
            team_info = input(teams[requested_team] + 'Edit here. You will have to copy all the information shown above and make changes while typing, or untyped information will be lost: ')
            teams.pop(requested_team)
            teams[requested_team] = team_info
        elif requested_team not in teams:
        	print('Team not found. Try another team or make sure you entered the team number correctly.')
        uncontinue = input("Would you like to modify another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'

    while request == 'Search for team':
        wanted_action = input("Would you like to search by team number or name? Enter 'number' or 'name': ")
        if wanted_action == 'number':
            requested_team = int(input("Which team would you like to confirm is in our database?: "))
            if requested_team in teams:
                print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
            else:
                print('Team not found. Please search for another team.')
        if wanted_action == 'name':
            requested_team = input("Which team would you like to confirm is in our database?: ")
            if requested_team in team_names:
                print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
            else:
                print('Team not found. Please search for another team.')
        uncontinue = input("Would you like to search for another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'Done'