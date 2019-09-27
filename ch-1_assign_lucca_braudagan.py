teams = {
	1678 : {
		"team_name" : "Citrus Circuits",
		"location" : "Davis, CA", 
		"rookie_year" : 2005, 
		"competed_in_2019_season" : True, 
		"2019_competition_names_and_locations" : {
			"Central Valley Regional" : "Fresno, CA",
			"Sacramento Regional" : "Davis, CA",
			"Aerospace Valley Regional" : "Lancaster, CA",
			"Carver Division" : "Houston, TX",
			"Einstein Field" : "Houston, TX",
			"RCC Qianjiang International Robotics Invitational" : "Hangzhou, Zhejiang, China",
			"Chezy Champs" : "San Jose, CA"
		},
		"2019_season_awards" : [
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
	4322 : {
		"team_name" : "Clockwork Oranges",
		"location" : "Orange, CA",
		"rookie_year" : 2012,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"San Diego Regional Presented By Qualcomm" : "Del Mar, CA",
			"Las Vegas Regional" : "Las Vegas, NV",
			"Einstein Field" : "Houston, TX",
			"Battleship Blast Monday" : "San Pedro, CA",
			"Beach Blitz" : "Huntington Beach, CA"
		},
		"2019_season_awards" : [
			"FIRST Dean's List Finalist Award",
			"FIRST Dean's List Award"]
	},
	5458 : {
		"team_name" : "Digital Minds",
		"location" : "Woodland, CA",
		"rookie_year" : 2015,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"Central Valley Regional" : "Fresno, CA",
			"Sacramento Regional" : "Davis, CA"
		},
		"2019_season_awards" : "None"
	},
	1 : {
		"team_name" : "The Juggernauts",
		"location" : "Pontiac, MI",
		"rookie_year" : 1997,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"FIM District Center Line Event" : "Center Line, MI",
			"FIM District Troy Event" : "Troy, MI"
		},
		"2019_season_awards":"Imagery Award In Honor Of Jack Kamen"
	},
	7229 : {
		"team_name" : "Electronic Eagles",
		"location" : "Sacramento, CA",
		"rookie_year" : 2018,
		"competed_in_2019_season" : True,
		"2019_competition_names_and_locations" : {
			"Sacramento Regional" : "Davis, CA"
		}, 
		"2019_season_awards" : "None"
	}
}
team_number = int (input("Team Number (options are '1', '1678', '4322', '5458', '7229'):"))
team_information = input("Category (options are 'team_name', 'location', 'rookie_year', 'competed_in_2019_season','2019_competition_names_and_locations', '2019_season_awards':")
print(teams[team_number][team_information])