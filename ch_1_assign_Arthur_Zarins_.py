#Reminder for self: to run python programs in Visual Studio code, use Cntrl + Fn + F5
teams = {
	'1678': {'Last Year': 2019,
            'Location': "Davis CA",
            'Rookie Year': 2005,
            'Events': 'Sac Regional, Central Valley Regional, AeroSpace Valley Regional, Carver division, Einstein field, RCC Qianjiang International Robotics Invitational, Chezy Champs'
            },
	'2551': {'Last Year': 2019, 
            'Location': "Novato CA", 
            'Rookie Year': 2008, 'Events': 
            'Sac Regional, SF Regional, Galileo divison'},
    '3421': {'Last Year': 2013, 
            'Location': "Marysville MI", 
            'Rookie Year': 2010, 
            'Events': 'MI FRC state championship'},
    '2942': {'Last Year': 2018, 
            'Location': "Seattle, WA", 
            'Rookie Year': 2009,
            'Events': ''}
}
#reference = "is"
def teamStats(teamName, attribute):
    #New variable refernce will handle grammer related to pluralities
    reference = "is"
    stringTest = teams[teamName][attribute].split()
    attributeDisplay = attribute
    if attribute == "Events" and len(stringTest) > 2:
        reference = "are"
    else:
        if attribute == "Events":
            attributeDisplay = "only Event"
        reference = "is"
    print("Team " + teamName + "'s " + attributeDisplay + " " + reference + " " + teams[teamName][attribute])

#The big test, comprised of 3 questions:
teamStats('1678', 'Location')
teamStats('1678', 'Events')
#Just one event: demonstration of proper grammer
teamStats('3421', 'Events')