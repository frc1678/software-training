teams = { #Stores all the teams with string form of team number as key
    1: {
        "location": "Pontiac, Michigan, USA",
        "rookie_year": 1997,
        "competed_2019": True,
        "2019_comps": [
            "FIM District Center Line Event 2019",
            "FIM District Troy Event 2019",
        ],
        "comp_locations": [
            "Center Line, MI, USA",
            "Troy, MI, USA",
        ],
        "2019_awards": [
            "Imagery Award in honor of Jack Kamen",
        ],
    },
    16: {
        "location": "Mountain Home, Arkansas, USA",
        "rookie_year": 1996,
        "competed_2019": True,
        "2019_comps": [
            "Midwest Regional",
            "Rocket City Regional 2019",
            "Darwin Division 2019",
        ],
        "comp_locations": [
            "Chicago, IL, USA",
            "Huntsville, AL, USA",
            "Detriot, MI, USA",
        ],
        "2019_awards": [
            "Industrial Design Award sponsored by General Motors",
            "Regional Finalists",
            "Excellence in Engineering Award sponsored by Delphi",
        ],
    },
    253: {
            "location": "Millbrae, California, USA",
            "rookie_year": 1999,
            "competed_2019": True,
            "2019_comps": [
                "San Fransisco Regional",
                "Monterey Bay Regional",
                "Newton Divison",
            ],
            "comp_locations": [
            "San Fransisco, CA, USA",
            "Seaside, CA, USA",
            "Houston, TX, USA",
        ],
            "2019_awards": [
                "Team Spirit Award sponsored by FCA Foundation",
            ],
    },
	342: {
        "location": "North Charleston, South Carolina, USA",
            "rookie_year": 2000,
            "competed_2019": True,
            "2019_comps": [
                "Palmetto Regional 2019",
                "Rocket City Regional 2019",
            ],
            "comp_locations": [
            "Myrtle Beach, SC, USA",
            "Huntsville, AL, USA",
        ],
            "2019_awards": [],
    },
    554: {
        "location": "Ft. Thomas, Kentucky, USA",
            "rookie_year": 2001,
            "competed_2019": True,
            "2019_comps": [
                "Miami Valley Regional 2019",
            ],
            "comp_locations": [
            "Fairborn, OH, USA",
        ],
            "2019_awards": [],
    }
}

#Attributes that can be input as keys, their discription as values
valid_requests = { 
    "location": "Team's location",
    "rookie_year": "Team's rookie year",
    "competed_2019": "Seeing if team competed in 2019",
    "2019_comps": "A list of the competitions the team competed in for 2019",
    "comp_locations": "The location of the 2019 competitions",
    "2019_awards": "Awards won during the 2019 season",
}


print("Valid teams:")
print(" ".join(map(str, teams.keys()))) #Print teams seperated by spaces onto one line 
requested_team_number = ""

while requested_team_number == "": #loop until valid input
    requested_team_number = input("Team Number: ")
    if requested_team_number.isdigit(): #Tests if input is only digits
        if int(requested_team_number) in teams:
            team_number = int(requested_team_number)
        else:
            print(f"Team number '{requested_team_number}' not stored.")
            requested_team_number = ""
            
    else:
        print(f"Invalid team number '{requested_team_number}'")
        requested_team_number = ""


print("Valid Requests:")
for attribute in valid_requests: #loop through keys in valid_attributes
    print(f"'{attribute}' for {valid_requests[attribute]}") #prints name/function
requested_attribute = ""
while requested_attribute == "": #loop until valid input
    #Case insensitive input, spaces replaced w/underscore
    requested_attribute = input("Attribute: ").lower().replace(" ", "_")

    if requested_attribute not in valid_requests:
        print(f"Attribute {requested_attribute} not recognized.")
        requested_attribute = ""

requested_attribute_value = teams[team_number][requested_attribute]
print(f"Team {requested_team_number}'s {requested_attribute}:")
if isinstance(requested_attribute_value, list):
    for value in requested_attribute_value:
        print(value)
else:
    print(requested_attribute_value)