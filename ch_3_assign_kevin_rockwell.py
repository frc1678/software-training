teams = {}

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
    comps = {}
    while True:
        if comps == {}: # No comps have been, so add
            print("Add competition?")
        else: # Comps have been added, so add another comp
            print("Add another competition?")
        if not get_bool(): #User does not want to add more competitions
            return comps

        name = input_or_cancel("Input Competition Name or 'q' to cancel:\n")
        if name is None:
            continue
        elif name in comps:
            print(f"Competition {name} already in list")
            continue

        location = input_or_cancel("Input Location or 'q' to cancel:\n")
        if location is None:
            continue
        comps[name] = location

def print_team(team, team_num):
    print(f"Team Number {team_num}")
    for a in attributes:
        value = team.get(a)
        if value is not None:
            if a == "2019_comps":
                print(a + ":")
                if value == {}:
                    print(f"No stored competitions for {team_num}")
                    continue
                for comp, location in value.items():
                    print(f"{comp} in {location}")
                continue
            print(f"{a}: {value}")
        else:
            print(f"{a} is unknown for team {team_num}")

attributes = [
    "location", 
    "rookie_year", 
    "competed_2019", 
    "2019_comps", 
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
            + " 'q' if unknown: ") # None for unknowns 
        print("Enter team rookie year")
        temp_team["rookie_year"] = get_positive_int()
        print("Enter if team competed in 2019")
        temp_team["competed_2019"] = get_bool()
        temp_team["2019_comps"] = get_comps()
        temp_team["2019_awards"] = input_or_cancel("Enter 2019 awards or"
            + " 'q' if unknown\n")

        print(f"Save team {team_num}")
        if get_bool():
            teams[team_num] = temp_team

    elif selection == "v": #View team
        print("Input team number: ")
        team_num = get_positive_int()
        if team_num not in teams:
            print(f"Team Number {team_num} not stored.")
            continue
        elif team_num == None:
            continue
        print_team(teams[team_num], team_num)

    elif selection == "m": #modify team
        print("Input team number:")
        team_num = get_positive_int()
        if team_num is None:
            continue
        elif team_num not in teams:
            print(f"Team number {team_num} not stored.")
            continue
        print("Current Values:")
        print_team(teams[team_num], team_num) #Show current values
        print("""
            Attribute to change:
            (l)ocation
            (r)ookie year
            (c)ompetitions in 2019
            (i)f the team competed in 2019
            (a)wards won in 2019
            """)
        while True:
            i = input_or_cancel("Select attribute or 'q' to cancel: ")
            if i in ["l", "r", "c", "i", "a", None]:
                break
            else:
                print("Invalid attribute selection.")
        if i == None:
            continue
        if i == "l": # Change location
            location = input_or_cancel("Enter updated location or 'q' to cancel: ")
            if location is not None:
                teams[team_num]["location"] = location
        elif i == "r": # Change rookie year
            rookie = input_or_cancel("Enter updated rookie year or 'q' to cancel: ")
            if rookie is not None:
                teams[team_num]["rookie_year"] = rookie
        elif i == "c": # Change 2019 competitions
            print("Please enter all 2019 competitions. Enter no competitions to cancel")
            comps = get_comps()
            if comps != {}:
                teams[team_num]["2019_comps"] = comps
        elif i == "i": # Change competed 2019
            print("Enter if team competed in 2019 or 'q' to cancel")
            comp_2019 = get_bool()
            if comp_2019 is not None:
                teams[team_num]["competed_2019"] = comp_2019
        elif i == "a":
            awards = input_or_cancel("Enter 2019 awards or 'q' to cancel")
            if awards is not None:
                teams[team_num]["2019_awards"] = awards

    elif selection == "r": #remove team
        print("Input team number:")
        team_num = get_positive_int()
        if team_num is None:
            continue
        elif team_num not in teams:
            print(f"Team Number {team_num} not stored.")
            continue

        print(f"Delete team {team_num}?")
        if get_bool():
            del teams[team_num]

    elif selection == "s": #search for teams
        print("Enter the start of or complete team number to search for:")
        search_team = get_positive_int()
        for t in teams:
            if str(t).startswith(str(search_team)):
                print(t)

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
        print("Confirm Exit:")
        if get_bool():
            break

    else:
        print(f"Invalid Action: {selection}\n")