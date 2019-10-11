teams = {
    1678 : {
        "rookie year" : 2005,
        "location" : "Davis, California, USA",
        "compete in 2019" : True,
        "competitions and locations" : {
            "Central Valley Regional" : "Fresno, Ca, US",
            "Sacramento Reagional" : "Sacramento, CA, USA",
            "Aerospace Valley Regional" : "Lancaster, CA, USA",
            "Carver Division" : "Houston, TX, USA", 
            "Einstein Field" : "Houston, TX, USA"
        },
        "awards" : "CHAIRMAN'S AWARD, CENTRAL VALLEY REGIONAL WINNER, SACRAMENTO REGIONAL WINNER, AEROSPACE VALLEY REGIONAL WINNER",
    },
    1682 : {
        "rookie year" : 2005,
        "location" : "Riverside, California, USA",
        "compete in 2019" : False,
        "competitions" : "None",
        "competitions and locations" : {},
        "awards" : "None"
    },
    1690 : {
        "rookie year" : 2005,
        "location" : "Binyamina, HaZafon, Israel",
        "compete in 2019" : True,
        "competitions and locations" : {
            "ISR District Event #1" : "Haifa, HA 00000, Israel", 
            "ISR District Event #4" : "Tel Aviv-Yafo, TA 00000, Israel",
            "FIRST Israel District Championship" : "Tel Aviv-Yafo, TA 00000, Israel",
            "Darwin Division": "Detroit, MI, USA",
            "Indiana Robotics Invitational" : "Indianapolis, IN, USA;"
        },
        "awards" : "None",
    },
    1700 : {
        "rookie year" : 2005,
        "location" : "Palo Alto, California, USA",
        "compete in 2019" : True,
        "competitions and locations" : {
            "San Francisco Regionals" : "San Francisco, CA, USA", 
            "Utah Regionals" : "West Valley City, Utah, USA",
            "Turing Devision": "Houston, TX, USA"
        },
        "awards" : "None"
    },
    2907 : {
        "rookie year" : 2009,
        "location" : "Auburn, Washington, USA",
        "compete in 2019" : True,
        "competitions and locations" : {
            "PNW District Auburn Mountainview Event" : "Auburn, WA, USA",
            "NW District West Valley Event" : "Spokane, WA, USA",
            "PNW District Auburn Event" : "Auburn, WA, USA",
            "Pacific Northwest FIRST District Championship" : "Tacoma, WA, USA", 
            "Roebling Division" : "Houston, TX, USA", 
            "Einstein Field" : "Houston, TX, USA",
            "Peak Performance": "Sea Tac, WA, USA;"
        },
        "awards" : "None"
    },
    3132 : {
        "rookie year" : 2010,
        "location" : "Sydney, New South Wales, Australia",
        "compete in 2019" : True,
        "competitions and locations" : {
            "Southern Cross Regional" : "Sydney Olympic Park, NSW, Australia",
            "NSouth Pacific Regional" : "Sydney Olympic Park, NSW, Australia",
            "Carver Division" : "Houston, TX, USA",
            "Einstein Field" : "Houston, TX, USA",
            "Duel Down Under" : "Sydney, New South Wales, Australia;"
        },
        "awards" : "2019 SOUTHERN CROSS REGIONAL, 2019 CARVER DIVISION",
    },
}

team_aspects = ["rookie year", "location", "compete in 2019", "competitions and locations", "awards", "team number"]

#List of Function Operations:
#remove_team: removes a team
#modify_team: modifies an attribute of a team
#search_team: searches for an attribute of a team
#add_team: adds a team to the main teams dictionary
#comp_local: makes a seperate dictionary for the competitions and locations for a team
#list_team: lists the team #, or keys in the teams dictionary
#exit_program: leaves the program
#validate: validates input for add team function
#main_function: The "main menu" for the other operations


def remove_team():
    user_remove = int(input("What team do you want to remove? "))
    teams.pop(user_remove)

    main_function()

def modify_team():
    user_modify = int(input("What team do you want to modify? "))
    print("Options:")
    print(team_aspects)
    team_attribute_modify = input("What would you like to modify about the team? ")
    for team_aspect in team_aspects:
        if team_attribute_modify == team_aspect:
            new_attribute = input("What is the team's updated attribute? ")
            teams[user_modify][team_aspect] = new_attribute
            break
        elif team_attribute_modify == team_aspects[3]:
            teams[user_modify]["competitions and locations"] = comp_local()
            teams[user_modify]["compete in 2019"] = True
            break
        elif team_attribute_modify == team_aspects[2]:
            new_compete = input("Did the team compete in 2019? (y/n) ")
            if new_compete == "y":
                teams[user_modify][team_aspect[2]] = True
                comp_local_modify = input("Would you like to add competitions? (y/n) ")
                while True:
                    if comp_local_modify == "y":
                       teams[user_modify]["competitions and locations"] = comp_local()
                       break
                    elif comp_local_modify == "n":
                        teams[user_modify]["competitions and locations"] = "None"
                        break
                    else:
                        print("Unknown input, please input y or n")
                break
            elif new_compete == "n":
                teams[user_modify]["compete in 2019"] = False
                teams[user_modify][team_aspects[3]] = "None"
                break
    else:
        print("Input Unknown")
        modify_team()

    main_function()

def add_team():
    temp_team_dictionary = {}

    rookie = input("What is the rookie year for your team? ")
    location = input("What is your team's location? ")
    compete = input("Did your team compete in 2019? (yes/no) ")
    if compete == "yes":
        compete = True
        temp_team_dictionary["competitions and locations"] = comp_local()
    elif compete == "no":
        compete = False
        temp_team_dictionary["competitions and locations"] = ["None, didn't compete"]
    awards = input("What award did your team win? ")

    temp_team_dictionary["rookie year"] = rookie
    temp_team_dictionary["location"] = location
    temp_team_dictionary["compete in 2019"] = compete
    temp_team_dictionary["awards"] = awards

    team_number_input = input("Add a team number ")
    
    if team_number_input[0].isdigit():
        team_number_input = int(team_number_input)
        teams[team_number_input] = temp_team_dictionary
    
    else:
        print("Input wasn't a number, please enter a team number")
        team_number_input = int(input("Add a team number "))
        teams[team_number_input] = temp_team_dictionary

    validation(team_number_input)
    main_function()

def comp_local(comp_local_dict={}):
    comp_local_input = input("Would you like to add a competition and location? (y/n) ")

    while True:
        if comp_local_input == "y":
            comp = input("What competition did your team compete in? ")
            comp_location = input("Where was that competition? ")
            comp_local_dict[comp] = comp_location
            return comp_local(comp_local_dict)
        
        elif comp_local_input == "n":
            return comp_local_dict
        
        else:
            print("Unknown input. Please input y or n")

def validation(team_number_input):
    for data_field in ["rookie year"]:
        if teams[team_number_input][data_field].isdigit():
            teams[team_number_input][data_field] = int(teams[team_number_input][data_field])
        else:
            print("Input wasn't a number, please enter number for")
            print(data_field)
            teams[team_number_input][data_field] = int(input("Please enter the new answer "))
    for data_field in ["location", "awards"]:
        if teams[team_number_input][data_field].isdigit() == False:
            teams[team_number_input][data_field] = str(teams[team_number_input][data_field])
        else:
            print("Input was a number, please enter a word for")
            print(data_field)
            teams[team_number_input][data_field] = str(input("Please enter the new answer "))

def search_team():
    user_search = int(input("What team do you want to search? "))
    print("Options:")
    print(team_aspects)
    user_search_specific = input("What would you like to look up about a team? ")
    for team_aspect in team_aspects:
        if user_search_specific == team_aspect:
            print(user_search_specific)
            print(teams[user_search][user_search_specific])
            break
    else:
        print("Unknown Input")
        search_team()

    main_function()

def list_team():
    print(teams.keys())

    main_function()

def exit_program():
    print("You are choosing to exit the program")
    user_exit = input("Are you sure you want to leave? (y/n) ")
    if user_exit == "y":
        "You are now leaving the program"
        return
    elif user_exit == "n":
        "You chose to stay in the program"
        main_function()
    else:
        print("Input is unknown. Please input y or n")
        exit_program()

def main_function():
    print("Options:")
    print("add team, remove team, modify team, list of teams, search for team, exit")
    user_question_1 = input("What would you like to do? ")
    if user_question_1 == "add team":
        add_team()
    elif user_question_1 == "modify team":
        modify_team()
    elif user_question_1 == "remove team":
        remove_team()
    elif user_question_1 == "search for team":
        search_team()
    elif user_question_1 == "list of teams":
        list_team()
    elif user_question_1 == "exit":
        exit_program()
    else:
        print("Input is unknown.")
        main_function()

main_function()