teams = {}
allowed_actions = [
    'Add team',
    'Remove team',
    'View team information',
    'Modify team information',
    'Search for team',
    ]
on = True
def mainMenu():
    print(allowed_actions)
def addTeam():
    requested_team = input('Input team number: ')
    if requested_team in teams:
        print('This team is already in the system. Please add a different team, confirm you have entered the team number correctly, or edit the information already existing in this team.')
    else:
        location = input('What is the location of the team?: ')
        rookie_year = input('What is their rookie year?: ')
        competed_in_2019 = input('Did they compete in the 2019 competitions?: ')
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
    requested_team = input('Input team number: ')
    if requested_team in teams:
        teams.pop(requested_team)
    else:
        print('Team not found. Try another team or make sure you entered the team number correctly.')

def viewTeam():
    print(teams.keys())
    requested_team = input('Input team number: ')
    if requested_team in teams:
        print(teams[requested_team])
    else:
        print('Team not found. Try another team or make sure you entered the team number correctly.')

def modifyTeam():
    print(teams.keys())
    requested_team = input("What team's information would you like to edit?: ")
    if requested_team in teams:
        change = input("What would you like to change for this team? Enter 'Location' 'Rookie Year' 'Competed in 2019 Competitions' 'Competition Names' 'Competition Locations' 'Awards Won': ")
        if change == 'Location':
            location = input('Where is the team located?: ')
            teams[requested_team].pop('Location')
            teams[requested_team]['Location'] = location
        if change == 'Rookie Year':
            rookie_year = input('What is their rookie year?: ')
            teams[requested_team].pop('Rookie Year')
            teams[requested_team]['Rookie Year'] = rookie_year
        if change == 'Competed in 2019 Competitions':
            competed_in_2019 = input('Did they compete in the 2019 Competitions?: ')
            teams[requested_team].pop('Competed in 2019 Competitions')
            teams[requested_team]['Competed in 2019 Competitions'] = competed_in_2019
        if change == 'Competition Names':
            competitions = input('What are the names of the competitions they participated in?: ')
            teams[requested_team].pop('Competition Names')
            teams[requested_team]['Competition Names'] = competitions
        if change == 'Competition Locations':
            locations_of_competitions = input('Where were the competitions they participated in?: ')
            teams[requested_team].pop('Competition Locations')
            teams[requested_team]['Competition Locations'] = locations_of_competitions
        if change == 'Awards Won':
            awards_won = input('What awards did they win?: ')
            teams[requested_team].pop('Awards Won')
            teams[requested_team]['Awards Won'] = awards_won
    elif requested_team not in teams:
        print('Team not found. Try another team or make sure you entered the team number correctly.')

def searchTeam():
    requested_team = input("Which team would you like to confirm is in our database?: ")
    if requested_team in teams:
        print("Requested team is in database. You can view its information using command 'View team information' and entering the team number again.")
    if requested_team not in teams:
        print('Requested team is not in our database. Make sure you entered it correctly or search for another team.')
while on:
    mainMenu()
    request = input('What would you like to do? Please enter exactly as shown: ')
    while request == 'Add team':
        addTeam()
        uncontinue = input("Would you like to add another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'No'
        else:
            request = 'Add team'
    while request == 'Remove team':
        removeTeam()
        uncontinue = input("Would you like to remove another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'No'
        else:
            request = 'Remove team'
    while request == 'View team information':
        viewTeam()
        uncontinue = input("Would you like to view another team's information? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'No'
        else:
            request = 'View team information'
    while request == 'Modify team information':
        modifyTeam()
        uncontinue = input("Would you like to modify another team's information? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'No'
        else:
            request = 'Modify team information'
    while request == 'Search for team':
        searchTeam()
        uncontinue = input("Would you like to search for another team? Enter 'Yes' 'No': ")
        if uncontinue == 'No':
            request = 'No'
        else:
            request = 'Search for team'