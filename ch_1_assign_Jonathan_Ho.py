Robot_Team = int(input("What Robotics Team do you want to look into?"))
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

print(Robot_TeamB[Robot_Team][Robot_Stat])
