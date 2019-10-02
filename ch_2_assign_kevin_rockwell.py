teams = {} 

def get_team_num():
    print("Enter team number or 'c' to cancel")
    while True:
        team_num = input("Team Number: ")
        if team_num.isdigit():
            return int(team_num)
        elif team_num.lower() == "c":
            return ""
        else:
            print(f"Invalid Team Number {team_num}")

def get_vision():
    while True: #Limit Vision to True or False 
        vision = input("Team Has Vision System [True/False]: ").lower()
        if vision == "t" or vision == "true":
            return True
        elif vision == "f" or vision == "false":
            return False
        elif vision == "":
            return ""
        else:
            print(f"Invalid Value {vision}, expected True or False")

def get_drivetrain_motors():
    while True: #Limit Number of motors to int
        motors = input("Number of Drivetrain Motors (Integer): ")
        if motors.isdigit():
            return int(motors)
        elif motors == "":
            return ""
        else:
            print(f"Invalid Motor Number {motors}")

def get_input(prompt):
    """Takes input, returns None for Blank String"""
    response = input(prompt)
    if response != "":
        return response
    else:
        return None

def print_team(team_num, team):
    print(f"Team {team_num} - {team['name']}\n") #Print Number - Name
    print(f"Programming Language: {team['lang']}")
    print(f"Robot Length: {team['length']}")
    print(f"Robot Width: {team['width']}")
    print(f"Has Vision System: {team['vision']}")
    print(f"Number of Drivetrain Motors: {team['motors']}")

def get_team_data():
    temp_team = {} #Store unentered values as blank string 
    print("Input team data, enter blank line to skip data point")
    #Store Unknowns as None using get_input
    temp_team["name"] = get_input("Team name:\n")
    temp_team["lang"] = get_input("Programming Language: ") 

    #Keep dimensions as str to allow arbitrary dimensions 
    temp_team["width"] = get_input("Robot Width: ")
    temp_team["length"] = get_input("Robot Length: ")

    temp_team["vision"] = get_vision()
    temp_team["motors"] = get_drivetrain_motors()
    return temp_team

while True:
    #Print main menu
    print("""
        Allowed Actions:
        (a)dd Team
        (v)iew team data
        (m)odify team data
        (r)emove team
        (s)earch for teams
        (l)ist all teams
        (e)xit
        """)
    selection = ""
    selection = input("Action: ")
    if selection == "a": #Add team
        team_num = get_team_num()
        if team_num == "": #User canceled add operation
            continue #Go back into main menu loop
        
        temp_team = get_team_data()
        
        while True: #Confirm before saving
            save = input(f"Save team {team_num}? [Y/n]").lower() 
            if save == "y" or save == "":
                teams[team_num] = temp_team
                break
            elif save == "n":
                break

    elif selection == "v": #View team
        team_num = get_team_num()
        print_team(team_num, teams[team_num])

    elif selection == "m": #modify team
        team_num = get_team_num()
        if team_num not in teams.keys():
            print(f"Team Number {team_num} not stored.")
            continue
        print(f"Modifying team {team_num}")
        while True: #Confirm before saving
            save = input(f"Edit team {team_num}? [Y/n]").lower() 
            if save == "y" or save == "":
                teams[team_num] = get_team_data()
                break
            elif save == "n":
                break

    elif selection == "r": #remove team
        team_num = get_team_num()
        if team_num != "":
            if team_num in teams.keys():
                del teams[int(team_num)]
            else:
                print(f"Invalid Team Number {team_num}")
        else:
            continue #user canceled, so return to main menu

    elif selection == "s": #search for teams
        search_str = input("Search for team by name or number: ")
        matches = []
        if search_str.isdigit():
            for team, dat in teams.items():
                if str(team).startswith(search_str): #if start if numbers match
                    matches.append(f"{team}: {dat['name']}") #number + name
        else:
            for team, dat in teams.items():
                if dat["name"].startswith(search_str): #if start of name match
                    matches.append(f"{team}: {dat['name']}")  #num + name

        if matches != []:
            print(f"Matches to {search_str}")
            for m in matches:
                print(m)
        else:
            print(f"No matches for {search_str}")

    elif selection == "l": #list teams
        if len(teams.keys()) < 1:
            print("No stored teams")
            continue
        print("Stored Teams:")
        temp_ls = [] #used to store numbers temporarily to print nicer
        for team in teams.keys():
            if len(temp_ls) < 4: #print 4 numbers per line
                temp_ls.append(str(team))
            else:
                print(" ".join(temp_ls)) 
                temp_ls = [str(team)]
        else:
            print(" ".join(temp_ls))

    elif selection == "e": #exit program
        break

    else:
        print(f"Invalid Action: {selection}\n")