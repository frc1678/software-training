import ch_1_assign_Arthur_Zarins_
# Reminder for self: to run python programs in Visual Studio code, use Cntrl + Fn + F5
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
def add(team):
    if is_number(team) == True:
        ch_1_assign_Arthur_Zarins_.teams.update({str(team): {"name": "",
                                      "language": "",
                                      "width": "",
                                      "length": "",
                                      "motors": "",
                                      "cameraVision": False
                                      }})
        print("Team " + str(team) + " added successfully.\n     ")
    else:
        print("Team name must be a number")

def update(team, stat, updateTxt):
    if search(team) == True:
        ch_1_assign_Arthur_Zarins_.teams[team].update({str(stat): str(updateTxt)})
        print("Successfully updated an attribute of " + team)

def remove(team):
    if(search(team)):
        ch_1_assign_Arthur_Zarins_.teams.pop(str(team), None)

def search(team):
    if(str(team) in ch_1_assign_Arthur_Zarins_.teams):
        print("Team " + team + " exists")
        return True
    else:
        print("Error: team " + team + " does not exist")
        return False

def listTeams():
    teamList = []
    for i in ch_1_assign_Arthur_Zarins_.teams.keys():
        teamList.append(i)
    print("All teams: ")
    print(teamList)

def teamStats(team):
    if(search(team)):
        print("Stats for team " + team + ":")
        print(ch_1_assign_Arthur_Zarins_.teams[team])
# Now we can ask questions

def runContinuous():
    while True:
        # constant prompt
        function = input(
            "HOME. Type one of the following commands: 1)add 2)update 3)remove 4)search 5)listTeams 6)teamStats\n        ")
        if function == "add":
            # Adds a new team to the database
            a1 = input(
                "What is the team number? This is how the team will be referred to. WARNING: DUPLICATE TEAM NAME OVERWRITES OLD DATA\n    ")
            add(str(a1))
        elif function == "update":
            # Updates a team attribute
            a1 = input("What is the team number?\n    ")
            a2 = input(
                "What is the team attribute? (name/motors/cameraVision/language/width/length)\n    ")
            a3 = input("What is the team attribute NEW value?\n     ")
            update(a1, a2, a3)
        elif function == "remove":
            # Removes a team
            a1 = input("What is the team number?\n      ")
            remove(a1)
        elif function == "search":
            # States if a team exists
            a1 = input("What is the team number?\n      ")
            search(a1)
        elif function == "listTeams":
            # State all existing teams
            listTeams()
        elif function == "teamStats":
            # States the stats for the team, specifically the attributes
            a1 = input("What is the team number?\n      ")
            teamStats(a1)
