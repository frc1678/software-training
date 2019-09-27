Robot_Team = input("What Robotics Team do you want to look into?")
Robot_Stat = input("What statistic would you like to see?")


Robot_TeamB = {1678: {'Location': 'Davis, CA, USA', 'Rookie': '2005', 'Participate?': 'Yes',
	'Competition Names': [
		'Central Valley Regional',
		'Sacramento Regional',
		'Aerospace Valley Regional', 
		'Carver Division', 
		'Einstein Field', 
		'RCC Qianjiang International Robotics Invitational'
	], 
	'Competition Location': [
		'Fresno, CA, USA', 
		'Davis, CA, USA', 
		'Lancaster, CA, USA', 
		'Houston, TX, USA', 
		'Houston TX, USA', 
		'Hangzhou, Zhejiang, China'
	],
	'Awards': [
		'Regional Chairman`s Award and Regional Winners', 
		'FIRST Dean`s List Finalist Award (Katie Stachowicz), Regional Winners, and Industrial Design Award sponsored by General Motors',
		'Regional Winners and Excellence in Engineering Award sponsored by Delphi', 'Championship Subdivision Winner and Entrepreneurship Award sponsored by Kleiner Perkins Caufield and Byers'
	,]}, 
	1111: {'Location': 'Edgewater, Maryland, USA', 'Rookie': '2003', 'Participate?': 'Yes',
	'Competition Names': [
		'CHS District Bethesda MD Event sponsored by Bechtel',
		'CHS District Owings Mills MD Event sponsored by Leidos', 
		'FIRST Chesapeake District Championship'
	],
	'Competition Location': [
		'Bethesda, MD 20817, USA', 
		'Owings Mills, MD 21117, USA', 
		'Fairfax, VA 22030, USA'
	],
	'Awards': [
		'Autonomous Award sponsored by Ford', 
		'District Chairman`s Award', 
		'Team Spirit Award sponsored by FCA Foundation'
	]},
	2222: {'Location': 'Tacoma, WA, USA', 'Rookie': '2007', 'Participate?': 'No', 'Competition': 'Pacific Northwest Regional 2007', 
	'Competition Location': 'Pioneer Courthouse Square in Portland, OR, USA', 'Award': 'None'},
	3333: {'Location': 'Julesburg, CO, USA', 'Rookie': '2010', 'Participate?': 'No', 'Competition': 'Colorado Regional 2010', 
	'Competition Location': 'Ritchie Center in Denver, CO, USA', 'Award': 'Judges Award'
	},
	5555: {'Show Location': 'Warren, Michigan', 'Rookie Year': '2015', 'Participate?': 'Yes', 
	'Competitions': ['FIM District Center Line Event','FIM District Marysville Event'], 'Competitions Location': ['Center Line, MI, USA', 'Marysville, MI, USA'],
	'Awards': 'District Event Winner'}}

print(Robot_Team)
if Robot_Team == "1678":
	print(Robot_Stat)
	if Robot_Stat == "Location" or Robot_Stat == "Team Location":
		print("Here you go!")
		print(Robot_TeamB[1678]['Location'])
	elif Robot_Stat == "Rookie Year" or Robot_Stat == "Team Debut":
		print("Processing!")
		print(Robot_TeamB[1678]['Rookie'])
	elif Robot_Stat == "2019" or Robot_Stat == "Did they participate in the 2019 competition?":
		print("Voila!")
		print(Robot_TeamB[1678]['Participate?'])
	elif Robot_Stat == "Competitions" or Robot_Stat == "Names of Competitions":
		print("Bang!")
		print(Robot_TeamB[1678]['Competition Names'])
	elif Robot_Stat == "Locations of Competition" or Robot_Stat == "Competition Locations":
		print("Fresh from the oven! Note that these are in order with the competition names. Best if you check that, first")
		print(Robot_TeamB[1678]['Competition Location'])
	elif Robot_Stat == "Awards" or Robot_Stat == "Awards Given":
		print("Flash!")
		print(Robot_TeamB[1678]['Awards'])
	else:
		print("*Database.exe has stopped working. Try the code again. :P*")


elif Robot_Team == "1111":
	print(Robot_Stat)
	if Robot_Stat == "Location" or Robot_Stat == "Team Location":
		print("Here you go!")
		print(Robot_TeamB[1111]['Location'])
	elif Robot_Stat == "Rookie Year" or Robot_Stat == "Team Debut":
		print("Processing!")
		print(Robot_TeamB[1111]['Rookie'])
	elif Robot_Stat == "2019" or Robot_Stat == "Did they participate in the 2019 competition?":
		print("Voila!")
		print(Robot_TeamB[1111]['Participate?'])
	elif Robot_Stat == "Competitions" or Robot_Stat == "Names of Competitions":
		print("Bang!")
		print(Robot_TeamB[1111]['Competition Names'])
	elif Robot_Stat == "Locations of Competition" or Robot_Stat == "Competition Locations":
		print("Fresh from the oven! Note that these are in order with the competition names. Best if you check that, first")
		print(Robot_TeamB[1111]['Competition Location'])
	elif Robot_Stat == "Awards" or Robot_Stat == "Awards Given":
		print("Flash!")
		print(Robot_TeamB[1111]['Awards'])
	else:
		print("*Database.exe has stopped working. Try the code again. :P*")


elif Robot_Team == "2222":
	print(Robot_Stat)
	if Robot_Stat == "Location" or Robot_Stat == "Team Location":
		print("Here you go!")
		print(Robot_TeamB[2222]['Location'])
	elif Robot_Stat == "Rookie Year" or Robot_Stat == "Team Debut":
		print("Processing!")
		print(Robot_TeamB[2222]['Rookie'])
	elif Robot_Stat == "2019" or Robot_Stat == "Did they participate in the 2019 competition?":
		print("Voila!")
		print(Robot_TeamB[2222]['Participate?'])
	elif Robot_Stat == "Competitions" or Robot_Stat == "Names of Competitions":
		print("Bang!")
		print(Robot_TeamB[2222]['Competition'])
	elif Robot_Stat == "Locations of Competition" or Robot_Stat == "Competition Location":
		print("Fresh from the oven! Note that these are in order with the competition names. Best if you check that, first")
		print(Robot_TeamB[2222]['Competition Location'])
	elif Robot_Stat == "Awards" or Robot_Stat == "Awards Given":
		print("Flash!")
		print(Robot_TeamB[2222]['Award'])
	else:
		print("*Database.exe has stopped working. Try the code again. :P*")



elif Robot_Team == "3333":
	print(Robot_Stat)
	if Robot_Stat == "Location" or Robot_Stat == "Team Location":
		print("Here you go!")
		print(Robot_TeamB[3333]['Location'])
	elif Robot_Stat == "Rookie Year" or Robot_Stat == "Team Debut":
		print("Processing!")
		print(Robot_TeamB[3333]['Rookie'])
	elif Robot_Stat == "2019" or Robot_Stat == "Did they participate in the 2019 competition?":
		print("Voila!")
		print(Robot_TeamB[3333]['Participate?'])
	elif Robot_Stat == "Competitions" or Robot_Stat == "Names of Competitions":
		print("Bang!")
		print(Robot_TeamB[3333]['Competition'])
	elif Robot_Stat == "Locations of Competition" or Robot_Stat == "Competition Locations":
		print("Fresh from the oven! Note that these are in order with the competition names. Best if you check that, first")
		print(Robot_TeamB[3333]['Competition Location'])
	elif Robot_Stat == "Awards" or Robot_Stat == "Awards Given":
		print("Flash!")
		print(Robot_TeamB[3333]['Award'])
	else:
		print("*Database.exe has stopped working. Try the code again. :P*")


elif Robot_Team == "5555":
	print(Robot_Stat)
	if Robot_Stat == "Location" or Robot_Stat == "Team Location":
		print("Here you go!")
		print(Robot_TeamB[5555]['Location'])
	elif Robot_Stat == "Rookie Year" or Robot_Stat == "Team Debut":
		print("Processing!")
		print(Robot_TeamB[5555]['Rookie'])
	elif Robot_Stat == "2019" or Robot_Stat == "Did they participate in the 2019 competition?":
		print("Voila!")
		print(Robot_TeamB[5555]['Participate?'])
	elif Robot_Stat == "Competitions" or Robot_Stat == "Names of Competitions":
		print("Bang!")
		print(Robot_TeamB[5555]['Competitions'])
	elif Robot_Stat == "Locations of Competition" or Robot_Stat == "Competitions Location":
		print("Fresh from the oven! Note that these are in order with the competition names. Best if you check that, first")
		print(Robot_TeamB[5555]['Competition Location'])
	elif Robot_Stat == "Awards" or Robot_Stat == "Awards Given":
		print("Flash!")
		print(Robot_TeamB[5555]['Awards'])
	else:
		print("*Database.exe has stopped working. Try the code again. :P*")


else:
	print("Sorry! I didn't get that!")


'''
# Citrus Circuits location
location_1678 =  {'Location': 'Davis, CA, USA'} 
# 1678's first debut
rookie_1678 = {'Rookie Year': '2005'} 
# If 1678 participated in the 2019 competition or not
Season_2019_1678 = {'Participate?': 'Yes'}
# All the Competitions 1678 participated in
Names_1678 = {'Competition Names': [
		'Central Valley Regional',
		'Sacramento Regional',
		'Aerospace Valley Regional', 
		'Carver Division', 
		'Einstein Field', 
		'RCC Qianjiang International Robotics Invitational']} 
# Where each Competition was located.
C_Locate_1678 = {'Competition Location': [
		'Fresno, CA, USA', 
		'Davis, CA, USA', 
		'Lancaster, CA, USA', 
		'Houston, TX, USA', 
		'Houston TX, USA', 
		'Hangzhou, Zhejiang, China']}
# What Awards were they given?
Awards_1678 = {'Awards': [
		'Regional Chairman`s Award and Regional Winners', 
		'FIRST Dean`s List Finalist Award (Katie Stachowicz), Regional Winners, and Industrial Design Award sponsored by General Motors',
		'Regional Winners and Excellence in Engineering Award sponsored by Delphi', 'Championship Subdivision Winner and Entrepreneurship Award sponsored by Kleiner Perkins Caufield and Byers'
	,]}
team_1678 = [location_1678, rookie_1678, Season_2019_1678, Names_1678, C_Locate_1678, Awards_1678]


location_1111 = {'Show location': 'Edgewater, Maryland, USA'}
rookie_1111: {'Rookie Year': '2003'}, 
Season_2019_1111 = {'Participate?': 'True'}
Names_1111 = {'Competition Names': [
		'CHS District Bethesda MD Event sponsored by Bechtel',
		'CHS District Owings Mills MD Event sponsored by Leidos', 
		'FIRST Chesapeake District Championship']}
C_Locate_1111 = {'Competition Location': [
		'Bethesda, MD 20817, USA', 
		'Owings Mills, MD 21117, USA', 
		'Fairfax, VA 22030, USA']},
Awards_1111 = {'Awards': [
		'Autonomous Award sponsored by Ford', 
		'District Chairman`s Award', 
		'Team Spirit Award sponsored by FCA Foundation']}
team_1111 = [location_1111, rookie_1111, Season_2019_1111, Names_1111, C_Locate_1111, Awards_1111]

location_2222 =  {'Show location': 'Tacoma, WA, USA'} 
rookie_2222 = {'Rookie Year': '2007'}
Season_2019_2222 = {'Participate?': 'No'}
Names_2222 = {'Competition': 'Pacific Northwest Regional 2007'}
C_Locate_2222 = {'Location of Competition': 'Pioneer Courthouse Square in Portland, OR, USA'}
Awards_2222 = {'Award': 'None'}
team_2222 = [location_2222, rookie_2222, Season_2019_2222, Names_2222, C_Locate_2222, Awards_2222]

	
location_3333 = {'Show location': 'Julesburg, CO, USA'}
rookie_3333 = {'Rookie Year': '2010'}
Season_2019_3333 = {'Participate?': 'No'}
Names_3333 = {'Competition': 'Colorado Regional 2010'}
C_Locate_3333 = {'Location of Competition': 'Ritchie Center in Denver, CO, USA'} 
Awards_3333 = {'Award': 'Judges Award'}
	
team_3333 = [location_3333, rookie_3333, Season_2019_3333, Names_3333, C_Locate_3333, Awards_3333]

location_5555 = {'Show Location': 'Warren, Michigan'} 
rookie_5555 = {'Rookie Year': '2015'} 
Season_2019_5555 = {'Participate?': 'True'} 
Names_5555 = ['FIM District Center Line Event','FIM District Marysville Event']
C_Locate_5555 = ['Center Line, MI, USA', 'Marysville, MI, USA'] 
Awards_5555 = {'Award': 'District Event Winner'}
team_5555 = [location_5555, rookie_5555, Season_2019_5555, Names_5555, C_Locate_5555, Awards_5555]
'''