master_dictionary = {} #Setting up the master el dictionario
input_list = ['menu', 'view', 'remove', 'search', 'modify']
statistic_list = ['tm', 'n', 'pl', 'w', 'l', 'cv', 'dt']
#Translating user inputs into functions

def remove_function():
    while True: #Idiotproofing code
        removal = input("Which team would you like to remove? This action cannot be undone!")
        if ("statistics" + removal) in master_dictionary:
            master_dictionary[removal] = {}
            break;

def view_function():
    while True:
        viewing_selection = input("Which team's statistics would you like to view? ")
        if "statistics" + str(viewing_selection) in master_dictionary:
            break;
    while True:
        statistic_selection = input("""Which statistic would you like to view? Please type one of
        tm (team number), n (name), pl (programming language), w or l (width or a length for your robot), 
        cv (whether or not your robot has a camera vision system),or dt (the number of drivetrain motors on your robot). """)
        if statistic_selection in statistic_list and master_dictionary["statistics" + viewing_selection][statistic_selection] != '':
            print (master_dictionary["statistics" + viewing_selection][statistic_selection])
            break;
        elif master_dictionary["statistics" + viewing_selection][statistic_selection] == '':
            print("That hasn't been added yet. Try something else.")
            break;

def search_teams(): #Searching teams
    while True:
        team_search = input("What team would you like to search for? ")
        if team_search.isdigit() == False: #If the search is all digits
            print("Oops, enter a valid input!")
            continue;
        else:
            break;
    for search in master_dictionary: #Checking every master_dict key to see if it's equal to the search
        if search == ("statistics" + team_search):
            return ("A match has been found!")
            break;
    return ("No matches were found.")

def add_team(): #How to add a new team
    print("You are adding a new file. The first step is to name your team.")
    while True:
        team_name = input("What would you like your team to be named? Make sure it's all numbers! ") #Getting a name for the team
        if team_name.isdigit() == False: #Checking if a team name is all digits
            print("Valid input, please!")
            continue;
        else:
            master_dictionary["statistics" + str(team_name)] = {} #Making a dictionary entry for the team
            for yeet in statistic_list:
                master_dictionary["statistics" + str(team_name)][yeet] = ''
            break;

def add_statistic(): #How to add a statistic for a team
    team_name = '' #Setting variables empty
    datapoint = ''
    while True:
        team_name = input("Please select a team whose information you would like to modify.") #Finding the team
        if ("statistics" + str(team_name)) in master_dictionary:
            break;
    while True:
        statistic_added = input("""You may add a team number (tm), a name (n), a programming language (pl),
        a width or a length for your robot (w or l), whether or not your robot has a camera vision system (cv),
        and the number of drivetrain motors on your robot (dt). Which one of these options would you like
        to edit? Enter your options as the parenthetical after the option you have selected. """) #Note the shorthands like 'pl' here.
        if statistic_added in statistic_list:
            break;
    for statistic_name in statistic_list: #For all possible statistic names
        if statistic_added == statistic_name: #If the statistic selected has been found:
            datapoint = (input("What would you like to set this team's " + statistic_added + "?")) #What data the user wants to add.
            master_dictionary["statistics" + str(team_name)][statistic_added] = datapoint

def menu_function():
    if master_dictionary == {}:
        valid_input = False
        while valid_input == False:
            first_input = input("You don't seem to have any data. Enter 'yes' to add some. ")
            if first_input == 'yes':
                modification_function()
                valid_input = True

while True:
    valid_input_5 = False
    while valid_input_5 == False:
        menu_selection = input("""Type 'view' to view, 
            'remove' to remove, 'search' to search the teams, 'add' to add a team, or
            'statistic' to add a statistic to a team's file. """)
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
                continue;