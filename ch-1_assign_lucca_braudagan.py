teams={
	1678:{
		"team_name":"Citrus Circuits",
		"location":"Davis, CA", 
		"rookie_year":2005, 
		"competed_in_2019_season":True, 
		"2019_competition_names":[
			"Central Valley Regional",
			"Sacramento Regional",
			"Aerospace Valley Regional",
			"Carver Division",
			"Einstein Field",
			"RCC Qianjiang International Robotics Invitational",
			"Chezy Champs"],
		"2019_competition_locations":[
			"Fresno, CA",
			"Davis, CA",
			"Lancaster, CA",
			"Houston, TX",
			"Houston, TX, Again"
			"Hangzhou, Zhejiang, China",
			"San Jose, CA"],
		"2019_season_awards":[
			"Regional Chairman's Award At Central Valley Regional",
			"Regional Winners At Central Valley Regional",
			"FIRST Dean's List Finalist Award",
			"Regional Winners At Sacramento Regional",
			"Industrial Design Award Sponsored By General Motors",
			"Regional Winners At Aerospace Valley Regional",
			"Excellence In Engineering Award Sponsered By Delphi",
			"Championship Subdivision Winner In Carver Divison",
			"Entrepreneurship Award Sponsored By Kleiner Perkins Caufield And Byers"]
	},
	4322:{
		"team_name":"Clockwork Oranges",
		"location":"Orange, CA",
		"rookie_year":2012,
		"competed_in_2019_season":True,
		"2019_competition_names":[
			"San Diego Regional Presented By Qualcomm",
			"Las Vegas Regional",
			"Einstein Field",
			"Battleship Blast Monday",
			"Beach Blitz"],
		"2019_competition_locations":[
			"Del Mar, CA",
			"Las Vegas, NV",
			"Houston, TX",
			"San Pedro, CA",
			"Huntington Beach, CA"],
		"2019_season_awards":[
			"FIRST Dean's List Finalist Award",
			"FIRST Dean's List Award"]
	},
	5458:{
		"team_name":"Digital Minds",
		"location":"Woodland, CA",
		"rookie_year":2015,
		"competed_in_2019_season":True,
		"2019_competition_names":[
			"Central Valley Regional",
			"Sacramento Regional"],
		"2019_competition_locations":[
			"Fresno, CA",
			"Davis, CA"],
		"2019_season_awards":"None"
	},
	1:{
		"team_name":"The Juggernauts",
		"location":"Pontiac, MI",
		"rookie_year":1997,
		"competed_in_2019_season":True,
		"2019_competition_names":[
			"FIM District Center Line Event",
			"FIM District Troy Event"],
		"2019_competition_locations":[
			"Center Line, MI",
			"Troy, MI"],
		"2019_season_awards":"Imagery Award In Honor Of Jack Kamen"
	},
	7229:{
		"team_name":"Electronic Eagles",
		"location":"Sacramento, CA",
		"rookie_year":2018,
		"competed_in_2019_season":True,
		"2019_competition_names":"Sacramento Regional",
		"2019_competition_locations":"Davis, CA",
		"2019_season_awards":"None"
	}
}
team_number=int(input("Team Number (options are '1', '1678', '4322', '5458', '7229'):"))
team_information=input("Category (options are 'team_name', 'location', 'rookie_year', 'competed_in_2019_season','2019_competition_names', '2019_competition_locations', '2019_season_awards':")
print(teams[team_number][team_information])