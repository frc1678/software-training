teams = { 
	1678:{
		'location': 'Davis, CA, USA', 
		'rookie year': 2005, 
		'2019 compete': True , 
		'names and locations of 2019 competitions': {
			'Central Valley Regional': 'Fresno, CA, USA', 
			'Sacramento Regional': 'Davis, CA, USA', 
			'Aerospace Valley Regional': 'Lancaster, CA, USA', 
			'Carver Division': 'Houston, TX, USA', 
			'Einstein Field': 'Houston, TX, USA', 
			'RCC': 'Hangzhou, Zhejian, China', 
			'Chezy Champs': 'San Jose, CA, USA'
			}, 
		'2019 awards': [
			'Regional Chairmans', 
			'Regional Winner', 
			'Regional Winner', 
			'FIRST Deans List Finalist Award', 
			'Industrial Design Award', 
			'Regional Winner', 
			'Excellence in Engineering Award', 
			'Division Winner', 
			'Entrepreneurship Award'
			]
	},

	1323: {
		'location': 'Madera, CA, USA', 
		'rookie year': 2004, 
		'2019 compete': True , 
		'names and locations of 2019 competitions': {
			'Central Valley Regional': 'Fresno, CA, USA', 
			'Sacramento Regional': 'Davis, CA, USA', 
			'Newton Division': 'Houston, TX, USA', 
			'Einstein Field': 'Houston, TX, USA'
		},  
		'2019 awards': [
			'Regional Winner', 
			'Autonomous Award', 
			'Regional Winner', 
			'Quality Award', 
			'Division Winner', 
			'Industrial Design Award', 
			'Houston Champs Winner']
	},

	254: {
		'location': 'San Jose, CA, USA', 
		'rookie year': 1999, 
		'2019 compete': True , 
		'names and locations of 2019 competitions': {
			'San Francisco Regional': 'San Francisco, CA, USA', 
			'Silicon Valley Regional': 'San Jose, CA, USA', 
			'Turing Division': 'Houston, TX, USA', 
			'Einstein Field': 'Houston, TX, USA', 
			'Chezy Champs': 'San Jose, CA, USA'}, 
		'2019 awards': [
			'Regional Winner', 
			'Innovation in Control Award', 
			'Regional Winner', 
			'Excellence in Engineering Award', 
			'Division Winner', 
			'Industrial Design Award', 
			'Houston Champs Finalist']
	},

	3132: {
		'location': 'Sydney, New South Wales, Australia', 
		'rookie year': 2010, 
		'2019 compete': True , 
		'names and locations of 2019 competitions': {
			'Southern Cross Regional': 'Sydney Olympic Park, NSW, Australia', 
			'South Pacific Regional': 'Sydney Olympic Park, NSW, Australia',
		 	'Carver Division': 'Houston, TX, USA', 
		 	'Einstein Field': 'Houston, TX, USA'},
		'2019 awards': [
			'Woodie Flowers Finalist Award', 
			'Gracious Professionalism Award', 
			'Regional Engineering Inspiration Award', 
			'Safety Award','Division Winner']
		},

	3476:{
		'location': 'Irvine, CA, USA', 
		'rookie year': 2011, 
		'2019 compete': True , 
		'names and locations of 2019 competitions': {
			'Los Angeles Regional': 'Los Angeles, CA, USA', 
			'Aerospace Valley Regional': 'Lancaster, CA, USA', 
			'Hopper Division': 'Houston, TX, USA', 
			'Battleship Blast': 'San Pedro, CA, USA',
	 		'Chezy Champs': 'San Jose, CA, USA', 
	 		'Beach Blitz': 'Huntington Beach, CA, USA'}, 
	 	'2019 awards': [
			'Gracious Professionalism Award', 
			'Autonomous Award', 
			'Regional Winner', 
			'Quality Award']
	}
}
team_num = int(input("Team number: "))
attribute = input("Attribute: ")
print(teams[team_num][attribute]) 