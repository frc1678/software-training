teams = {1678:[1678,"Citrus Circuits","Idk",10,10,"Yes",10]}
name_to_number = {"Citrus Circuits": 1678}
def verifyview(dict,dict2,user):
    if user.isnumeric():
        if int(user) in dict: return dict[int(user)]
        else: return False
    elif user in dict2: return dict[dict2[user]]
    elif user == "return": return "quit"
    else: return False
while True:
    useraction = input("\nPlease select action. For actions type 'actions': ")
    if useraction == "actions": print("Available actions are: 'actions', 'view', 'modify', 'remove', 'list', 'add', 'quit'")
    elif useraction == "list": print(teams)
    elif useraction == "view":
        while True:
            Team = input("enter the team to view: ")
            display = verifyview(teams,name_to_number,Team)
            if display == "quit": break
            elif  display != False:
                print(display)
                break
    elif useraction == "modify":
        while True:
            Team = input("enter the team to modify: ")
            display = verifyview(teams,name_to_number,Team)
            if display == "quit": break
            elif display != False:
                userNumber = input("enter the new team number: ")
                if userNumber == "return": break
                elif userNumber.isnumeric():
                    userNumber = int(userNumber)
                    userName = input("enter the new team name: ")
                    if userName == "return": break
                    else:
                        userProgLang = input("enter the new team Programming Language: ")
                        if userProgLang == "return": break
                        else:
                            userWidth = input("enter the new team's width (of robot maybe?): ")
                            if userWidth == "return": break
                            elif userWidth.isnumeric():
                                userLength = input("enter the new team's length (of robot maybe?): ")
                                if userLength == "return": break
                                elif userLength.isnumeric():
                                    userCamera = input("enter if the team has a camera system: ")
                                    if userCamera == "return": break
                                    else:
                                        userDrive = input("enter number of Drivetrain motors: ")
                                        if userDrive == "return": break
                                        elif userDrive.isnumeric():
                                            teams[int(userNumber)] = [int(userNumber),userName,userProgLang,float(userWidth),float(userLength),userCamera,int(userDrive)]
                                            name_to_number[userName] = int(userNumber)
                                            print("successfully changed")
                                            break
    elif useraction == "add":
        while True:
            userNumber = input("enter the new team number: ")
            if userNumber == "return": break
            elif userNumber.isnumeric():
                userNumber = int(userNumber)
                userName = input("enter the new team name: ")
                if userName == "return": break
                else:
                    userProgLang = input("enter the new team Programming Language: ")
                    if userProgLang == "return": break
                    else:
                        userWidth = input("enter the new team's width (of robot maybe?): ")
                        if userWidth == "return": break
                        elif userWidth.isnumeric():
                            userWidth = float(userWidth)
                            userLength = input("enter the new team's length (of robot maybe?): ")
                            if userLength == "return": break
                            elif userLength.isnumeric():
                                userLength = float(userLength)
                                userCamera = input("enter if the team has a camera system: ")
                                if userCamera == "return": break
                                else:
                                    userDrive = input("enter number of Drivetrain motors: ")
                                    if userDrive == "return": break
                                    elif userDrive.isnumeric():
                                        userDrive = int(userDrive)
                                        name_to_number[userName] = userNumber
                                        teams[userNumber] = [userNumber,userName,userProgLang,userWidth,userLength,userCamera,userDrive]
                                        print("successfully added")
                                        break
                                    else: print("try again")
                            else: print("try again")
                        else: print("try again")
            else: print("try again")
    elif useraction == "remove":
        while True:
            Team = input("enter the team to delete: ")
            if Team == "return": break
            elif Team.isnumeric():
                if int(Team) in teams:
                    Team = int(Team)
                    del teams[Team]
                    print("successfully deleted")
                    break
                else: print("Attempt to delete failed")
            elif Team in name_to_number:
                del teams[name_to_number[Team]]
                print("successfully deleted")
                break
            else: print('Attempt to delete failed')
    elif useraction == "quit": break
