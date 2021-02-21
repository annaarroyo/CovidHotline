import os, zipcodes, database
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Dial, VoiceResponse, Say
from twilio.rest import Client
app = Flask(__name__)


@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Hi, thank you for calling Ringmune!", voice='alice')

    # Start our <Gather> verb
    gather = Gather(num_digits=5, action='/zip')
    gather.say('Please enter your five digit zip code.')
    resp.append(gather)

    # If the user doesn't select an option, redirect them into a loop
    resp.redirect('/answer')

    return str(resp)

@app.route('/zip', methods=['GET', 'POST'])
def checkZip():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']
        resp.say("Here is the zipcode you entered:", voice='alice')
        resp.say(choice[0])
        resp.say(choice[1])
        resp.say(choice[2])
        resp.say(choice[3])
        resp.say(choice[4])


        # validate zipcode
        if(zipcodes.is_real(choice)):
          resp.redirect('/list_places')
        
        resp.say("Zip code not valid.", voice='alice')
        resp.redirect('/answer')

    return str(resp)


@app.route('/list_places', methods=['GET', 'POST'])
def callPhone():
    """Processes results from the <Gather> prompt in /call"""
    # Start our TwiML response
    resp = VoiceResponse()
 
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    resp.say('There are currently three places with covid nineteen vaccine appointments.')
    resp.say("1 Wellness 360 Adult Located at 7703 Floyd Curl Dr San Antonio has 7,020 appointments this week.")
    #say.break_(strength='x-weak', time='900ms')
    resp.say("2 University Health System Inpatient Located at 4502 Medical Dr San Antonio has 12,870 vaccines this week.")
    #say.break_(strength='x-weak', time='900ms')
    resp.say("3 Samhd Main Immunizations Clinic Located at 210 N Mel Waiters Way San Antonio has 2,340 vaccines this week.")



    gather = Gather(num_digits=1, action='/call_places')
    gather.say('To be forwarded to a phone line, for Wellness 360 Adult, press 1. For University Health System Inpatient, press 2. For Samhd Main Immunizations Clinic, press 3.')
    resp.append(gather)

    #database.db_fun()
    return str(resp)

@app.route('/call_places', methods=['GET', 'POST'])
def call_places():
    """Processes results from the <Gather> prompt in /voice"""
    # Start our TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            resp.say('You selected Wellness 360 Adult. Redirecting your call now...')
            resp.dial('210-567-2788')
            return str(resp)
        elif choice == '2':
            resp.say('You selected University Health System Inpatient. Redirecting your call now...')
            resp.dial('210-358-4000')
            return str(resp)
        elif choice == '3':
            resp.say("You selected Samhd Main Immunizations Clinic. Redirecting your call now...")
            resp.dial('210-207-8894')
        else:
            # If the caller didn't choose 1 or 2, apologize and ask them again
            resp.say("Sorry, I don't understand that choice.")

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/list_places')

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
