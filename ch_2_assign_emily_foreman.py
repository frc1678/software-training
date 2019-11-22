teams = {}

while True:
    command = input("""Type 'add' to add a team
Type 'remove' to remove a team
Type 'edit' to change a teams data
Type 'search' to search for a team
Type 'list all teams' to display all teams
Type 'quit' to exit
                   """)

    if command == "add":
      
        check = False
        while check == False:
            leavethisthing =input("Type quit to exit ")
            if leavethisthing == "quit":
                break
            number = input("What is the team number ")
            if number.isdigit():
                check = True
                if leavethisthing == "quit":
                    continue
        team_name = input("What is the team name? ")
        print("The team name has been added")

        programming_language = input("What programming language does the team use? ")
        print("The programming language has been added")

        width = int(input("What is the width of the robot? "))
        print("The width has been added")

        length = int(input("What is the length of the robot? "))
        print("The length has been added")

        vision = input("Does the robot have a vision system? True or False: ")
        print("The information has been added")

        nummotors = int(input("How many motors does the robot have? "))
        print("The number of motors have been added")
        
        attributes_of_team = {"Number": number,
                              "Name": team_name,
                              "Programming_language": programming_language,
                              "Width" : width,
                              "Length": length,
                              "Vision_system": vision,
                              "Number_of_Motors" : nummotors}
        new_team = {number: attributes_of_team}
        teams.update(new_team)                  
        print(teams)
    

    if command == "remove":
        wannaquitdis = input("Type quit to exit ")
        if wannaquitdis == "quit":
            break
        print(teams)
        int_remove = int(input("What team number do you want to remove? "))
        teams.pop(int_remove)
        print(teams)
        
    if command == "list all teams":
        quitdisthing = input("Type quit to exit ")
        if quitdisthing == "quit":
            break
        print(teams)
       
    if command == "edit":
        wannaleavedis = input("Type quit to exit ")
        if wannaleavedis == "quit":
            break
        def edit(keyfind, definition):
            for key in attributes_of_team.keys():
                if key == keyfind:
                    attributes_of_team[key] = definition
        definition = input("What do you want the key to be? ")
        attributes = input("""What do you want to edit? 
Type "Number" to edit the number
Type "Name" to edit the name
Type "Programming_laguage" to edit the programming language
Type "Width" to edit the width
Type "Length" to edit the length
Type "Vision_system" to edit the vision
Type "Number_of_Motors" to edit the number of motors
Type "quit" to exit
""" )
        edit(attributes, definition)
        teams.update(attributes_of_team)
        print(attributes_of_team)
                      
    if command == "search":
        leavedisbadboy = input("Type quit to leave ")
        if leavedisbadboy == "quit":
            break
        searcht = input("""What do you want to search for?
Type "number" to search for the team number
Type "team name" to search for a team name
Type "programming language" to search for a programming language
Type "width" to search for a width of a robot
Type "length" to search for the length of a robot
Type "vision" to search if a robot has vison
Type "motors" to find the number of motors a robot has
 """)
        if searcht == "number":
            print(attributes_of_team.get("Number"))
        if searcht == "team name":
            print(attributes_of_team.get("Name"))
        if searcht == "programming language":
            print(attributes_of_team.get("Programming_language"))
        if searcht == "width":
            print(attributes_of_team.get("Width"))
        if searcht == "length":
            print(attributes_of_team.get("Length"))
        if searcht == "vison":
            print(attributes_of_team.get("Vision_System"))
        if searcht == "motors":
            print(attributes_of_team.get("Number_of_Motors"))
        print(attributes_of_team.get(searcht))
    if command == "quit":
        break
