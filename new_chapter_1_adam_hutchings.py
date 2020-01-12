master_dict = {
'dict_1111':{
	'place':'Edgewater, Maryland',
	'year':2003,
	'active':True,
	'competitions':{'CHS District Bethesda MS Event sponsored by Bechtel',
	'CHS District Owings Mills MD Event sponsored by Leidos','FIRST Chesapeake District Championship'},
	'locations':{'Bethesda, Maryland','Owings Mills, Maryland','Fairfax, Virginia'},
	'awards':{'Autonomous Award sponsored by Ford',"District Chairman's Award",'Team Spirit Award sponsored by FCA Foundation'}
	},
'dict_1678':{
	'place':'Davis, California',
	'year':2005,
	'active':True,
	'competitions':{'Central Valley Regional','Sacramento Regional','Aerospace Valley Regional','Carver Division','Einstein Field',
	'RCC Qianjiang International Robotics Invitational'},
	'locations':{'Fresno, California','Davis, California','Lancaster, California',
	'Houston, Texas','Hangzhou, China'},
	'awards':{"Regional Chairman's Award",'Regional Winners',"FIRST Dean's List Finalist Award",
	'Industrial Design Award sponsored by General Motors','Excellence in Engineering Award sponsored by Delphi',
	'Championship Subdivision Winner','Entrepeneurship Award sponsored by Kleiner Perkins Caufield and Byers'}
},
'dict_2222':{
	'place':'Tacoma, Washington',
	'year':2007,
	'active':False,
	'competitions':"Pacific Northwest Regional",
	'locations':'Portland, Oregon',
	'awards':'No awards. Boo-hoo...'
},
'dict_3333':{
	'place':'Julesburg, Colorado',
	'year':2010,
	'active':False,
	'competitions':"Colorado Regional",
	'locations':'Denver, Colorado',
	'awards':'Judges Award'
},
'dict_5555':{
	'place':'Warren, Michigan',
	'year':2015,
	'active':True,
	'competitions':{'FIM District Center Line Event','FIM District Marysville Event'},
	'locations':{'Center Line, Michigan','Marysville, Michigan'},
	'awards':"District Event Winner"
}
}
team = 'dict_' + input("Which team? ")
statistic = input("Which statistic? ")
print((master_dict[team])[statistic])