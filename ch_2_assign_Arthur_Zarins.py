#Reminder for self: to run python programs in Visual Studio code, use Cntrl + Fn + F5
teams = {}
def add(team):
    teams.update({str(team):{"name": "",
    "language": "",
    "width": "",
    "length": "",
    "motors": "",
    "cameraVision": False
    }})
def update(team, stat, updateTxt):
    if search(team) == True:
        teams[team].update({str(stat): str(updateTxt)})
        print("Successfully updated an attribute of " + team)
def remove(team):
    if(search(team)):
        teams.pop(str(team), None)
def search(team):
    if(str(team) in teams):
        print("Team " + team + " exists")
        return True
    else:
        print("Error: team " + team + " does not exist")
        return False
def listTeams():
    teamList = []
    for i in teams.keys():
        teamList.append(i)
    print("All teams: ")
    print(teamList)
def teamStats(team):
    if(search(team)):
        print("Stats for team " + team + ":")
        print(teams[team])
#Now we can ask questions
while True:
    #constant prompt
    function = input("HOME. Type one of the following commands: 1)add 2)update 3)remove 4)search 5)listTeams 6)teamStats\n        ")
    if function == "add":
        #Adds a new team to the database
        a1 = input("What is the team number? This is how the team will be referred to. WARNING: DUPLICATE TEAM NAME OVERWRITES OLD DATA\n    ")
        add(str(a1))
        print("Team " + a1 + " added successfully.\n     ")
    elif function == "update":
        #Updates a team attribute
        a1 = input("What is the team number?\n    ")
        a2 = input("What is the team attribute? (name/motors/cameraVision/language/width/length)\n    ")
        a3 = input("What is the team attribute NEW value?\n     ")
        update(a1, a2, a3)
    elif function == "remove":
        #Removes a team
        a1 = input("What is the team number?\n      ")
        remove(a1)
    elif function == "search":
        #States if a team exists
        a1 = input("What is the team number?\n      ")
        search(a1)
    elif function == "listTeams":
        #State all existing teams
        listTeams()
    elif function == "teamStats":
        #States the stats for the team, specifically the attributes
        a1 = input("What is the team number?\n      ")
        teamStats(a1)