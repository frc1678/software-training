teams = {
	1: {"location": "Pontiac, Michigan, USA", 
		"rookie year": 1997,
		"competed in 2019 season": True,
		"2019 competitions and locations": {"FIM District Center Line Event", "Center Line, MI, USA".
											"FIM District Troy Event", "Troy, MI, USA".
											}
		"2019 season awards": {"Imagery Award"}
		}
	16: {"location": "Mountain Home, Arkansas, USA",
		"rookie year": 1996,
		"competed in 2019 season": True,
		"2019 competitions and locations": {"Midwest Regional", "Chicago, IL, USA". 
											"Rocket City Regional", "Huntsville, AL, USA".
											"Darwin Division", "Detroit, MI, USA".
											}
		"2019 season awards": {"Industrial Design Award", "Regional Finalists", "Excellence in Engineering Award"}
	}
	253: {"location": "Millbrae, California, USA",
		  "rookie year": 1999,
		  "competed in 2019 season": True,
		  "2019 competitions and locations": {"San Fransisco Regional", "San Fransisco, California, USA".
		  									  "Monterey Bay Regional", "Seaside, CA, USA".
		  									  "Newton Division", "Houston, TX, USA".
		  									  }
		  "2019 season awards": {"Team Spirit Award"}
	}
	342: {"location": "North Charleston, South Carolina, USA",
		  "rookie year": 2000,
		  "competed in 2019 season": True,
		  "2019 competitions and locations": {"Palmetto Regional", "Myrtle Beach, SC USA".
		  									  "Rocket City Regional", "Huntsville, AL, USA".
		  									}
		  "2019 season awards": False 
	}
	554: {"location": "Ft. Thomas, Kentucky, USA",
		  "rookie year": 2001,
		  "competed in 2019 season": True,
		  "2019 competitions and locations": {"Miami Valley Regional", "Dayton, OH, USA".
		  									  }
		  "2019 season awards": False 
	}
requested_team_number = input("Team Number: ")
requested_team_information = input(requested_team_number + "information: ")
print([teams][requested_team_number][requested_team_information])