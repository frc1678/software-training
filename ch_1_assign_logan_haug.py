#This dictionary stores all of the information related to the teams,
#The Key of the main Dict is the team number, and its dictionary are its attributes
teamInfo = {
    "1678": {
        "Location" : "Davis, California, USA",
        "Rookie Year" : 2005,
        "Competed in 2019 Season" : True,
        "Competitions" : {
            "Central Valley Regional": "Fresno, CA, USA",
            "Sacramento Regional":"Davis, CA, USA",
            "Aerospace Valley Regional":"Lancaster, CA, USA",
            "2019 Championships":"Houston, TX, USA",
            "RCC Qianjiang International Robotics Invitational":"Hangzhou, Zhejiang, China"
        },
        "Awards in 2019 Season": ["Regional Chairman's Award", "Regional Winners","FIRST Dean's List Finalist Award (Katie Stachowicz)","Regional Winners","Industrial Design Award sponsored by General Motors","Regional Winners","Excellence in Engineering Award sponsored by Delphi","Championship Subdivision Winner","Entrepreneurship Award sponsored by Kleiner Perkins Caufield and Byers"]
    },
    "1": {
        "Location" : "Pontiac, Michigan, USA",
        "Rookie Year" : 1997,
        "Competed in 2019 Season" : True,
        "Competitions" : {
            "FIM District Center Line Event": "Center Line, MI, USA",
            "FIM District Troy Event": "Troy, MI, USA"
        },
        "Awards in 2019 Season": ["Imagery Award in honor of Jack Kamen"]
    },
    "4": {
        "Location" : "Van Nuys, California, USA",
        "Rookie Year" : 1997,
        "Competed in 2019 Season" : True,
        "Competitions" : {
            "Los Angeles North Regional": "Valencia, CA, USA",
            "Los Angeles Regional": "Los Angeles, CA 90015, USA",
            "Wings Over Camarillo": "Camarillo, CA, USA" ,
            "Battleship Blast": "San Pedro, CA, USA",
        },
        "Awards in 2019 Season": ["Quality Award sponsored by Motorola Solutions Foundation"]
    },
    "6": {
        "Location" : "Plymouth, MN, USA",
        "Rookie Year" : 1994,
        "Competed in 2019 Season" : False,
        "Competitions" : "No Competitions in the 2019 season",
        "Awards in 2019 Season": ["No awards in the 2019 season"]
    },
    "5": {
        "Location" : "Melvindale, MI, USA",
        "Rookie Year" : 1998,
        "Competed in 2019 Season" : True,
        "Competitions" : {
            "Big Bang!": "Taylor, MI, USA",
        },
        "Awards in 2019 Season": ["No awards in 2019 Season"]
    },
}
#Takes user team number, attribute, and prints it
uteam = input("enter an frc team: ")
uattribute = input("enter an attribute: ")
print(teamInfo[uteam][uattribute])
