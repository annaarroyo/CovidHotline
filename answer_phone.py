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
        resp.say(choice)

        # validate zipcode
        if(zipcodes.is_real(choice)):
          resp.redirect('/call_number')
        
        resp.say("Zip code not valid.", voice='alice')
        resp.redirect('/answer')

    return str(resp)


@app.route('/call_number', methods=['GET', 'POST'])
def callPhone():
    """Processes results from the <Gather> prompt in /call"""
    # Start our TwiML response
    resp = VoiceResponse()
 
    # Your Account Sid and Auth Token from twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    database.db_fun()
    resp.dial('512-820-2641')
    print(resp)

    return str(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
