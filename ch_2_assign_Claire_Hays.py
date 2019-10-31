teams = {}
while True:
    command = input("""Enter the command (add a team, remove a team, search for a team, list all teams, 
view team's information, modify team's information, view all teams and information, or quit): """)
    

    if command == "add a team":
        check = False
        while check == False:
            team_num = input("What is the team number? ")
            if team_num == 'quit':
                check = True
            elif team_num.isdigit():
                team_num = int(team_num)
                check = True
            else:
                print("Please type your team number as an integer")
        if team_num == 'quit':
            continue

        team_name = input("What is the team name? ")
        if team_name == 'quit':
            continue

        team_prog_lang = input("What is the team's programming language? ")
        if team_prog_lang == 'quit':
            continue

        check = False
        while check == False:
            robot_width = input("What is the robot's width? ")
            if robot_width == 'quit':
                check = True
            elif robot_width.isnumeric():
                robot_width = float(robot_width)
                check = True
            else:
                print("Please type your robot width as an float")
        if robot_width == 'quit':
            continue
        
        check = False
        while check == False:
            robot_length = input("What is the robot's length? ")
            if robot_length == 'quit':
                check = True
            elif robot_length.isnumeric():
                robot_length = float(robot_length)
                check = True
            else:
                print("Please type your robot length as an float")
        if robot_length == 'quit':
            continue

        check = False
        while check == False:
            robot_vision = input("Does the robot have camera vision? ")
            if robot_vision == 'quit':
                check = True
            elif robot_vision.lower() == "yes":
                robot_vision = True
                check = True
            elif robot_vision.lower() == "no":
                robot_vision == False
                check = True
            else:
                print("Please type either yes or no")
        if robot_vision == 'quit':
            continue
        
        check = False
        while check == False:
            robot_motors = input("How many drivetrain motors does the robot have? ")
            if robot_motors == 'quit':
                check = True
            elif robot_motors.isdigit():
                robot_motors = int(robot_motors)
                check = True
            else:
                print("Please type the number of motors as an integer")
        if robot_motors == 'quit':
            continue

        attributes = {"Name": team_name, "Programming Language": team_prog_lang, 
        "Width": robot_width, "Length": robot_length, "Camera Vision": robot_vision, 
        "Drivetrain Motors": robot_motors}
        new_team = {team_num: attributes} 
        teams.update(new_team)


    elif command == "remove a team":
        remove_team_num = input("What team number would you like to remove? ")
        if remove_team_num == 'quit':
            continue
        else:
            remove_team_num = int(remove_team_num)
        teams.pop(remove_team_num)
        print("Team number successfully removed. To view new team list, type 'list all teams'")


    elif command == "search for a team":
        team_search = input("What team would you like to search for? ")
        if team_search == 'quit':
            continue
        elif team_search.isnumeric() == True:
            team_get = teams.get(int(team_search))
            if team_get == None:
                print("The team you searched for was not found in the database. ")
            else:
                print("The team you searched for was found in the database. ")
        else:
            names = []
            for team_num, team_attributes in teams.items():
                names.append(team_attributes["Name"])
            if team_search in names:
                print("The team you searched for was found in the database.")
            else:
                print("The team you searched for was not in the database.")
                   


    if command == "list all teams":
        print(teams.keys())


    if command == "view team's information":
        view_team_num = input("What team's information would you like to view? ")
        if view_team_num == 'quit':
            continue
        else:
            view_team_num = int(view_team_num)
        view_team_attribute = str(input("""What attribute would you like to view (Name, 
    Programming Language, Width, Length, Camera Vision, Drivetrain Motors? """))
        if view_team_attribute == 'quit':
            continue
        else:
            print(teams[view_team_num][view_team_attribute])


    if command == "modify team's information":
        print("If attribute hasn't changed, type none")
        
        check = False
        while check == False:
            chng_team_num = input("What team number's information would you like to change? ")
            if chng_team_num == 'quit':
                check = True
            elif chng_team_num.isdigit():
                chng_team_num = int(chng_team_num)
                check = True
            else:
                print("Please type your team number as an integer")
        if chng_team_num == 'quit':
            continue

        new_team_name = input("What is the new team name? ")
        if new_team_name == 'quit':
           continue
        elif new_team_name == "none":
           new_team_name = teams[chng_team_num]["Name"]
        
        new_team_prog_lang = input("What is the team's new programming language? ")
        if new_team_prog_lang == 'quit':
            continue
        elif new_team_prog_lang == "none":
            new_team_prog_lang = teams[chng_team_num]["Programming Language"]
        
        check = False
        while check == False:
            new_robot_width = input("What is the robot's new width? ")
            if new_robot_width == 'quit':
                check = True
            elif new_robot_width == 'none':
                new_robot_width = teams[chng_team_num]["Width"]
                check = True
            elif new_robot_width.isnumeric():
                new_robot_width = float(new_robot_width)
                check = True
            else:
                print("Please type your robot width as an float")
        if new_robot_width == 'quit':
            continue
        
        check = False
        while check == False:
            new_robot_length = input("What is the robot's new length? ")
            if new_robot_length == 'quit':
                check = True
            elif new_robot_length == "none":
                new_robot_length = teams[chng_team_num]["Length"]
                check = True
            elif new_robot_length.isnumeric():
                new_robot_length = float(new_robot_length)
                check = True
            else:
                print("Please type your robot length as an float")
        if new_robot_length == 'quit':
            continue


        check = False
        while check == False:
            new_robot_vision = input("Does the new robot have camera vision? ")
            if new_robot_vision == 'quit':
                check = True
            elif new_robot_vision == "none":
                new_robot_vision = teams[chng_team_num]["Camera Vision"]
                check = True
            elif new_robot_vision.lower() == "yes":
                new_robot_vision = True
                check = True
            elif new_robot_vision.lower() == "no":
                new_robot_vision == False
                check = True
            else:
                print("Please type either yes or no")
        if new_robot_vision == 'quit':
            continue
        
        
        check = False
        while check == False:
            new_robot_motors = input("How many drivetrain motors does the new robot have? ")
            if new_robot_motors == 'quit':
                check = True
            elif new_robot_motors == "none":
                new_robot_motors = teams[chng_team_num]["Drivetrain Motors"]
                check = True
            elif new_robot_motors.isdigit():
                new_robot_motors = int(new_robot_motors)
                check = True
            else:
                print("Please type the number of motors as an integer")
        if new_robot_motors == 'quit':
            continue

        new_attributes = {"Name": new_team_name, "Programming Language": new_team_prog_lang, 
        "Width": new_robot_width, "Length": new_robot_length, "Camera Vision": new_robot_vision, 
        "Drivetrain Motors": new_robot_motors}
        teams[chng_team_num] = new_attributes
    

    elif command == "view all teams and information":
        print(teams)
    

    elif command == "quit":
        break

