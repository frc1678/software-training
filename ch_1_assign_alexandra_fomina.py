robot_information = { 
 'one' : {
	'location': 'Pontiac, Michigan',
 	'rookie_year' : '1997' , 
 	'2019_competition' : 'true',
 	'comp_location' : 'Michigan',
 	'awards' : 'none'
 },
 'four' : {
 	'location' : 'Van Nuys, California',
 	'rookie_year' : '1997',
	'2019_competition' : 'true',
	'comp_location' : 'Valencia, Los Angeles, Camarillo, San Pedro',
	'awards' : 'Quality'
 },
 'five' : {
 	'location' : 'Melvindale, Michigan',
 	'rookie_year' : '1998',
 	'2019_competition' : 'true',
 	'comp_location' : 'Michigan',
 	'awards' : 'none'
 },
 'six' : {
 	'location' : 'Plymouth, Minnesota',
 	'rookie_year' : '1994',
 	'2019_competition' : 'false',
 	'comp_location' : 'none',
 	'awards' : 'none'
 },
 'seven' : { 
 	'location' : 'Baltimore Maryland',
 	'rookie_year' : '1997',
 	'2019_competition' : 'none',
 	'comp_location' : 'none',
 	'awards' : 'none',
 }
}
team_number = input("What is the team number? ")
team_attribute = input("What is the team attribute? ")
print(robot_information[team_number] [team_attribute])
