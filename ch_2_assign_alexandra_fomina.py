teams = {
	'': {}
}
while True:
    command = input("""
    	Type add to add a team, 
    	Type remove to remove a team, 
        Type search to search for a team, 
        Type list all teams to display all teams, 
        Type view to see a team's information
        Type edit to edit a team's information
    	Type quit to exit
    	""")
    if command == "add":
        t_number = int(input("What is the team number?"))
        t_name = input("What is the team name? ")
        t_lang = input("What is their programming language? ")
        t_width = float(input("What is the width of their robot? "))
        t_length = float(input("What is the length of their robot? "))
        t_camera = bool(input("Do they have camera vision?"))
        t_motors = int(input("How many motors do they have? "))
        attributes = {
        "Name" : t_name, 
        "Language" : t_lang, 
        "Width" : t_width, 
        "Length" : t_length, 
        "Camera" : t_camera ,
        "Motors" : t_motors
         }
        new_t = {t_number: attributes}
        teams.update(new_t)
    if command == "remove":
        remove = int(input("What team would you like to remove?"))
        teams[remove] = {}
        print("That team has been removed")
    if command == "search":
        search = bool(input("Are you searching by number?" ))
        if search == True: 
            number = input("What is the team number?")
        if number in teams: 
            print(teams)
        if search == False:
                    print("Please serach by team number!")
        else:
            print("This team doesn't exist")
    if command == "list":
        print(teams)
    if command == "view": 
        view = int(input("Which team would you like to view? "))
        if view in teams:
            print(teams[1678])
        else:
            print("This team doesn't have any information")
    if command == "edit":
        new_name = input("What is the team name? ")
        new_lang = input("What is their programming language? ")
        new_width = float(input("What is the width of their robot? "))
        new_length = float(input("What is the length of their robot? "))
        new_camera = bool(input("Do they have camera vision?"))
        new_motors = int(input("How many motors do they have? "))
        def replace_new_info(key_to_find, definition):
            for key in teams.keys():
                if key == key_to_find:
                    teams[key] = new_name
        replace_new_info('teams', 't_number')
        print(t_number)
    if command == "quit":
        break