team_dictionary = {}
user_action = input("""Enter the number of the action you want to do
            1   add a team
            2   modify a team
            3   view a team
            4   remove a team
            5   search a team
            6   list all teams 
            7   leave \n """)
while True:  
    if user_action == "0":
    #returning to main menu
        user_action = input("""Enter the number of the action you want to do
            1   add a team
            2   modify a team   
            3   view a team
            4   remove a team
            5   search a team
            6   list all teams
            7   leave \n """)
    elif user_action == "1":
    #adding a team  
        number = input("What is your team number? \n")
        while number.isdigit() == False:
            number = input("Your input is not an integer, please input an integer \n")
        name = input("What is the name of your team? \n")
        while name.isdigit() == True:
            name = input("Your input is not a string, please input a string\n")
        programming_language = input("What is the programming language of your team? \n")
        while programming_language.isdigit() == True:
            programming_language = input("Your input is not a string, please input a string\n")
        width = input("What is the width of your robot? \n")
        while width.isdigit() == False:
            width = input("Your input is not an integer, please input an integer \n")
        length = input("What is the length of your robot? \n")
        while length.isdigit() == False:
            length = input("Your input is not an integer, please input an integer \n")
        camera_vision_system = input("True or False, your robot has a camera vision system? \n")
        while True:
            if camera_vision_system != "True":
                if camera_vision_system != "False":
                    camera_vision_system = input("Your input is not a boolean, please input either 'True' or 'False' \n")
                    if camera_vision_system == "True":
                        break 
                    elif camera_vision_system == "False":
                        break
                else:
                    break
            else:
                break
        number_of_motors = input("How many motors does your robot have? \n")
        while number_of_motors.isdigit() == False:
            number_of_motors = input("Your input is not an integer, please input an integer \n")
        added_team_information = {
            "number": number,
            "name": name,
            "programming_language": programming_language,
            "width": width,
            "length": length, 
            "camera_vision_system": camera_vision_system, 
            "number_of_motors": number_of_motors}
        team_dictionary.update({number:added_team_information})
        user_action = input("""If you want to continue, press 1. \nIf you want to exit the "add" function, press 0. \n """)
    elif user_action == "2":
    #modify a team
        modify_team = input("What is the team you want to modify? \n")
        modify_attribute = None
        new_attribute = None 
        if modify_team in team_dictionary:
            print(team_dictionary[modify_team])
            modify_attribute = input("What is the attribute that you want to modify? \n")
            if modify_attribute in team_dictionary[modify_team]:
                new_attribute = input("What do you want the new "+modify_attribute+" to be? \n")
                if modify_attribute == "number":
                    while new_attribute.isdigit() == False:
                        new_attribute = input("Your input is not an integer, please input a integer\n")
                elif modify_attribute == "name":
                    while new_attribute.isdigit() == True:
                        new_attribute = input("Your input is not a string, please input a string\n")
                elif modify_attribute == "programming_language":
                    while new_attribute.isdigit() == True:
                        new_attribute = input("Your input is not a string, please input a string\n")
                elif modify_attribute == "width":
                    while new_attribute.isdigit() == False:
                        new_attribute = input("Your input is not an integer, please input a integer\n")
                elif modify_attribute == "length":
                    while new_attribute.isdigit() == False:
                        new_attribute = input("Your input is not an integer, please input a integer\n")
                elif modify_attribute == "camera_vision_system":
                    while True:
                        if new_attribute != "True":
                            if new_attribute != "False":
                                new_attribute = input("Your input is not a boolean, please input either 'True' or 'False' \n")
                                if new_attribute == "True":
                                    break 
                                elif new_attribute == "False":
                                    break
                            else:
                                break
                        else:
                            break
                elif modify_attribute == "number_of_motors":
                    while new_attribute.isdigit() == False:
                        new_attribute = input("Your input is not an integer, please input a integer\n")
                team_dictionary[modify_team].update({modify_attribute:new_attribute})
                print(team_dictionary[modify_team])
                user_action = input("""If you want to continue, press 2. \nIf you want to exit the "modify" function, press 0. \n""")
                if modify_attribute == "number":
                    team_dictionary[new_attribute] = team_dictionary[modify_team]
                    team_dictionary.pop(modify_team)           
            elif modify_team not in team_dictionary[modify_team]:
                print("I'm sorry, the team you want to modify is not in the dictionary.")
                user_action = input("""If you want to continue, press 2. \nIf you want to exit the "modify" function, press 0. \n""")
        elif modify_team not in team_dictionary:
            print("I'm sorry, the team you want to modify is not in the dictionary.")
            user_action = input("""If you want to continue, press 2. \nIf you want to exit the "modify" function, press 0. \n""")
    elif user_action == "3":
    #viewing a team
        view_team = input("What is the number of the team you want to view? \n ")
        if view_team in team_dictionary:
            print(team_dictionary[view_team])
        elif view_team not in team_dictionary:
                print("I'm sorry, the team you are looking for does not exist.")
        user_action = input("""If you want to continue, press 3. \nIf you want to exit the "view" function, press 0. \n """)
    elif user_action == "4":
    #removing a team
        print(team_dictionary)
        remove_team = input("What is the number of the team you want to remove? \n ")
        if remove_team in team_dictionary:
            team_dictionary.pop(remove_team)
            print("Team " +remove_team+ " has been removed from the team dictionary!")
        elif remove_team not in team_dictionary:
                print("I'm sorry, the team you are looking for does not exist.")
        user_action = input("""If you want to continue, press 4. \nIf you want to exit the "remove" function, press 0.\n """)
    elif user_action == "5":
    #searching for a team
        search_team = input("What is the number or name of the team you want to search for?\n")
        if search_team in team_dictionary:
            print("Yes, the team you are looking for is in the team dictionary")
        else:
            result=None
            for key in team_dictionary:
                if team_dictionary[key]["name"] == search_team:
                    print("Yes, the team you are looking for is in the team dictionary")
                    result=team_dictionary[key]
                    break  
            if not result:
                print("""I'm sorry, but the team you are looking for is not in the team dictionary.
                Please make sure that your input is an integer.""")
        user_action = input("""If you want to continue, press 5. \n If you want to exit the "search" function, press 0.\n """)
    elif user_action == "6":
    #listing all teams
        print(team_dictionary)
        user_action = input("""If you want to continue, press 6. \nIf you want to exit the "list" function, press 0.\n """)
    elif user_action not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
    #returning to main menu if user_action is not a known value
        print("I'm sorry, could you please re-enter your command?")
        user_action = input("""Enter the number of the action you want to do
            1   add a team
            2   modify a team   
            3   view a team
            4   remove a team
            5   search a team
            6   list all teams
            7   leave \n""")
    elif user_action == "7":
        break