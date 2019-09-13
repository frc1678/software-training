robot_information = {'team_one' : {'location': 'Pontiac, Michigan',
                                         'rookie_year': '1997',
                                         'competed_in_2019': 'True',
                                         'competition_names' : 'FIM District Center Line Event, FIM District Troy Event',
                                         'competition_locations' : 'Center Line MI, USA and  Troy MI, USA',
                                         'competition_awards' : 'none',
                                   },

                     'team_four' : {
                         'location' : 'Van Nuys California, USA',
                         'rookie_year' : '1997',
                         'competed_in_2019' : 'True',
                         'competition_names' : 'Los Angeles North Regional, Los Angeles Regional, Wings Over Camarillo, Battleship Blast (Saturday), Beach Blitz',
                         'competition_locations' : 'Valencia, CA, USA, Valencia, CA, USA, Camarillo, CA, USA, San Pedro, CA, United States',
                         'awards' : 'Quality Award sponsored by Motorola Solutions Foundation',
                      },

                     'team_five' : {
                         'location' : 'Melvindale, MI, USA',
                         'rookie_year' : '1998',
                         'competed_in_2019' : 'True',
                         'competition_names' : 'Big Bang!',
                         'competition_locations' : 'Taylor, MI, USA',
                         'awards' : 'none',
                      },

                     'team_six' : {
                         'location' :  'Plymouth, MN, USA',
                         'rookie_year' : '1994',
                         'competed_in_2019' : 'false',
                         'competition_names' : 'none',
                         'competition_locations' : 'none',
                         'awards' : 'none',
                     },

                     'team_seven' : {
                         'location' : 'Baltimore, MD, USA',
                         'rookie_year' : 'not stated, last competed in 2012',
                         'competed_in_2019' : 'False',
                         'competition_locations' : 'none',
                         'competition_names' : 'none',
                         'awards' : 'none',

                      }
                     }


                                   
team_number = input("What is the team number? ")
team_attribute = input("What is the team attribute? ")
print(robot_information[team_number] [team_attribute])
