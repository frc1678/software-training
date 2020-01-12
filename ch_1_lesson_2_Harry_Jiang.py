team_dict = {
	1: {
	    'location' : "Pontact, Michigan, USA",
	    "rookie_year" : 1997 ,
	    "2019_competition" : True,
	    "2019_competition_names" : [
	        'FIM Distric Center Line Event',
	        'FIM District Troy Event'
	    ],
	    "2019_competition_location" : [
	        'Center Line, MI,USA',
	        'Troy, MI, USA'],
	    "2019_awards" : False
	},


	20: {
	   'location' : "Clifton Park, New Yourk, USA",
	    "rookie_year" : 1992 ,
	    "2019_competition" : True,
	    "2019_competition_names" : [
	        'New York Tech Valley Regional',
	        'Hudson Valley Regional',
	        'Curie Division'],
	    "2019_competition_location" : ['Troy, NY, 12180, USA',
	    'Suffern, NY, USA',
	    'Detroit, MI, USA'],
	    "2019_awards" : False
	},

	4 :{
	    'location' : "Van Nuys, California, USA",
	    "rookie_year" : 1997,
	    "2019_competition" : True,
	    "2019_competition_names" : [
	        'Los Angeles North Regional',
	        'Los Angeles Regional', 'Wings Over Camarillo',
	        'Batlleship Blast'],
	    "2019_competition_location" : [
	        'Valencia, CA, USA',
	        'Los Angeles, CA, USA',
	        'Camarillo, CA, USA',
	        'San Pedro, CA, USA'],
	    "2019_awards" : False
	},

	5 :{
	    'location' : "Melvindale, MI, USA",
	    "rookie_year" : 1998,
	    "2019_competition" : True,
	    "2019_competition_names" : ['Big Bang!'],
	    "2019_competition_location" : ['Taylor, MI, USA'],
	    "2019_awards" : False
	},

	8 :{
	    'location' : 'Palo Alto, California, USA',
	    "rookie_year" : 1996,
	    "2019_compitition" : True,
	    "2019_competition_names" : [
	        'Del Mar Regional presented by Qualcomm',
	        'Great Northern Regional',
	        'Silicon Valley Regional'],
	    "2019_competition_location" : [
	        'Del Mar, CA, USA',
	        'Grand Forks, ND, USA',
	        'San Jose, CA, USA'],
	    "2019_awards" : False
	},

}
print("Search a team")
team_dictionary = input("what team number: ")
print("What field(location, rookie_year, 2019_competition, 2019_competition_names, 2019_competition_location, 2019_award")
team_field = input("what field: ")
print(team_dict[int(team_dictionary)][team_field])