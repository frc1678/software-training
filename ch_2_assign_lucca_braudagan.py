teams = {}

initial_user_request = input("choose_from:_'add',_'view',_'modify',_'remove',_'search',_'list',_'return'")
if initial_user_request=="add":
    add_team();
elif initial_user_request=="view":

elif initial_user_request=="modify":

elif initial_user_request=="remove":

elif initial_user_request=="search":

elif initial_user_request=="list":

elif initial_user_request=="return":

else initial_user_request!="add","view","modify","remove","search","list","return":

def add_team():
	temp_team_dictionary = {}

	name = input("What is your team's name?")
	p_language = input("What is your team's programming language?")

	temp_team_dictionary["name"] = name
	temp_team_dictionary["p_l"] = p_language

	team_number = input("What is your team's 'team number'")
	teams[team_number] = temp_team_dictionary

add_team() citrus circuits, c++, 1678

#{1678 : {"name" : "citrus circuits", "p_l" : "c++"}}
 


