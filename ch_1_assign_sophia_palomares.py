def team_info():
	teams = input("What team would you like to look up? options: 1678, 1682, 1690, 1700, 2907, 3132 ")
	#1678
	if(teams == "1678"):
		print("You chose team 1678, or Citrus Circuits")
		info_question_1678 = input("Would you like to know about the team ")
		if(info_question_1678 == "rookie year"):
			print(rookie[1678])
			team_info()
		elif(info_question_1678 == "location"):
			print(location[1678])
			team_info()
		elif(info_question_1678 == "competed in 2019"):
			if(compete_1678 == True):
				print("Yes, this team did compete in 2019")
				comp_1678_question = input("Would you like to know the competitions this team competed in?")
				if (comp_1678_question == "yes"):
					print(competitions_1678)
					comp_location_question_1678 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_1678 == "yes"):
						print(competitions_locations_1678["1"])
						print(competitions_locations_1678["2"])
						print(competitions_locations_1678["3"])
						print(competitions_locations_1678["4"])
						print(competitions_locations_1678["5"])
						team_info()
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
				team_info()
		elif(info_question_1678 == "awards in 2019"):
			print(awards_1678)
			team_info()
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
			team_info()
	#1682
	elif(teams == "1682"):
		print("You chose team 1682, or Eye Bots")
		info_question_1682 = input("Would you like to know about the team ")
		if(info_question_1682 == "rookie year"):
			print(rookie[1682])
			team_info()
		elif(info_question_1682 == "location"):
			print(location[1682])
			team_info()
		elif(info_question_1682 == "competed in 2019"):
			if(compete_1682 == True):
				print("Yes, this team did compete in 2019")
				comp_1682_question = input("Would you like to know the competitions this team competed in?")
				if (comp_1682_question == "yes"):
					print(competitions_1682)
					comp_location_question_1682 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_1682 == "yes"):
						print(competitions_locations_1682["1"])
						team_info()
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
				team_info()
		elif(info_question_1682 == "awards in 2019"):
			print(awards_1682)
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
	#1690
	elif(teams == "1690"):
		print("You chose team 1690, or Orbit")
		info_question_1690 = input("Would you like to know about the team ")
		if(info_question_1690 == "rookie year"):
			print(rookie[1690])
			team_info()
		elif(info_question_1690 == "location"):
			print(location[1690])
			team_info()
		elif(info_question_1690 == "competed in 2019"):
			if(compete_1690 == True):
				print("Yes, this team did compete in 2019")
				comp_1690_question = input("Would you like to know the competitions this team competed in?")
				if (comp_1690_question == "yes"):
					print(competitions_1690)
					comp_location_question_1690 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_1690 == "yes"):
						print(competitions_locations_1690["1"])
						print(competitions_locations_1690["2"])
						print(competitions_locations_1690["3"])
						print(competitions_locations_1690["4"])
						print(competitions_locations_1690["5"])
						team_info()
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
				team_info()
		elif(info_question_1690 == "awards in 2019"):
			print(awards_1690)
			team_info()
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
			team_info()
	#1700
	elif(teams == "1700"):
		print("You chose team 1700, or Gatorbotics")
		info_question_1700 = input("Would you like to know about the team ")
		if(info_question_2907 == "rookie year"):
			print(rookie[1700])
			team_info()
		elif(info_question_1700 == "location"):
			print(location[1700])
			team_info()
		elif(info_question_1700 == "competed in 2019"):
			if(compete_1700 == True):
				print("Yes, this team did compete in 2019")
				comp_1700_question = input("Would you like to know the competitions this team competed in?")
				if (comp_1700_question == "yes"):
					print(competitions_1700)
					comp_location_question_1700 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_1700 == "yes"):
						print(competitions_locations_1700["1"])
						print(competitions_locations_1700["2"])
						print(competitions_locations_1700["3"])
						print(competitions_locations_1700["4"])
						print(competitions_locations_1700["5"])
						print(competitions_locations_1700["6"])
						print(competitions_locations_1700["7"])
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
		elif(info_question_1700 == "awards in 2019"):
			print(awards_1700)
			team_info()
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
			team_info()
	#2907
	elif(teams == "2907"):
		print("You chose team 2907, or Lion Robotics")
		info_question_2907 = input("Would you like to know about the team ")
		if(info_question_2907 == "rookie year"):
			print(rookie[2907])
			team_info()
		elif(info_question_2907 == "location"):
			print(location[2907])
			team_info()
		elif(info_question_2907 == "competed in 2019"):
			if(compete_2907 == True):
				print("Yes, this team did compete in 2019")
				comp_2907_question = input("Would you like to know the competitions this team competed in?")
				if (comp_2907_question == "yes"):
					print(competitions_2907)
					comp_location_question_2907 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_2907 == "yes"):
						print(competitions_locations_2907["1"])
						print(competitions_locations_2907["2"])
						print(competitions_locations_2907["3"])
						team_info()
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
				team_info()
		elif(info_question_2907 == "awards in 2019"):
			print(awards_2907)
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
	#3132
	elif(teams == "3132"):
		print("You chose team 3132, or Thunder Down Under")
		info_question_3132 = input("Would you like to know about the team ")
		if(info_question_3132 == "rookie year"):
			print(rookie[3132])
			team_info()
		elif(info_question_3132 == "location"):
			print(location[3132])
			team_info()
		elif(info_question_3132 == "competed in 2019"):
			if(compete_3132 == True):
				print("Yes, this team did compete in 2019")
				comp_3132_question = input("Would you like to know the competitions this team competed in? ")
				if (comp_3132_question == "yes"):
					print(competitions_3132)
					comp_location_question_3132 = input("Would you like to know where those competitions are located? ")
					if(comp_location_question_3132 == "yes"):
						print(competitions_locations_3132["1"])
						print(competitions_locations_3132["2"])
						print(competitions_locations_3132["3"])
						print(competitions_locations_3132["4"])
						print(competitions_locations_3132["5"])
						team_info()
					else:
						print("You chose not to look at where the competitions are located")
						team_info()
				else:
					print("You chose not to look at the competitions")
					team_info()
			else:
				print("Didn't compete in 2019")
				team_info()
		elif(info_question_3132 == "awards in 2019"):
			print(awards_3132)
		else:
			print("I'm sorry I don't know what you asked. Your options are: rookie year, location, competed in 2019, competitions in 2019, and awards in 2019. Please copy them exactly")
	


#General Info
team_numbers =[
	1678,
	1682, 
	1690,
	1700,
	2907,
	3132,
]#team numbers
rookie = {
	1678 : 2005,
	1682 : 2005,
	1690 : 2005,
	1700 : 2005,
	2907 : 2009,
	3132 : 2010,
}#teams starting year
location = {
	1678: "Davis, California, USA",
	1682: "Riverside, CA, USA", 
	1690: "Binyamina, HaZafon, Israel",
	1700: "Palo Alto, California, USA",
	2907: "Auburn, Washington, USA",
	3132: "Sydney, New South Wales, Australia",
}#team locations
compete_1678 = True
compete_1682 = False
compete_1690 = True
compete_1700 = True
compete_2907 = True
compete_3132 = True

#1678
competitions_1678 = [
	"Central Valley Regional",
	"Sacramento Reagional",
	"Aerospace Valley Regional",
	"Carver Division",
	"Einstein Field"
] #1678 2019 competitions
competitions_locations_1678 = {
	"1" : "Central Valley Regional: Fresno, Ca, USA", 
	"2": "Sacramento Reagional: Sacramento, CA, USA", 
	"3": "Aerospace Valley Regional: Lancaster, CA, USA", 
	"4": "Carver Division: Houston, TX, USA", 
	"5": "Einstein Field: Houston, TX, USA"
} #1678 2019 competitions and locations
awards_1678 = [
	"CHAIRMAN'S AWARD", 
	"CENTRAL VALLEY REGIONAL WINNER", 
	"SACRAMENTO REGIONAL WINNER", 
	"AEROSPACE VALLEY REGIONAL WINNER"
]#1678 2019 awards

#1682
competitions_1682 = []
competitions_locations_1682 = {}
award_1682 = ["None"]

#1690
competitions_1690 = [
	"ISR District Event #1",
	"ISR District Event #4"
	"FIRST Israel District Championship"
	"Darwin Division"
	"Indiana Robotics Invitational"
] #1690 2019 competitions
competitions_locations_1690 = {
	"1" : "ISR District Event #1: Haifa, HA 00000, Israel",
	"2" : "ISR District Event #4: Tel Aviv-Yafo, TA 00000, Israel",
	"3": "FIRST Israel District Championship: Tel Aviv-Yafo, TA 00000, Israel", 
	"4": "Darwin Division: Detroit, MI, USA", 
	"5": "Indiana Robotics Invitational: Indianapolis, IN, USA"
} #1690 2019 competitions and locations
awards_1690 = ["None"] #1690 awards

#1700
competitions_1700 = [
	"San Francisco Regionals",
	"Utah Regionals",
	"Turing Devision"
]
competitions_locations_1700 = {
	"1" : "San Francisco Regionals: San Francisco, CA, USA",
	"2" : "Utah Regionals: West Valley City, Utah, USA",
	"3" : "Turing Devision: Houston, TX, USA"

}
award_1700 = ["None"]

#2907
competitions_2907 = [
	"PNW District Auburn Mountainview Event",
	"PNW District West Valley Event",
	"PNW District Auburn Event",
	"Pacific Northwest FIRST District Championship",
	"Roebling Division",
	"Einstein Field",
	"Peak Performance",


]
competitions_locations_2907 = {
	"1" : "PNW District Auburn Mountainview Event: Auburn, WA, USA",
	"2" : "NW District West Valley Event: Spokane, WA, USA",
	"3" : "PNW District Auburn Event: Auburn, WA, USA",
	"4" : "Pacific Northwest FIRST District Championship: Tacoma, WA, USA",
	"5" : "Roebling Division: Houston, TX, USA",
	"6" : "Einstein Field: Houston, TX, USA",
	"7" : "Peak Performance: Sea Tac, WA, USA"
}
award_2907 = [
	"2019 PACIFIC NORTHWEST FIRST DISTRICT CHAMPIONSHIP",
	"2019 ROEBLING DIVISION"
]

#3132
competitions_3132 = [
	"Southern Cross Regional",
	"South Pacific Regional",
	"Carver Division",
	"Einstein Field",
	"Duel Down Under",
]
competitions_locations_3132 = {
	"1" : "Southern Cross Regional: Sydney Olympic Park, NSW, Australia",
	"2" : "NSouth Pacific Regional: Sydney Olympic Park, NSW, Australia",
	"3" : "Carver Division: Houston, TX, USA",
	"4" : "Einstein Field: Houston, TX, USA",
	"5" : "Duel Down Under: Sydney, New South Wales, Australia"
}
award_3132 = [
	"2019 SOUTHERN CROSS REGIONAL",
	"2019 CARVER DIVISION"
]

team_info()