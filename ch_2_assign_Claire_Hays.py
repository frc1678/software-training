teams = {}
while True:
    command = input("""Enter the command (add a team, remove a team, search for a team, list all teams, 
    view team's information, modify team's information, view all teams and information, or quit): """)
    

    if command == "add a team":
        team_num = int(input("What is the team number? ")) 
        team_name = input("What is the team name? ")
        team_prog_lang = input("What is the team's programming language? ")
        robot_width = float(input("What is the robot's width? "))
        robot_length = float(input("What is the robot's length? "))
        robot_vision = input("Does the robot have camera vision? ")
        if robot_vision.lower() == "yes":
            robot_vision = True
        elif robot_vision.lower() == "no":
            robot_vision == False
        robot_motors = int(input("How many drivetrain motors does the robot have? "))
        attributes = {"Name": team_name, "Programming Language": team_prog_lang, 
        "Width": robot_width, "Length": robot_length, "Camera Vision": robot_vision, 
        "Drivetrain Motors": robot_motors}
        new_team = {team_num: attributes} 
        teams.update(new_team)


    if command == "remove a team":
        remove_team_num = int(input("What team number would you like to remove? "))
        teams.pop(remove_team_num)
        print("Team number successfully removed. To view new team list, type 'list all teams'")


    if command == "search for a team":
        team_search = int(input("What team number would you like to search for? "))
        print(teams.get(team_search))


    if command == "list all teams":
        print(teams.keys())


    if command == "view team's information":
        view_team_num = int(input("What team's information would you like to view? "))
        view_team_attribute = str(input("""What attribute would you like to view (Name, 
        Programming Language, Width, Length, Camera Vision, Drivetrain Motors? """))
        print(teams[view_team_num][view_team_attribute])


    if command == "modify team's information":
        print("If attribute hasn't changed, type none")
        chng_team_num = int(input("What team number's information would you like to change? "))
        new_team_name = input("What is the new team name? ")
        
        if new_team_name == "none":
            new_team_name = teams[chng_team_num]["Name"]
        new_team_prog_lang = input("What is the team's new programming language? ")
        
        if new_team_prog_lang == "none":
            new_team_prog_lang = teams[chng_team_num]["Programming Language"]
        new_robot_width = input("What is the robot's new width? ")
       
        if new_robot_width == "none":
            new_robot_width = teams[chng_team_num]["Width"]
        else:
            new_robot_width = float(new_robot_width)
        new_robot_length = input("What is the robot's new length? ")
        
        if new_robot_length == "none":
            new_robot_length = teams[chng_team_num]["Length"]
        else:
            new_robot_length = float(new_robot_length)
        new_robot_vision = input("Does the new robot have camera vision? ")
        
        if new_robot_vision == "none":
            new_robot_vision = teams[chng_team_num]["Camera Vision"]
        elif new_robot_vision.lower() == "yes":
            new_robot_vision = True
        elif new_robot_vision.lower() == "no":
            new_robot_vision == False
        new_robot_motors = input("How many drivetrain motors does the new robot have? ")
        
        if new_robot_motors == "none":
            new_robot_motors = teams[chng_team_num]["Drivetrain Motors"]
        else:
            new_robot_motors = int(new_robot_motors)
        new_attributes = {"Name": new_team_name, "Programming Language": new_team_prog_lang, 
        "Width": new_robot_width, "Length": new_robot_length, "Camera Vision": new_robot_vision, 
        "Drivetrain Motors": new_robot_motors}
        teams[chng_team_num] = new_attributes
    

    if command == "view all teams and information":
        print(teams)
    

    if command == "quit":
        break

