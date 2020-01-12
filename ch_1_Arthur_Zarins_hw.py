#Reminder for self: to run python programs in Visual Studio code, use Cntrl + Fn + F5
teams = {
	'1678': {'Weight':200, 'Wheels': 4, 'Speed': 9},
	'2583': {'Weight': 300, 'Wheels': 325, 'Speed': 3}
}
def teamStats(teamName):
	print("Team " + teamName + " is awesome")
print(teams['1678']['Weight'])