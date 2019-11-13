master_dictionary = {} #Setting up the master el dictionario
input_list = ['menu', 'view', 'remove', 'search', 'modify']
statistic_list = ['nm', 'tm', 'pl', 'w', 'l', 'cv', 'dt']
#Translating user inputs into functions

def remove_function():
    while True: #Idiotproofing code
        removal = input("Which team would you like to remove? This action cannot be undone! You may also quit at any time by pressing q. ")
        if removal == 'q':
            break
        elif ("statistics" + removal) in master_dictionary:
            master_dictionary[removal] = {}
            break
        else:
            print("Enter a valid input!")

def view_function():
    if master_dictionary == {}:
        print("You don't have any stored data.")
        return None
    while True:
        viewing_selection = input("""Which team's statistics would you like to view?
            You may also quit at any time by pressing q. """)
        if ("statistics" + str(viewing_selection)) in master_dictionary:
            break
        elif viewing_selection == 'q':
            print("Returning to main menu.")
            return None
        else:
            print("That isn't a team.")
    while True:
        statistic_selection = input("""Which statistic would you like to view? Please type one of
tm (team number), nm (name), pl (programming language), w or l (width or a length for your robot), 
cv (whether or not your robot has a camera vision system),or dt (the number of drivetrain motors on your robot). 
Again, you can quit with 'q'. """)
        if statistic_selection == 'q':
            print("Returning to main menu.")
            break
        elif statistic_selection in statistic_list and master_dictionary["statistics" + viewing_selection][statistic_selection] != '':
            print (master_dictionary["statistics" + viewing_selection][statistic_selection])
            break
        elif master_dictionary["statistics" + viewing_selection][statistic_selection] == '':
            print("That hasn't been added yet. Try something else.")
            break

def search_teams(): #Searching teams
    while True:
        team_search = input("What team would you like to search for? You may also quit at any time by pressing q. ")
        if team_search == 'q':
            print("Returning to main menu.")
            return None
        if not team_search.isdigit(): #If the search is all digits
            print("Oops, enter a valid input!")
            continue
        else:
            break
    for search in master_dictionary: #Checking every master_dict key to see if it's equal to the search
        if search == ("statistics" + team_search):
            return ("A match has been found!")
    return ("No matches were found.")

def add_team(): #How to add a new team
    print("You are adding a new file. The first step is to name your team. You may also quit at any time by pressing q. ")
    while True:
        team_number = input("What would you like your team to be named? Make sure it's all numbers! ") #Getting a name for the team
        team_name = input("How about your team's name? ")
        if team_number == 'q' or team_name == 'q':
            print("Returning to the main menu. ")
            break
        elif team_number.isdigit() == False: #Checking if a team name is all digits
            print("Valid input, please!")
            continue
        else:
            master_dictionary["statistics" + str(team_number)] = {} #Making a dictionary entry for the team
            for yeet in statistic_list:
                master_dictionary["statistics" + str(team_number)][yeet] = ''
            master_dictionary["statistics" + str(team_number)]['nm'] = team_name
            break

def add_statistic(): #How to add a statistic for a team
    team_name = '' #Setting variables empty
    datapoint = ''
    while True:
        team_name = input("""Please select a team whose information you would like to modify. 
You may also quit at any time by pressing q. """) #Finding the team
        if ("statistics" + str(team_name)) in master_dictionary:
            break
    while True:
        statistic_added = input("""You may add a team number (tm), change the name (nm), add a programming language (pl),
        a width or a length for your robot (w or l), whether or not your robot has a camera vision system (cv),
        and the number of drivetrain motors on your robot (dt). Which one of these options would you like
        to edit? Enter your options as the parenthetical after the option you have selected. """) #Note the shorthands like 'pl' here.
        if statistic_added == 'q':
            return None
        elif statistic_added in statistic_list:
                datapoint = (input("What would you like to set this team's " + statistic_added + " to?"))
                if statistic_added == 'w' or 'l':
                    if not datapoint.isnum():
                        continue
                elif statistic_added == 'cv':
                    if datapoint not in ['yes', 'no', 'True', 'False']:
                        continue
                elif statistic_added == 'dt':
                    if not datapoint.isnum():
                        continue
                else:
                    continue
                master_dictionary["statistics" + str(team_name)][statistic_added] = datapoint
                return None
        else:
            continue

while True: #Mainloop
    menu_selection = input("""Type 'view' to view, 
        'remove' to remove, 'search' to search the teams, 'add' to add a team, or
        'statistic' to add a statistic to a team's file. 
        Or type 'stop' to end this program. """)
    if menu_selection == 'view':
        valid_input_5 = True
        view_function()
    elif menu_selection == 'remove':
        valid_input_5 = True
        remove_function()
    elif menu_selection == 'search':
        valid_input_5 = True
        print(search_teams())
    elif menu_selection == 'add':
        valid_input_5 = True
        add_team()
    elif menu_selection == 'statistic':
        if master_dictionary != {}:
            valid_input_5 = True
            add_statistic()
        else:
            print("You don't have any teams! Darn it!")
            continue
    elif menu_selection == 'stop':
        break
    else:
        print('Enter a valid input! ')
        continue