from ch_1_assign_kevin_rockwell import teams

def input_or_cancel(prompt):
    i = input(prompt)
    if i == "q":
        return None
    else:
        return i

def get_positive_int():
    while True:
        i = input_or_cancel("Enter a positive integer or 'q' to cancel: ")
        if i is not None:
            if i.isdigit():
                return int(i)
            else:
                print(f"Invalid input {i}")
                continue
        return i # user canceled, so return none

def get_bool():
    while True:
        i = input_or_cancel("Please enter (y)es or (n)o: ")
        if i is not None:
            i = i.lower()
            if i in ["t", "true", "1", "y", "yes"]: # Accept more truthy values
                return True
            elif i in ["f", "false", "0", "n", "no"]: # Same but for falsey
                return False
            else:
                print(f"Invalid input {i}")
                continue
        return i # User canceled

def get_comps():
    new_comps = {}
    while True:
        if comps == {}:
            print("Add competition?")
        else:
            print("Add another competition?")
        if not get_bool(): #User does not want to add more competitions
            return comps

        name = input_or_cancel("Input Competition Name or 'q' to cancel:\n")
        if name is None:
            continue
        elif name in new_comps:
            print(f"Competition {name} already in list")
            continue

        location = input_or_cancel("Input Location or 'q' to cancel:\n")
        if location is None:
            continue
        comps[name] = location

attributes = [
    "location", 
    "rookie_year", 
    "competed_2019", 
    "2019_comps", 
    "comp_locations",
    "2019_awards",
    ]

while True:
    #Main Menu
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
        print("Enter team Number:")
        team_num = get_positive_int()
        if team_num in teams:
            print(f"Team Number {team_num} already in teams")
            continue
        elif team_num is None:
            continue #User canceled, so exit add team and return to main menu
        temp_team = {}
        temp_team["location"] = input_or_cancel("Input team location or" 
            + "'q' if unknown: ") # None for unknowns 
        print("Enter team rookie year")
        temp_team["rookie_year"] = get_positive_int()
        print("Enter if team competed in 2019")
        temp_team["competed_2019"] = get_bool()
        temp_team["2019_comps"] = get_comps()
        temp_team["2019_awards"] = input_or_cancel("Enter 2019 awards or"
            + "'q' if unknown")

        print(f"Save team {team_num}")
        if get_bool():
            teams[team_num] = temp_team

    elif selection == "v": #View team
        pass        

    elif selection == "m": #modify team
        pass

    elif selection == "r": #remove team
        pass

    elif selection == "s": #search for teams
        pass

    elif selection == "l": #list teams
        pass

    elif selection == "e": #exit program
        pass

    else:
        print(f"Invalid Action: {selection}\n")