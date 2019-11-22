teams = {}
def add():
    check = False
    while check == False:
        number = input("What is the team number ")
        width = input("What is the width of the robot? ")
        length = input("What is the length of the robot? ")
        nummotors = input("How many motors does the robot have? ")
        rookie_year = input("What year is the rookie year?")

        if number.isdigit() and width.isdigit() and length.isdigit() and nummotors.isdigit() and rookie_year.isdigit():
            check == True    
        else:
          continue
        team_name = input("What is the team name? ")
        competed_in_2019 = input("Did the team compete in 2019?")
        programming_language = input("What programming language does the team use? ")
        vision = input("Does the robot have a vision system? True or False: ")
        awards = input("What awards have been earned?")
        location = input("Where is the team located?")
        competition_names = input("What are the names of the competitions that the team went to?")         
        attributes_of_team = {"Number": number,
                              "Name": team_name,
                              "Programming_language": programming_language,
                              "Width" : width,
                              "Length": length,
                              "Vision system": vision,
                              "Number of Motors" : nummotors,
                              "Awards" : awards,
                              "Location" : location,
                              "Rookie year" : rookie_year,
                              "Competed last year" : competed_in_2019,
                              "Competition names" : competition_names }
        teamsnew = {int(number): attributes_of_team}
        teams.update(teamsnew)
        check = True
def remove():
    print(teams)
    int_remove = int(input("What team number do you want to remove? "))
    teams.pop(int_remove)
    print(teams)
        
def list_all_teams():
        print(teams)
       
def edit():
   team_number = int(input("What team do you want to edit? (Use team number)"))
   add()             
   teams.pop(team_number)
   print(teams)
def search():
    team_number = int(input("What is the team number? "))
    team_attribute = input("What is the team attribute? ")
    print(teams[team_number] [team_attribute])
    
while True:
    command = input("""Type 'add' to add a team
Type 'remove' to remove a team
Type 'edit' to change a teams data
Type 'search' to search for a team
Type 'list all teams' to display all teams
Type 'quit' to exit
                   """)
    if command == "add":
        add()
    if command == "remove":
        remove()
    if command == "edit":
        edit()
    if command == "search":
        search()
    if command == "list all teams":
        list_all_teams()
    if command == "quit":
        break
