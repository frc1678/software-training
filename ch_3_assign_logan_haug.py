from isfloat import isTeam, getTeam, isValidUserInput, isbool, emptyList
class competition():
    name = ""
    place = ""
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def __str__(self):
        return self.name + " in " + self.place
#this is the class for a team, I wanted to make a team a class because i really didn't want to deal with dictionaries that nest three times. Additionally Carter had just showed me o.o.p. and I wanted to practice it, also it seemed like a good idea at the time. the class team has the properties of name,number,location,rookie_year,recent_season (if the team competed in the most recent frc season),competitions, and awards. The only thing really notable about this is that the property competitions is also a class which just has the properties of name, and place. I also employ the __str__ function to make printing a team extremely easy and this is one of the main benefits imo over using a large nested dictionary
class team():
    name = ""
    number = 0
    location = ""
    rookie_year = 0
    recent_season = False
    competitions = []
    awards = []
    def __init__(self,name,number,location,rookie_year,recent_season,competitions,awards):
        self.name = name
        self.number = number
        self.location = location
        self.rookie_year = rookie_year
        self.recent_season = recent_season
        self.competitions = competitions
        self.awards = awards
#all this function does is make the information look nice and pretty for the user.
    def __str__(self):
        comps = ""
        awards = ""
        for award in self.awards:
            awards = awards + "\n" + award
        for competition in self.competitions:
            comps = comps + "\n" + str(competition)
        comps = comps + "\n"
        return "\n" + str(self.number) + ":\n\nName: " + self.name + "\n\nLocation: " + self.location + "\n\nRookie Year: " + str(self.rookie_year) + "\n\nCompeted in 2019 Season: " + str(self.recent_season) + "\n\nCompetitions: " + comps + "\nAwards: " + awards
    def isValid(self):
        if type(self.name) == str and type(self.number) == int and type(self.location) == str and type(self.rookie_year) == int and type(self.recent_season) == bool and type(self.competitions) == list and type(self.awards) == list:
            return True
        return False
#this is the teams list
teams = [team("name",1,"location",0,False,[competition("competition","place"),competition("competition 2","place 2")],["award","award 2"])]
#the main part of the program runs in a while true loop because I wanted the features to be repeatable, and I didn't want the program to be easy to accidentally exit.
while True:

    user_feat = input("\nenter a feature to use: ")
#this is the view feature, all that it does is take a user input for the team that the user wants, and passes it through isTeam() which is a function that I wrote that just returns the printable version of the user team if it exists in the teams list, if it doesn't the function returns something like "this team isn't in the teams list"
    if user_feat == "view":
        userTeam = input("\nEnter a team: ")
        if userTeam != "return":
            userTeam = isTeam(teams,userTeam)
            print(userTeam)

#this is the remove feature, first it takes a team from the user, and then passes it through the getTeam() function which returns the team object if it exists within the teams list, otherwise it returns False. Then it removes the team if it exists, otherwise it prints a generic error message.
    elif user_feat == "remove":
        userTeam = input("\nEnter a team: ")
        if userTeam != "return":
            userTeam = getTeam(userTeam, teams)
            if userTeam != False:
                teams.pop(teams.index(userTeam))
                print("\nSuccessfully Removed")
            else:
                print("\nSomething went wrong, please try again")
#this is the list feature, first it checks to see if the teams list is empty, then it iterates through the teams list and prints every element. This imo is one of the benefits of using a object based viewer for this case because it makes printing a lot easier than having to have a function to print every team.
    elif user_feat == "list":
        if len(teams) == 0:
            print("\nthere are no teams added yet, try adding some :)")
        else:
            for team in teams:
                print(team)

    elif user_feat == "add":
#The first thing that the add feature does is iterate through the attributes of a "team" object (excluding competitons and awards), and gets inputs from the user. each time a new attribute is asked from the user, user_attribute is checked to see if the user wants to return, if the user does keep_going is set to false which stops the rest of the add feature from running any more code, otherwise the user's inputs are appended to a list which stores the attributes of the new team.
        attributes = ["\nName", "\nNumber","\nLocation","\nRookie year","\nCompeted in most recent season?"]
        user_attributes = []
        keep_going = True
        for attribute in attributes:
            user_attribute = input(attribute + ": ")
            if user_attribute == "return":
                keep_going = False
                break
            else:
                user_attributes.append(user_attribute)
#The next thing the add feature does is go through adding awards that the new team has earned, and competitions the new team has gone to. I wanted the competitions to be a class because it would be a lot easier to see all of the names of the competitions, or all the places the team has gone to. I could have done this with a dictionary, but with a class its a lot easier to make a __str__ function when I want to print the competitions. As you can see there is a difference for the user when they enter "None" compared to "return", None just ends the addition of more competitions whilst "return" stops the add feature. I wanted to do this because I needed a way to break out of the competition adding loop, and we also had to make the viewer stop any feature anywhere when the user enters the word "return".
        user_competitions = []
        user_awards = []
        while keep_going:
            user_competition = input("\nEnter the competiton's name (if no more competitions enter 'None'): ")
            if user_competition == "None":
                break
            elif user_competition == "return":
                keep_going = False
                break
            user_place = input("\nEnter where the competiton took place: ")
            if user_place == "None":
                break
            elif user_place == "return":
                keep_going = False
                break
            user_competitions.append(competition(user_competition,user_place))

#This is the loop that adds awards to the list user_awards
        while keep_going:
            user_award = input("\nEnter Awards this team has recieved during their most recent season (if there are none or no more enter 'None'): ")
            if user_award == "None":
                break
            elif user_award == "return":
                keep_going = False
                break
            user_awards.append(user_award)

#I test if keep_going is True, so that this code block doesn't get run if the user enters "return" at any point in the add feature. Then the function isValidUserInput() is run, which literally just tests if the entered user attributes for number, rookie_year could be cast into integers, and if recent_season is either the string "true" or the string "false". Then the function emptyList is run which just checks if the argument's len() is equivalent to 0, if it is it returns a list only containing the string "None", otherwise it returns the original list. I did this because I didn't want the user to be confused when they view the team that they added to the teams list prints two brackets instead of something like "No competitions" or "None".
        if keep_going:
            if not isValidUserInput(user_attributes):
                print("\nSomething went wrong please try again.")
            else:
                user_competitions = emptyList(user_competitions)
                user_awards = emptyList(user_awards)
#Then the user input that will become whether or not the team competed in the most recent season is checked to see if it was either "true" or "false". isbool() is a function I wrote that returns either true or false depending on the user input, and if the user input is not the exact string for a boolean value it returns Nonetype. Next the new team is appended to the teams list. However if the user input for whether the team competed in the most recent season is not either "true" or "false" it just prints a generic error message
                if type(isbool(user_attributes[4])) != None:
                    teams.append(team(user_attributes[0], int(user_attributes[1]), user_attributes[2], int(user_attributes[3]), isbool(user_attributes[4]), user_competitions, user_awards))

                else:
                    print("\nSomething went wrong please try again.")

    elif user_feat == "modify":
        ut = input("\nWhich team to modify: ")
        user_team = getTeam(ut,teams)

        if user_team != False:

            user_attribute = input("Which attribute of " + str(user_team.number) + " to modify: ").lower()
            user_attributes = ["name","number","location","rookie year","recent season","competitions","awards"]


            if user_attribute in user_attributes:
                if user_attribute == "competitions":
                    add_or_remove = input("Would you like to add or remove competitions: ").lower()
                    if add_or_remove == "add":
                        user_data = user_team.competitions
                        while True:
                            user_competition = input("\nEnter the competiton's name (if no more competitions enter 'none'): ")
                            if user_competition == "none" or user_competition == "return":
                                break
                            user_place = input("\nEnter where the competiton took place: ")
                            if user_place == "return":
                                break
                            user_data.append(competition(user_competition,user_place))
                            if len(user_data) == 0:
                                user_data = emptyList(user_data)

                    elif add_or_remove == "remove":
                        user_data = user_team.competitions
                        while True:
                            competition_count = 1
                            for competition in user_team.competitions:
                                print(str(competition_count) + ": " + str(competition))
                                competition_count += 1
                            user_competition = input("which competition to remove (enter the number next to the competition or enter 'none' to stop): ")
                            if user_competition == "none" or user_competition == "return":
                                break
                            elif user_competition.isnumeric() == False:
                                print("Please enter a number")
                            else:
                                (user_data).pop(int(user_competition)-1)
                    else:
                        user_data = user_team.competitions


                elif user_attribute == "awards":
                    user_data = user_team.awards
                    add_or_remove = input("Would you like to add or remove awards: ")
                    if add_or_remove == "add":
                        while True:
                            user_award = input("\nEnter Awards this team has recieved during their most recent season (if there are none or no more enter 'none'): ")
                            if user_award == "none":
                                break
                            elif user_award == "return":
                                break
                            user_data.append(user_award)
                            user_data = emptyList(user_data)
                    elif add_or_remove == "remove":
                        while True:
                            award_count = 1
                            for award in user_data:
                                print(str(award_count) + ": " + award)
                                award_count += 1
                            user_award = input("Which award to remove (enter the number, or enter 'none' to exit): ")
                            if user_award == "none" or "return":
                                break
                            elif user_award.isnumeric():
                                user_data.pop(int(user_award)-1)
                            else:
                                print("please enter a number or 'none'")
                        user_data == emptyList(user_data)



                else:
                    user_data = input("Input new data: ")
                if user_attribute == "number":
                    if user_data.isnumeric():
                        user_team.number = int(user_data)
                    else:
                        print("Please enter a number")
                elif user_attribute == "name":
                    user_team.name = user_data
                elif user_attribute == "location":
                    user_team.location = user_data
                elif user_attribute == "competitions":
                    user_team.competitions = user_data
                elif user_attribute == "awards":
                    user_team.awards == user_data
                elif user_attribute == "rookie year":
                    if user_data.isnumeric():
                        user_team.rookie_year = int(user_data)
                    else:
                        print("Please enter a number")
                elif user_attribute == "recent season":
                    if isbool(user_data) != None:
                        user_team.recent_season = isbool(user_data)
                    else:
                        print("please enter either true or false")
                if user_team.isValid():
                    teams.remove(getTeam(ut, teams))
                    teams.append(user_team)


        else:
            print("\nTeam not in entered teams")


    elif user_feat == "quit":
        print("\nGoodbye!\n")
        break
