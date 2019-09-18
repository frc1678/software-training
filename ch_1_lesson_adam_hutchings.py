list_1111 = [
	'Edgewater, Maryland',2003,True,['CHS District Bethesda MS Event sponsored by Bechtel', #Just tons of lists until line 23
	'CHS District Owings Mills MD Event sponsored by Leidos','FIRST Chesapeake District Championship'],
	['Bethesda, Maryland','Owings Mills, Maryland','Fairfax, Virginia'],
	['Autonomous Award sponsored by Ford',"District Chairman's Award",'Team Spirit Award sponsored by FCA Foundation']]

list_1678 = [
	'Davis, California',2005,True,
	['Central Valley Regional','Sacramento Regional','Aerospace Valley Regional','Carver Division','Einstein Field',
	'RCC Qianjiang International Robotics Invitational'],['Fresno, California','Davis, California','Lancaster, California',
	'Houston, Texas','Hangzhou, China'],["Regional Chairman's Award",'Regional Winners',"FIRST Dean's List Finalist Award",
	'Industrial Design Award sponsored by General Motors','Excellence in Engineering Award sponsored by Delphi',
	'Championship Subdivision Winner','Entrepeneurship Award sponsored by Kleiner Perkins Caufield and Byers']]

list_2222 = [
	'Tacoma, Washington',2007,False,"Pacific Northwest Regional",'Portland, Oregon','No awards. Boo-hoo...']

list_3333 = [
	'Julesburg, Colorado',2010,False,"Colorado Regional",'Denver, Colorado','Judges Award']

list_5555 = [
	'Warren, Michigan',2015,True,['FIM District Center Line Event','FIM District Marysville Event'],
	['Center Line, Michigan','Marysville, Michigan'],"District Event Winner"]

valid_input_1 = False #Whether a valid input has been submitted for a team
valid_input_2 = False #Whether a valid input has been submitted for a statistic

statistics_dictionary = {'location':0, 'rookie_year':1, 'competed':2, 'competition_names':3,
'competition_locations':4, 'season_awards':5}


while valid_input_1 == False: #Until a valid input has been submitted for a team
	team_selection = str(input("What team would you like to view statistics about? ")) #Which team do you want?
	if team_selection == '1111' or '1678' or '2222' or '3333' or '5555': #Breaking the loop for a valid input
		valid_input_1 = True
if team_selection == '1111':
	team_selection = list_1111
if team_selection == '1678':
	team_selection = list_1678
if team_selection == '2222':
	team_selection = list_2222
if team_selection == '3333':
	team_selection = list_3333
if team_selection == '5555':
	team_selection = list_5555

while valid_input_2 == False: #Until a valid input has been submitted for a statistic
	statistic_wanted = input("Which statistic would you like to find out? ") #Which statistic do you want?
	if statistic_wanted == 'location' or 'rookie_year' or 'competed' or 'competition_names' or 'competition_locations' or 'season_awards': #Breaking the loop for a valid input
		valid_input_2 = True #Breako el infinito el loopo

print(team_selection[statistics_dictionary[statistic_wanted]]) #Print the list selected, and the element of said list
