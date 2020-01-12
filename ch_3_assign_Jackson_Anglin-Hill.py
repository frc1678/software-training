teams = {}
allowed_actions = [
    'Add team',
    'Remove team',
    'View team information',
    'Modify team information',
    'Search for team',
    'List all teams'
    ]

running = True
def mainMenu():
    print(allowed_actions)
def addTeam():
    while True:
        requested_team = input('Input team number: ')
        try:
            requested_team = int(requested_team)
            break
        except:
            print('Enter the team number without letters.')
    if requested_team in teams:
        print('This team is already in the system. Please add a different team, confirm you have entered the team number correctly, or edit the information already existing in this team.')
    else:
        location = input('What is the location of the team?: ')
        while True:
            rookie_year = input('What is their rookie year?: ')
            try:
                rookie_year = int(rookie_year)
                break
            except:
                print('Enter rookie year without letters.')
        while True:
            competed_in_2019 = input('Did they compete in the 2019 competitions?: ')
            try:
                competed_in_2019 = competed_in_2019.lower()
            except:
                print("Please enter 'Yes' or 'No'")
            if competed_in_2019 == 'yes':
                competed_in_2019 = True
                break
            elif competed_in_2019 == 'no':
                competed_in_2019 == False
                break
            else:
                print("Please enter 'Yes' or 'No'")
        competitions = input('If they did, what are the names of the competitions they participated in?: ')
        locations_of_competitions = input('If they did, what are the locations of the competitions they participated in?: ')
        awards_won = input('If they won any, what awards did they win?: ')
        teams[requested_team] = {}
        teams[requested_team]['Location'] = location
        teams[requested_team]['Rookie Year'] = rookie_year
        teams[requested_team]['Competed in 2019 Competitions'] = competed_in_2019
        teams[requested_team]['Competition Names'] = competitions
        teams[requested_team]['Competition Locations'] = locations_of_competitions
        teams[requested_team]['Awards Won'] = awards_won

def removeTeam():
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

def viewTeam():
    print(teams.keys())
    while True:
        requested_team = input('Input team number: ')
        try:
            requested_team = int(requested_team)
            break
        except:
            print('Enter team number without letters.')
    if requested_team in teams:
        print(teams[requested_team])
    else:
        print('Team not found. Try another team or make sure you entered the team number correctly.')

def modifyTeam():
    print(teams.keys())
    while True:
        requested_team = input('Input team number: ')
        try:
            requested_team = int(requested_team)
            break
        except:
            print('Enter team number without letters.')
    if requested_team in teams:
        change = input("What would you like to change for this team? Enter 'Location' 'Rookie Year' 'Competed in Competitions' 'Competition Names' 'Competition Locations' 'Awards Won': ")
        change = change.lower()
        if change == 'location':
            location = input('Where is the team located?: ')
            teams[requested_team]['Location'] = location
        elif change == 'rookie year':
            while True:
                rookie_year = input('What is their rookie year?: ')
                try:
                    rookie_year = int(rookie_year)
                    break
                except:
                    print('Enter rookie year without letters.')
            teams[requested_team]['Rookie Year'] = rookie_year
        elif change == 'competed in competitions':
            while True:
                competed_in_2019 = input('Did they compete in the 2019 competitions?: ')
                try:
                    competed_in_2019 = competed_in_2019.lower()
                except:
                    print("Please enter 'Yes' or 'No'")
                if competed_in_2019 == 'yes':
                    competed_in_2019 = True
                    break
                elif competed_in_2019 == 'no':
                    competed_in_2019 == False
                    break
                else:
                    print("Please enter 'Yes' or 'No'")
            teams[requested_team]['Competed in 2019 Competitions'] = competed_in_2019
        elif change == 'competition names':
            competitions = input('What are the names of the competitions they participated in?: ')
            teams[requested_team]['Competition Names'] = competitions
        elif change == 'competition locations':
            locations_of_competitions = input('Where were the competitions they participated in?: ')
            teams[requested_team]['Competition Locations'] = locations_of_competitions
        elif change == 'awards won':
            awards_won = input('What awards did they win?: ')
            teams[requested_team]['Awards Won'] = awards_won
    else:
        print('Team not found. Try another team or make sure you entered the team number correctly.')

def searchTeam():
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
def uncontinue():
        while True:  
            uncontinue = input("Would you like to repeat this action?: ")  
            if uncontinue.lower() == 'no':
                return True
            elif uncontinue.lower() == 'yes':
                return False
            else:
                return True
while running:
    mainMenu()
    request = input('What would you like to do?: ')
    request = request.lower()
    while request == 'add team':
        addTeam()
        if uncontinue():
            request = 'o'
    while request == 'remove team':
        removeTeam()
        if uncontinue():
            request = 'o'
    while request == 'view team information':
        viewTeam()
        if uncontinue():
            request = 'o'
    while request == 'modify team information':
        modifyTeam()
        if uncontinue():
            request = 'o'
    while request == 'search for team':
        searchTeam()
        if uncontinue():
            request = 'o'
    if request == 'list all teams':
        print(teams.keys())
        request = 'o'