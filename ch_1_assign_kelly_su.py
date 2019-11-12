teams = {
	1: {
		'location': 'Pontiac, Michigan, USA.', 
		'rookie year': 1997,
		'competed in 2019 season': True,
		'2019 competitions': ['FIM District Center Line Event: Center Line, MI, USA.',
										 	'FIM District Troy Event: Troy, MI, USA.'],
		'2019 season awards':'Imagery Award'
	},
	16: {
		'location': 'Mountain Home, Arkansas, USA.',
		'rookie year': 1996,
		'competed in 2019 season': True,
		'2019 competitions': ['Midwest Regional: Chicago, IL, USA.',
											'Rocket City Regional: Huntsville, AL, USA.',
											'Darwin Division: Detroit, MI, USA.'],
		'2019 season awards': 'Industrial Design Award, Regional Finalists, Excellence in Engineering Award'
	},
	253: {
		'location': 'Millbrae, California, USA.',
		'rookie year': 1999,
		'competed in 2019 season': True,
		'2019 competitions': ['San Fransisco Regional: San Fransisco, California, USA.',
		  									  'Monterey Bay Regional: Seaside, CA, USA.',
		  									  'Newton Division: Houston, TX, USA.'],		  
		'2019 season awards': 'Team Spirit Award'
	},
	342: {'location': 'North Charleston, South Carolina, USA.',
		  'rookieyear': 2000,
		  'competed in 2019 season': True,
		  '2019 competitions': ['Palmetto Regional: Myrtle Beach, SC USA.',
		  									  'Rocket City Regional: Huntsville, AL, USA.'],
		  '2019 season awards': False 
	},
	554: {
		'location': 'Ft. Thomas, Kentucky, USA.',
		'rookie year': 2001,
		'competed in 2019 season': True,
		'2019 competitions': ['Miami Valley Regional: Dayton, OH, USA.'],
		'2019 season awards': False 
	},
}

input_team = int(input("Out of teams 1, 16, 253, 342, and 554, which one would you like to view?\n==>"))
input_requested_information = input(
"""What would you like to know about this team?
   Please enter one of the following: 
   location  
   rookie year  
   competed in 2019 season   
   2019 competitions
   2019 season awards\n==>""")
if isinstance(teams[input_team][input_requested_information], list):
	print("\n".join(teams[input_team][input_requested_information]))
else:
	print(teams[input_team][input_requested_information])										




