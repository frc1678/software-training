teams = { 
	'1678': {
		'location': 'Davis, CA, USA', 
		'rookie year': 2005, 
		'2019 compete': True , 
		'names of 2019 competitions': [
			'Central Valley Regional', 
			'Sacramento Regional', 
			'Aerospace Valley Regional', 
			'Carver Division', 
			'Einstein Field', 
			'RCC', 
			'Chezy Champs'
			], 
		'location of 2019 competitions': [
			'Fresno, CA, USA', 
			'Davis, CA, USA', 
			'Lancaster, CA, USA', 
			'Houston, TX, USA', 
			'Houston, TX, USA', 
			'Hangzhou, Zhejian, China', 
			'San Jose, CA, USA'
			], 
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

	'1323': {
		'location': 'Madera, CA, USA', 
		'rookie year': 2004, 
		'2019 compete': True , 
		'names of 2019 competitions': [
			'Central Valley Regional', 
			'Sacramento Regional', 
			'Newton Division', 
			'Einstein Field'
		], 
		'location of 2019 competitions': [
			'Fresno, CA, USA', 
			'Davis, CA, USA', 
			'Houston, TX, USA', 
			'Houston, TX, USA'
		], 
		'2019 awards': [
			'Regional Winner', 
			'Autonomous Award', 
			'Regional Winner', 
			'Quality Award', 
			'Division Winner', 
			'Industrial Design Award', 
			'Houston Champs Winner']
	},

	'254': {
		'location': 'San Jose, CA, USA', 
		'rookie year': 1999, 
		'2019 compete': True , 
		'names of 2019 competitions': [
			'San Francisco Regional', 
			'Silicon Valley Regional', 
			'Turing Division', 
			'Einstein Field', 
			'Chezy Champs'], 
		'location of 2019 competitions': [
			'San Francisco, CA, USA', 
			'San Jose, CA, USA', 
			'Houston, TX, USA', 
			'Houston, TX, USA', 
			'San Jose, CA, USA'], 
		'2019 awards': [
			'Regional Winner', 
			'Innovation in Control Award', 
			'Regional Winner', 
			'Excellence in Engineering Award', 
			'Division Winner', 
			'Industrial Design Award', 
			'Houston Champs Finalist']
	},

	'3132': {
		'location': 'Sydney, New South Wales, Australia', 
		'rookie year': 2010, 
		'2019 compete': True , 
		'names of 2019 competitions': [
			'Southern Cross Regional', 
			'South Pacific Regional',
		 	'Carver Division', 
		 	'Einstein Field'],
		'location of 2019 competitions': [
		 	'Sydney Olympic Park, NSW, Australia', 
			'Sydney Olympic Park, NSW, Australia',
			'Houston, TX, USA', 
			'Houston, TX, USA'], 
		'2019 awards': [
			'Woodie Flowers Finalist Award', 
			'Gracious Professionalism Award', 
			'Regional Engineering Inspiration Award', 
			'Safety Award','Division Winner']
		},
	'3476:' {
		'location': 'Irvine, CA, USA', 
		'rookie year': 2011, 
		'2019 compete': True , 
		'names of 2019 competitions': [
			'Los Angeles Regional', 
			'Aerospace Valley Regional', 
			'Hopper Division', 
			'Battleship Blast',
	 		'Chezy Champs', 
	 		'Beach Blitz'], 
	 	'location of 2019 competitions': [
	 		'Los Angeles, CA, USA', 
			'Lancaster, CA, USA', 
			'Houston, TX, USA', 
			'San Pedro, CA, USA', 
			'San Jose, CA, USA', 
			'Huntington Beach, CA, USA'], 
		'2019 awards': [
			'Gracious Professionalism Award', 
			'Autonomous Award', 
			'Regional Winner', 
			'Quality Award']
	}
}
team_num = input("Team number: ")
attribute = input("Attribute: ")
print(teams[team_num][attribute]) 