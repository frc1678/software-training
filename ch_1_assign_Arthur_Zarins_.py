# Reminder for self: to run python programs in Visual Studio code, use Cntrl + Fn + F5
teams = {
    "1678": {'Last Year': 2019,
             'Location': "Davis CA",
             'Rookie Year': 2005,
             'Events': "Sac Regional, Central Valley Regional, AeroSpace Valley Regional, Carver division, Einstein field, RCC Qianjiang International Robotics Invitational, Chezy Champs"
             },
    "2551": {'Last Year': 2019,
             'Location': "Novato CA",
             'Rookie Year': 2008, 'Events':
                 'Sac Regional, SF Regional, Galileo divison'},
    "3421": {'Last Year': 2013,
             'Location': "Marysville MI",
             'Rookie Year': 2010,
             'Events': 'MI FRC state championship'},
    "2942": {'Last Year': 2018,
             'Location': "Seattle, WA",
             'Rookie Year': 2009,
             'Events': ''},
    "3890": {'Last Year': 2015,
             'Location': "Boulder, Colorado",
             'Rookie Year': 2003,
             'Events': 'Colorado Regional'}
}
#reference = "is"


def teamStats(teamName, attribute):
    # New variable refernce will handle grammer related to pluralities
    if (attribute == "Events" or  attribute == "Rookie Year" or  attribute == "Location" or attribute == "Last Year"):
        if(teamName in teams):
            reference = "is"
            stringTest = str(teams[teamName][attribute]).split(",")
            attributeDisplay = attribute
            if attribute == "Events" and len(stringTest) > 2:
                reference = "are"
            else:
                if attribute == "Events":
                    attributeDisplay = "only Event"
                reference = "is"

            print("Team " + str(teamName) + "'s " + str(attributeDisplay) +
                    " " + str(reference) + " " + str(teams[teamName][attribute]))


# The big test, comprised of 3 questions:
teamStats("1678", 'Location')
teamStats("1678", 'Events')
# Just one event: demonstration of proper grammer
teamStats("3421", 'Events')


def runContinuous():
    while(True):
        a1 = input("What is the team number?\n      ")
        a2 = input("What's the stat?\n      ")
        teamStats(a1, a2)

#If you want to run the program, uncomment the following line (commented so chapter 3 can work):
#runContinuous()
