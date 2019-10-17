def isfloat(userInput):
    if isinstance(userInput, float) or isinstance(userInput, int) or userInput.isnumeric():
        return True
    elif not isinstance(userInput, str):
        return False
    elif "." not in userInput:
        return False
    else:
        userInput = userInput.split(".")
        if len(userInput) > 2:
            return False
        else:
            if userInput[0].isnumeric() and userInput[1].isnumeric():
                return True
            else:
                return False

def getTeam(userTeam,teams):
    if userTeam.isnumeric():
        userTeam = int(userTeam)
        for team in teams:
            if team.number == userTeam:
                return team
        return False
    else:
        for team in teams:
            if team.name == userTeam:
                return team
        return False

def isbool(userInput):
    userInput = userInput.lower()
    if userInput == "true":
        return True
    elif userInput =="false":
        return False
    return None

def isTeam(teams, userTeam):
    if userTeam.isnumeric():
        userTeam = int(userTeam)
        for team in teams:
            if userTeam == team.number:
                return str(team)
        return "\nTeam not in entered teams"

    else:
        for team in teams:
            if userTeam == team.name:
                return str(team)
        return "\nTeam not in entered teams"

def isValidUserInput(newTeam):
    return (newTeam[1]).isnumeric() and (newTeam[3]).isnumeric() and newTeam[4].lower() in ["true","false"]
#this function essentially just takes a list and if it is empty it makes the list into one with a string of "None", otherwise it returns the original list. I did this because I was having to check if some lists were empty, and if they were make them into something like "No competitions"
def emptyList(user_list):
    if len(user_list) == 0:
        return ["None"]
    else:
        return user_list
