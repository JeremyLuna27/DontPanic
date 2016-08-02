"""
The Don't Panic App by the vzhackthon10 demonstrates a skill 
built with the Amazon Alexa Skills Kit. This skill is designed to
assist users in urgent scenarios and time of need.

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
        if (selected_condition == 'seizure') or (selected_condition == 'seizing'):
            speech_output = "For a seizure " + \
                            "Prevent Choking: Loosen clothing around the person's neck . " \
                            "Roll the person on his or her side to keep the airway open . " \
                            "Don't put anything into the person's mouth . " \
                            "Protect From Injury: Move sharp objects, such as glassware or furniture, " \
                            "away from the person. Ask bystanders to give the person room . " \
                            "Do not restrain or hold down the person . " \
                            "Medications or various blood tests and imaging may be needed . " \
                            "Dial 911 or seek medical attention immediately . " \
                            "Stay with the person until emergency help arrives . "
            reprompt_text = "Prevent Choking: Loosen clothing around the person's neck . " \
                            "Roll the person on his or her side to keep the airway open . " \
                            "Don't put anything into the person's mouth . " \
                            "Protect From Injury: Move sharp objects, such as glassware or furniture, " \
                            "away from the person. Ask bystanders to give the person room . " \
                            "Do not restrain or hold down the person . " \
                            "Medications or various blood tests and imaging may be needed . " \
                            "Dial 911 or seek medical attention immediately . " \
                            "Stay with the person until emergency help arrives . "
        elif (selected_condition == 'panic attack') or (selected_condition == 'panicking') \
                        or (selected_condition == 'panic') or (selected_condition == 'anxiety') \
                        or (selected_condition == 'anxious') or (selected_condition == 'anxiety attack'):
            speech_output = "For " + \
                            (selected_condition if ((selected_condition == 'panicking') or selected_condition == 'anxiety')
                             else ('panics' if (selected_condition == 'panic') else
                            ('anxiousness' if (selected_condition == 'anxious') else
                            ('a panic attack' if (selected_condition == 'panic attack') else
                            ("an anxiety attack"))))) + \
                            ", Begin to slow your breathing down; aim for " \
                            "a maximum of 8 breaths per minute . " \
                            "Inhale 1, and, 2, and, 3, and, 4, and, hold the breath for " \
                            "1, and, 2, and, exhale 1, and, 2, and, 3, and, 4, and, Continue " \
                            "deep breathing this way for several minutes . " \
                            "Distract yourself from catastrophic thoughts. Repeat a positive mantra like: " \
                            "This is uncomfortable but not dangerous . " \
                            "I have been happy before and I will be again . " \
                            "In a few minutes, these feelings will be gone . "
            reprompt_text = "Is there anything else I could help you with? "
            should_end_session = True
        elif selected_condition == 'heart attack':
            speech_output = "Call emergency services immediately or call 9-1-1 . " \
                            "If you can't call 9-1-1 for some reason, ask a bystander to call and " \
                            "give you updates as to the estimated arrival of emergency services . " \
                            "Put the person in a seated position, with knees raised. The person's " \
                            "back should be supported. Loosen any clothing around his neck and " \
                            "chest and try to keep him still, calm, and warm. The person should " \
                            "not be allowed to walk around . "
            reprompt_text = "Call 9-1-1 "
            should_end_session = True
        elif (selected_condition == 'water broke') or (selected_condition == 'baby') or (selected_condition == 'the baby is coming') or (selected_condition == 'birth') or (selected_condition == 'going into labor'):
            speech_output = "Go to the Hospital. If you are not in the hospital " \
                            "in active labor when your water breaks: " \
                            "Make a note of what time your membranes " \
                            "ruptured because your providers will want to " \
                            "know this information . " \
                            "Don't put anything in your vagina to try to check " \
                            "yourself or you could introduce infection . " \
                            "You should consult your doctor or midwife and/or " \
                            "go to the hospital shortly thereafter . " \
                            "Go to the hospital even if you are just leaking " \
                            "fluid and you are not sure if your water broke . " \
                            "Go immediately if you are preterm (less than 37 " \
                            "weeks); especially if you are less than 34 weeks . " \
                            "Look at the color of the amniotic fluid, which " \
                            "should be clear whitish or straw colored. Go " \
                            "immediately to the hospital if the fluid is: " \
                            "Dark or greenish (meconium staining), indicating " \
                            "the baby moved his/her bowel. Bloody throughout, " \
                            "which could indicate risk of placental abruption " \
                            "Foul-smelling, indicating an infection. Take Calm Action "
            reprompt_text = "Go to the doctor. "
            should_end_session = True
        elif (selected_condition == 'commit suicide') or (selected_condition == 'suicidal') \
            or (selected_condition == 'kill myself') or (selected_condition == 'suicidal thoughts') \
            or (selected_condition == 'killing myself'):
            speech_output = "If you are " + \
                            (selected_condition if (selected_condition == 'suicidal') else ('contemplating suicide')) + \
                            ", Reach out for help. Call a friend, loved one " \
                            "or the suicide hotline (1-800-273-8255) . " \
                            "Remove whatever can harm you at that very moment " \
                            "Divert your mind, do anything to change the subject. "
            reprompt_text = "The suicide hotline number is 1-800-273-8255 "
            should_end_session = True
        elif (selected_condition == 'choking') or (selected_condition == 'choked') or (selected_condition =='choke') or (selected_condition == 'can\'t breathe'):
            speech_output = "If someone is choking, stand behind the person. Wrap your arms " \
                            "around the waist. Tip the person forward slightly . " \
                            "Make a fist with one hand. Position it slightly above the person's navel . " \
                            "Grasp the fist with the other hand. Press hard into the abdomen with a quick, upward thrust as if trying to lift the person up . " \
                            "Perform a total of 5 abdominal thrusts, if needed. If the blockage still isn't dislodged, repeat . "
            reprompt_text = ""
            should_end_session = True
        elif (selected_condition == 'overdosing') or (selected_condition == 'overdosed') or (selected_condition == 'O.D.\'d') or (selected_condition == 'overdose'):
            speech_output = "If someone had a drug overdose, call an ambulance immediately " \
                            "Don't give them anything to eat or drink. Adding another thing to their system could put more stress on their body . " \
                            "Don't put them under a shower. Moving someone can be dangerous and the sudden change in temperature could send them into shock . " \
                            "Don't allow them to sleep. Try to keep them awake as long as possible . " \
                            "Don't encourage them to throw up. There's a chance they could choke on their vomit . " \
                            "If the person is conscious, try to find out what they took and how much. This could help staff at the hospital know how to help . "
            reprompt_text = ""
            should_end_session = True
        elif (selected_condition == "having a stroke") or (selected_condition == "stroking") or (selected_condition =="stroke"):
            speech_output = "Call 9-1-1. " \
                            "If the person having a stroke is conscious, lay them down on their side with their head slightly raised and supported .	" \
                            "Do not give them anything to eat or drink. Loosen any restrictive clothing that could cause breathing difficulties . " \
                            "If weakness is obvious in any limb, support it and avoid pulling on it when moving the person . " \
                            "If they are unconscious, check their breathing and pulse and put them on their side. If they do not have a pulse or are not breathing start CPR straight away . "
            reprompt_text = ""
            should_end_session = True
        elif (selected_condition == "fainted") or (selected_condition == "fainting") or (selected_condition == "had a concussion") or (selected_condition == "concussion"):
            speech_output = "If someone fainted, Help them to lie down or sit with their head between their knees . " \
                            "If the person faints and doesn't regain consciousness within one or two minutes, put them into the recovery position . " \
                            "To do this, place them on their side so they're supported by one leg and one arm . " \
                            "open their airway by tilting their head back and lifting their chin . " \
                            "monitor their breathing and pulse continuously . "
            reprompt_text = ""
            should_end_session = True
        elif (selected_condition == 'alcohol poisoning') or (selected_condition == 'very drunk') \
        or (selected_condition == 'drank a lot') or (selected_condition == 'drank too much') \
        or (selected_condition == 'intoxicated') or (selected_condition == 'very intoxicated'):
            speech_output = "For alcohol poisoning" \
                            "If the person is conscious: " \
                            "Make sure they stay awake . " \
                            "Lay them on their side " \
                            "Before you touch them, tell them exactly what " \
                            "you are going to do. Be aware of any signs of " \
                            "aggression. Remain calm and be firm. Avoid " \
                            "communicating feelings of anxiety or anger. " \
                            "Don't give them food, drink, or medication of " \
                            "any kind . " \
                            "If they are unconscious . " \
                            "Call 911 for help, and while waiting for " \
                            "emergency personnel: Gently turn them onto "  \
                            "his or her side and into the Bacchus Maneuver " \
                            "position. Don't leave them alone at any time " \
                            "and be prepared to administer CPR. "

            reprompt_text = ""
            should_end_session = True
    else:
        speech_output = "I'm not sure what your condition or emergency is . " \
                        "Please try again . "
        reprompt_text = "I'm not sure what your condition or emergency is " \
                        "Please try again . "
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def create_selected_condition_attributes(selected_condition):
    return {"currentCondition": selected_condition}


def get_condition_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "currentCondition" in session.get('attributes', {}):
        selected_condition = session['attributes']['currentCondition']
        speech_output = "Your condition is " + selected_condition + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your condition or emergency is. " 
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
