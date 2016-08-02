 elif (selected_condition == 'commit suicide') or (selected_condition ==
         'suicidal') or (selected_conditon == 'kill myself') or
 (selected_conditon == 'suicidal thoughts') or (selected_conditon == 'killing
         myself'):
            speech_output = "If you are  " + \
                            (selected_condition if (selected_condition ==
                                'suicidal') else ('contemplating suicide')) + \
                            ", Reach out for help. Call a friend, loved one " \
                            "or the suicide hotline (1-800-273-8255)." \
                            "Remove whatever can harm you at that very moment" \
                            "Divert your mind, do anything to change the
                            subject."
            reprompt_text = "The suicide hotline number is 1-800-273-8255"

