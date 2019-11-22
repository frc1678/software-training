teams = {}
def remove():
    quitz = input("type quit to exit ")
    print(robot_information)
    removez = int(input("What team number do you want to remove? "))
    robot_information.pop(removez)
    print(robot_information)
def listteams():
    quitdis = input("Type quit to exit ")
    print(teams)

robot_information = {1 : {'location': 'Pontiac, Michigan',
                                         'rookie_year': 1997,
                                         'competed_in_2019': True,
                                         'competition_names' : 'FIM District Center Line Event, FIM District Troy Event',
                                         'competition_locations' : 'Center Line MI, USA and  Troy MI, USA',
                                         'competition_awards' : 'none',
                                   },
                     #this is team one's information

                     4 : {
                         'location' : 'Van Nuys California, USA',
                         'rookie_year' : 1997,
                         'competed_in_2019' : True,
                         'competition_names' : 'Los Angeles North Regional, Los Angeles Regional, Wings Over Camarillo, Battleship Blast (Saturday), Beach Blitz',
                         'competition_locations' : 'Valencia, CA, USA, Valencia, CA, USA, Camarillo, CA, USA, San Pedro, CA, United States',
                         'awards' : 'Quality Award sponsored by Motorola Solutions Foundation',
                      },
                
                     5 : {
                         'location' : 'Melvindale, MI, USA',
                         'rookie_year' : 1998,
                         'competed_in_2019' : True,
                         'competition_names' : 'Big Bang!',
                         'competition_locations' : 'Taylor, MI, USA',
                         'awards' : 'none',
                      },
        

                     6 : {
                         'location' :  'Plymouth, MN, USA',
                         'rookie_year' : 1994,
                         'competed_in_2019' : False,
                         'competition_names' : 'none',
                         'competition_locations' : 'none',
                         'awards' : 'none',
                     },

                     7 : {
                         'location' : 'Baltimore, MD, USA',
                         'rookie_year' : 'not stated, last competed in 2012',
                         'competed_in_2019' : False,
                         'competition_locations' : 'none',
                         'competition_names' : 'none',
                         'awards' : 'none',

                      }
                     }


while True:
    command = input(""" Type 'add' to add a team
Type 'remove' to remove a team
Type 'edit' to change a team's data
Type 'search' to search for a team
Type 'list all teams' to display all teams
Type 'quit' to exit
""")

    if command == "add":
        check = False
        while check == False:
            leave = input("type quit to exit ")
            if leave == "quit":
                break
                continue
            number = input("What is the team number ")
            if number.isdigit():
                check = True
                if leave == "quit":
                    continue
        team_name = input("What is the team name? ")
        programming_language = input("What programming language does the team use? ")
        checks = False
        while checks == False:
            width = input("What is the width? ")
            if width.isdigit():
                checks = True
                continue
        morecheck = False
        while morecheck == False:
            length  = input("What is the length? ")
            if length.isdigit():
                morecheck = True
                continue
        vision = input("Does the robot have a vision system? ")
        go = False
        while go == False:
            motorz = input("How many motors are there? ")
            if motorz.isdigit():
                go = True
                continue
        

        attributes_team = {"number" : number,
                           "name" : team_name,
                           "programming language" : programming_language,
                           "width" : width,
                           "length" : length,
                           "vision system" : vision,
                           "number of motors" : motorz,
                           "location" : location
                           
                      
        }
        newteam = {number: attributes_team}
        robot_information.update(newteam)
        teams.update(newteam)
        print(robot_information)
                         
    if command == "remove":
        remove()
    if command == "quit":
        break
        continue
    if command == "search":
        team_number = int(input("What is the team number? (search booooo) "))
        team_attribute = input("What is the team attribute? ")
        print(robot_information[team_number] [team_attribute])
def remove():
    quitz = input("type quit to exit ")
    print(robot_information)
    removez = int(input("What team number do you want to remove? "))
    robot_information.pop(removez)
    print(robot_information)
def listteams():
    quitdis = input("Type quit to exit ")
    print(teams)

robot_information = {1 : {'location': 'Pontiac, Michigan',
                                         'rookie_year': 1997,
                                         'competed_in_2019': True,
                                         'competition_names' : 'FIM District Center Line Event, FIM District Troy Event',
                                         'competition_locations' : 'Center Line MI, USA and  Troy MI, USA',
                                         'competition_awards' : 'none',
                                   },
                     #this is team one's information

                     4 : {
                         'location' : 'Van Nuys California, USA',
                         'rookie_year' : 1997,
                         'competed_in_2019' : True,
                         'competition_names' : 'Los Angeles North Regional, Los Angeles Regional, Wings Over Camarillo, Battleship Blast (Saturday), Beach Blitz',
                         'competition_locations' : 'Valencia, CA, USA, Valencia, CA, USA, Camarillo, CA, USA, San Pedro, CA, United States',
                         'awards' : 'Quality Award sponsored by Motorola Solutions Foundation',
                      },
                
                     5 : {
                         'location' : 'Melvindale, MI, USA',
                         'rookie_year' : 1998,
                         'competed_in_2019' : True,
                         'competition_names' : 'Big Bang!',
                         'competition_locations' : 'Taylor, MI, USA',
                         'awards' : 'none',
                      },
        

                     6 : {
                         'location' :  'Plymouth, MN, USA',
                         'rookie_year' : 1994,
                         'competed_in_2019' : False,
                         'competition_names' : 'none',
                         'competition_locations' : 'none',
                         'awards' : 'none',
                     },

                     7 : {
                         'location' : 'Baltimore, MD, USA',
                         'rookie_year' : 'not stated, last competed in 2012',
                         'competed_in_2019' : False,
                         'competition_locations' : 'none',
                         'competition_names' : 'none',
                         'awards' : 'none',

                      }
                     }


while True:
    command = input(""" Type 'add' to add a team
Type 'remove' to remove a team
Type 'edit' to change a team's data
Type 'search' to search for a team
Type 'list all teams' to display all teams
Type 'quit' to exit
""")

    if command == "add":
        check = False
        while check == False:
            leave = input("type quit to exit ")
            if leave == "quit":
                break
                continue
            number = input("What is the team number ")
            if number.isdigit():
                check = True
                if leave == "quit":
                    continue
        team_name = input("What is the team name? ")
        programming_language = input("What programming language does the team use? ")
        checks = False
        while checks == False:
            width = input("What is the width? ")
            if width.isdigit():
                checks = True
                continue
        morecheck = False
        while morecheck == False:
            length  = input("What is the length? ")
            if length.isdigit():
                morecheck = True
                continue
        vision = input("Does the robot have a vision system? ")
        go = False
        while go == False:
            motorz = input("How many motors are there? ")
            if motorz.isdigit():
                go = True
                continue
        

        attributes_team = {"number" : number,
                           "name" : team_name,
                           "programming language" : programming_language,
                           "width" : width,
                           "length" : length,
                           "vision system" : vision,
                           "number of motors" : motorz,
                      
        }
        newteam = {number: attributes_team}
        robot_information.update(newteam)
        print(robot_information)

    if command == "edit":
        print(teams)
        def replace(keyfind, definition):
            for key in robot_information.keys():
                if key == keyfind:
                    teams[key] = definition
        whattoedit = input("What do you want to edit? ")
        definition = input("What do you want the key to be?")
        replace(whattoedit , definition)
        
                         
    if command == "remove":
        remove()
    if command == "quit":
        break
        continue
    if command == "search":
        team_number = int(input("What is the team number? (search booooo) "))
        team_attribute = input("What is the team attribute? ")
        print(robot_information[team_number] [team_attribute])



