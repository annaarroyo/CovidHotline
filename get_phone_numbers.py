# Python program to place according to a single query (name of a vaccine place)
# and details about the place (phone number) gotten through the place_id returned by the query
  
# importing required modules 
import requests, json, os
from dotenv import load_dotenv

def getPhoneNumber(query):  

    #load api key
    load_dotenv()
    token = os.environ.get('API_KEY')

    # enter api key 
    api_key = token
    
    # url variable store url for textsearch request
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    
    # The text string on which to search is passed as a parameter, called query
     # get method of requests module return response object 
    r = requests.get(url + 'query=' + query +
                            '&key=' + api_key) 
    
    # json method of response object convert json format data into python format data 
    x = r.json() 
    
    # now x contains list of nested dictionaries 
    y = x['results'] 


    # use the place_id retreived from the search to search for the phone number of the location


    # url variable store url for details request
    url_for_details = "https://maps.googleapis.com/maps/api/place/details/json?"

    # get method of requests module return response object using the key place_id from the dictionary retrieved above
    r2 = requests.get(url_for_details + 'place_id=' + y[0]['place_id'] 
                            + '&fields=' + 'name,rating,formatted_phone_number'
                            + '&key=' + api_key)

    # json method of response object convert json format data into python format data 
    x2 = r2.json()

    # now x2 contains list of nested dictionaries 
    y2 = x2['result']

    #access the phone number
    raw_num = y2['formatted_phone_number']

    #remove everything but the digits from the phone number and return it
    phone_num = ''.join(c for c in raw_num if c.isdigit())

    return phone_num

def main():
    print(getPhoneNumber('Wellness 360'))

if __name__ == '__main__':
    main()