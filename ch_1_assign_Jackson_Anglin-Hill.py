teams = {
    1: {
        'location' : 'Flanders, New Jersey, USA', 
        'rookie year' : 1999, 
        'competed in 2019 competitions': 'Yes',
        'names of 2019 competitions': 'FIM District Center Line Event and FIM District Troy Event',
        'location of 2019 competitions': 'Center Line, MI, USA and Troy, MI, USA',
        '2019 season award': 'Imagery Award'
    },

    554: {
        'location' : 'Ft. Thomas, Kentucky, USA', 
        'rookie year' : 2001, 
        'competed in 2019 competitions': 'Yes',
        'names of 2019 competitions': 'Miami Valley Regional',
        'location of 2019 competitions': 'Dayton, OH 45435, USA',
        '2019 season award': 'None'
    },

    253: {
        'location' : 'Millbrae, California, USA', 
        'rookie year': 1999, 
        'competed in 2019 competitions': 'Yes',
        'names of 2019 competitions': 'San Francisco Regional, Monterey Bay Regional and Newton Division',
        'location of 2019 competitions': 'San Francisco, CA, USA, Seaside, CA, USA and Houston, TX, USA',
        '2019 season award': 'Team Spirit Award'
    },

    342: {
        'location' : 'North Charleston, South Carolina, USA', 
        'rookie year' : 2000, 
        'competed in 2019 competitions': 'Yes',
        'names of 2019 competitions': 'Palmetto Regional and Rocket City Regional',
        'location of 2019 competitions': 'Myrtle Beach, SC 29578, USA and Huntsville, AL 35801, USA',
        '2019 season award': 'None'
    },

    16: {
        'location' : 'Mountain Home, Arkansas, USA', 
        'rookie year' : 1996, 
        'competed in 2019 competitions': 'Yes',
        'names of 2019 competitions': 'Midwest Regional, Rocket City Regional and Darwin Division',
        'location of 2019 competitions': 'Detroit, MI, USA and Huntsville, AL 35801, USA',
        '2019 season award': 'Industrial Design Award, Regional Finalists and Excellence in Engineering Award'
    }
}
print("You must enter options exactly as they are displayed. If they are entered incorrectly, you will not receive any information.")
team_number = int(input("Please enter team number. You can enter '1, 554, 253, 342, or 16': "))
team_attribute = input("Please enter team attribute. You can enter 'location, rookie year, competed in 2019 competitions, names of 2019 competitions, location of 2019 competitions, or 2019 season award': ")
print(teams[team_number][team_attribute]) 