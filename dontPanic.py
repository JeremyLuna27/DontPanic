"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "MyConditionIsIntent":
        return set_condition_in_session(intent, session)
    elif intent_name == "WhatsMyConditionIntent":
        return get_condition_from_session(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Don't Panic. " \
                    "Please tell me your condition or emergency, "
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Welcome to Don't Panic. " \
                    "Please tell me your condition or emergency, "
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for using Don't Panic. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def set_condition_in_session(intent, session):
    """ Sets the condition in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Condition' in intent['slots']:
        selected_condition = intent['slots']['Condition']['value']
        session_attributes = create_selected_condition_attributes(selected_condition)
        if selected_condition == 'seizure':
            speech_output = "For a " + \
                            selected_condition + \
                            ". You can do the following, " \
                            "place a pillow under your head."
            reprompt_text = "For a " + \
                            selected_condition + \
                            ". You can do the following, " \
                            "place a pillow under your head."
        elif (selected_condition == 'panic attack') or (selected_condition == 'panicking'):
<<<<<<< HEAD
            speech_output = "<speak> For " + \
=======
            speech_output = "For " + \
>>>>>>> e65897ba827e9642f6ec35e493c2d0b0f3b12485
                            (selected_condition if (selected_condition == 'panicking') else ('a ' + selected_condition)) + \
                            ", Begin to slow your breathing down; aim for " \
                            "a maximum of 8 breaths per minute. " \
                            "Inhale 1, and, 2, and, 3, and, 4, and, hold the breath for" \
                            "1, and, 2, and, exhale 1, and, 2, and, 3, and, 4, and Continue " \
                            "deep breathing this way for several minutes."
            reprompt_text = "Inhale 1, and, 2, and, 3, and, 4, and hold the breath for " \
                            "1, and, 2 exhale 1, and, 2, and, 3, and, 4, and, Continue " \
                            "deep breathing this way for several minutes."
<<<<<<< HEAD
        elif selected_condition == 'my water broke':
            speech_output = "go to the doctor."
=======
        elif selected_condition == 'water broke':
            speech_output = "Go to the Hospital. If you are not in the hospital " \
                            "in active labor when your water breaks:" \
                            "Make a note of what time your membranes " \
                            "ruptured because your providers will want to " \
                            "know this information." \
                            "Don't put anything in your vagina to try to check " \
                            "yourself or you could introduce infection." \
                            "You should consult your doctor or midwife and/or " \
                            "go to the hospital shortly thereafter." \
                            "Go to the hospital even if you are just leaking " \
                            "fluid and you are not sure if your water broke." \
                            "Go immediately if you are preterm (less than 37 " \
                            "weeks); especially if you are less than 34 weeks." \
                            "Look at the color of the amniotic fluid, which " \
                            "should be clear whitish or straw colored. Go " \
                            "immediately to the hospital if the fluid is:" \
                            "Dark or greenish (meconium staining), indicating " \
                            "the baby moved his/her bowel. Bloody throughout, " \
                            "which could indicate risk of placental abruption " \
                            "Foul-smelling, indicating an infection. Take Calm Action"
>>>>>>> e65897ba827e9642f6ec35e493c2d0b0f3b12485
            reprompt_text = "go to the doctor."
    else:
        speech_output = "I'm not sure what your condition or emergency is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your condition or emergency is " \
                        "Please try again."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def create_selected_condition_attributes(selected_condition):
<<<<<<< HEAD
    return {"favoriteColor": selected_condition}
=======
    return {"currentCondition": selected_condition}
>>>>>>> e65897ba827e9642f6ec35e493c2d0b0f3b12485


def get_condition_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

<<<<<<< HEAD
    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        selected_condition = session['attributes']['favoriteColor']
=======
    if session.get('attributes', {}) and "currentCondition" in session.get('attributes', {}):
        selected_condition = session['attributes']['currentCondition']
>>>>>>> e65897ba827e9642f6ec35e493c2d0b0f3b12485
        speech_output = "Your condition is " + selected_condition + \
                        ". Goodbye."
        should_end_session = True
    else:
<<<<<<< HEAD
        speech_output = "I'm not sure what your condition or emergency is. " \
                        "You can say, my favorite color is red."
=======
        speech_output = "I'm not sure what your condition or emergency is. " 
>>>>>>> e65897ba827e9642f6ec35e493c2d0b0f3b12485
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
