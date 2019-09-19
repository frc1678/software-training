Robot_Team = input("What Robotics Team do you want to look into?")
"""
Robot_Location =
Robot_Debut
Robot_2019
Robot_comp_names
Robot_comp_locate
Robot_comp_award
"""

team_1678 = {'Location': {'Show location': 'Davis, CA, USA'}, 'Rookie': {'Rookie Year': '2005'}, 'Season 2019': {'Participate?': 'True'},
	'Competition Names': ['Central Valley Regional', 'Sacramento Regional', 'Aerospace Valley Regional', 'Carver Division', 'Einstein Field', 'RCC Qianjiang International Robotics Invitational'], 
	'Competition Location': ['Fresno, CA, USA', 'Davis, CA, USA', 'Lancaster, CA, USA', 'Houston, TX, USA', 'Houston TX, USA', 'Hangzhou, Zhejiang, China'],
	'Awards': ['Regional Chairman`s Award and Regional Winners', 'FIRST Dean`s List Finalist Award (Katie Stachowicz), Regional Winners, and Industrial Design Award sponsored by General Motors',
	'Regional Winners and Excellence in Engineering Award sponsored by Delphi', 'Championship Subdivision Winner and Entrepreneurship Award sponsored by Kleiner Perkins Caufield and Byers',]}

team_1111 = {'Location': {'Show location': 'Edgewater, Maryland, USA'}, 'Rookie': {'Rookie Year': '2003'}, 'Season 2019': {'Participate?': 'True'},
	'Competition Names': ['CHS District Bethesda MD Event sponsored by Bechtel', 'CHS District Owings Mills MD Event sponsored by Leidos', 'FIRST Chesapeake District Championship'],
	'Competition Location': ['Bethesda, MD 20817, USA', 'Owings Mills, MD 21117, USA', 'Fairfax, VA 22030, USA'],
	'Awards': ['Autonomous Award sponsored by Ford', 'District Chairman`s Award', 'Team Spirit Award sponsored by FCA Foundation']}

team_2222 = {'Location': {'Show location': 'Tacoma, WA, USA'}, 'Rookie': {'Rookie Year': '2007'}, 'Season 2019': {'Participate?': 'False'},
	'Competition Names': {'Competition': 'Pacific Northwest Regional 2007'}, 'Competition Location': {'Location of Competition': 'Pioneer Courthouse Square in Portland, OR, USA'},
	'Awards': {'Award': 'None'}}

team_3333 = {'Location': {'Show location': 'Julesburg, CO, USA'}, 'Rookie': {'Rookie Year': '2010'}, 'Season_2019': {'Participate?': 'False'},
	'Competition Names': {'Competition': 'Colorado Regional 2010'}, 'Competition Location': {'Location of Competition': 'Ritchie Center in Denver, CO, USA'},
	'Awards': {'Award': 'Judges Award'}}

team_5555 = {'Location': {'Show Location': 'Warren, Michigan'}, 'Rookie': {'Rookie Year': '2015'}, 'Season 2019': {'Participate?': 'True'},
	'Competition Names': ['FIM District Center Line Event','FIM District Marysville Event'], 'Competition Location': ['Center Line, MI, USA', 'Marysville, MI, USA'], 
	'Awards': {'Award': 'District Event Winner'}}


print(Robot_Team)
if Robot_Team == "1678":
	print("Here's their profile!")
	print(team_1678)

elif Robot_Team == "1111":
	print("Here's their profile!")
	print(team_1111)

elif Robot_Team == "2222":
	print("Here's their profile!")
	print(team_2222)


elif Robot_Team == "3333":
	print("Here's their profile!")
	print(team_3333)

elif Robot_Team == "5555":
	print("Here's their profile!")
	print(team_5555)

else:
	print("Sorry! I didn't get that!")


"""
team_1678_location = {'Show location': 'Davis'}
team_1678_rookie_year = 
team_1678_season_par = 
team_1678_comp_names = 

"""