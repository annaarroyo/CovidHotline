import zipcodes

# Simple zip-code matching.

usr_zip = '80232'

hospital_cities = {"Denver": 7203453668, "somewhere": 123456789}

if(zipcodes.is_real(usr_zip)):
    myzip = zipcodes.matching(usr_zip)
    for dictionary in myzip:
        city = dictionary['city']
        if city in hospital_cities:
            print("calling: " + str(hospital_cities[city]))
        else:
            print("Error: no vaccine information available for zip")

else:
    print("Error: invalid zip code")
