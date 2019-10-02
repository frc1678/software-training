robot_information = { 
#I'm using a dictionary because it allows to give variables a key
#I created a list for awards in case thaqt there are more awards to add later on
 1 : {
	'location': 'Pontiac, Michigan',
 	'rookie_year' : '1997' , 
 	'2019_competition' : True,
 	'comp_location' : 'Michigan',
 	'awards' : []
  },
 4 : {
 	'location' : 'Van Nuys, California',
 	'rookie_year' : '1997',
	'2019_competition' : False,
	'comp_location' : 'Valencia, Los Angeles, Camarillo, San Pedro',
	'awards' : ['Quality']
  },
 5 : {
 	'location' : 'Melvindale, Michigan',
 	'rookie_year' : '1998',
 	'2019_competition' : True,
 	'comp_location' : 'Michigan',
 	'awards' : []
  },
 6 : {
 	'location' : 'Plymouth, Minnesota',
 	'rookie_year' : '1994',
 	'2019_competition' : False,
 	'comp_location' : 'none',
 	'awards' : []
  },
  7 : { 
 	'location' : 'Baltimore Maryland',
 	'rookie_year' : '1997',
 	'2019_competition' : False,
 	'comp_location' : 'none',
 	'awards' : [],
  }
}
team_number = int(input("What is the team number? "))
team_attribute = input("What is the team attribute? ")
print(robot_information[team_number] [team_attribute])
