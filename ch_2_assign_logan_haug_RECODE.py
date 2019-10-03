teams = {
    (1678,"Citrus Circuits"): {
        "Number": 1678,
        "Name": "Citrus Circuits",
        "Programming Language": "Idk",
        "Team Width": 0.0,
        "Team Length": 0.0,
        "Drivetrain Motors": 0,
        "Camera System": True
    }
}
#This function validates user input. It takes a characteristic to compare the user input to, the team to compare it to, and then the dictionary of "teams"
def validateInput(userTeam,characteristic,userInput,teams):
    if isinstance((teams[userTeam][characteristic]), bool):
        if userInput == "True":
            return True
        elif userInput == "False":
            return False
        else:
            return None
    elif isinstance((teams[userTeam][characteristic]), int):
        if userInput.isnumeric():
            return round(int(userInput))
        else:
            return None
    elif isinstance((teams[userTeam][characteristic]), float):
        try:
            userInput = float(userInput)
            return float(userInput)
        except:
            return None
    elif isinstance((teams[userTeam][characteristic]), str):
        return userInput
#this function validates whether the user's team that they inputed is in the teams dictionary
def validateTeam(userTeam,teamsDict):
    for team in teamsDict:
        if userTeam in team:
            return team
    return False
#the while true loop is the actual pit viewer.
#I did this because I didn't want the user to mistype a feature and the program to stop because of that. I added a quit feature instead
while True:
    userFunc = input("Choose an operation (for operations type 'operations'): ")

    if userFunc == 'operations':
        print("Accceptable operations are: 'list','view','add','modify','remove','quit'")

    elif userFunc == 'list':
        print(teams)
#view feature: asks for a user team, checks if the input can be turned into an number if it can the team is cast into an integer,
#then validateTeam is run, and if the output is not false it prints the team
    elif userFunc == 'view':
        userTeam = input("team: ")
        if userTeam.isnumeric():
            userTeam = int(userTeam)
            if validateTeam(userTeam,teams) == False:
                print("Team is not in the dictionary, try entering it with 'add'")
            else: print(teams[validateTeam(userTeam,teams)])
        elif userTeam == "return": pass
        elif validateTeam(userTeam,teams) != False:
            print(teams[validateTeam(userTeam,teams)])
        else:
            print("Team is not in the dictionary, try entering it with 'add'")
    elif userFunc == "add":
        userInputs = []
        question = 0
        notstop = True
        for question in teams[(1678,"Citrus Circuits")].keys():
            userInput = input("Enter the new teams " + question + ": ")
            if userInput == "return":
                notstop = False
                break
            userInput = validateInput((1678,"Citrus Circuits"),question,userInput,teams)
            if userInput != None:
                userInputs.append(userInput)
            else:
                print("try again")
                notstop = False
                break
        if notstop:
            teams[(userInputs[0],userInputs[1])] = {
            "Number": userInputs[0],
            "Name": userInputs[1],
            "Programming Language": userInputs[2],
            "Team Width": userInputs[3],
            "Team Length": userInputs[4],
            "Drivetrain Motors": userInputs[5],
            "Camera System": userInputs[6]
            }
#I don't really know how to do this better, but I know that the notstop variable is really awful
#my plan was for the user to enter the team, then the code would validate the team, then for the user to enter a characteristic to modify, then the code would verify that
#then I would ask for the new data and then verify that, however I also wanted the program to print something like 'try again' until the user entered return or the a correct
#input
#This solution does that, but with repeated gross code.
#One issue with this solution is that it assumes that there is a citrus circuits team within the dictionary,
#so if it were to be deleted the add and modify functions wouldnt work
#this also goes for the add function.
    elif userFunc == "modify":
        characteristics = teams[(1678,"Citrus Circuits")].keys()
        notstop = True
        while notstop:
            userTeam = input("Enter a Team: ")
            if userTeam == "return":
                notstop = False
                break
            elif userTeam.isnumeric():
                userTeam = int(userTeam)
            userTeam = validateTeam(userTeam,teams)
            if userTeam == False:
                print("try again")
            else:
                break
        while notstop:
            userCharac = input("Which Characteristic to modify?: ")
            if userCharac == "return":
                notstop = False
                break
            elif userCharac not in characteristics:
                print("Please Try again")
            else:
                break
        while notstop:
            userData = input("Enter the new data: ")
            if userData == "return":
                notstop = False
                break
            userData = validateInput(userTeam,userCharac,userData,teams)
            if userData == None:
                print("try again")
            else:
                teams[userTeam][userCharac] = userData
                break
#This feature essentially just verifies the user team and then deletes it from the teams dictionary. Again using a while True loop so that a user can enter many wrong teams
    elif userFunc == "remove":
        while True:
            userTeam = input("Enter a Team: ")
            if userTeam == "return":
                break
            elif userTeam.isnumeric:
                userTeam = int(userTeam)
            userTeam = validateTeam(userTeam,teams)
            if userTeam == False:
                print("try again")
            else:
                del teams[userTeam]
                break
#aforementions quit feature, also congratulations you made it through my awful code.
    elif userFunc == "quit":
        break
