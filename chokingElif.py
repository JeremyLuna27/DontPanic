elif (current_condition == "choking") or (current_condition == "choked") or (current_condition =="choke") or (current_condition == "can't breathe"):
	speech_output = "If someone is choking, stand behind the person. Wrap your arms" \
					"around the waist. Tip the person forward slightly." \
					"Make a fist with one hand. Position it slightly above the person's navel." \
					"Grasp the fist with the other hand. Press hard into the abdomen with a quick, upward thrust — as if trying to lift the person up." \
					"Perform a total of 5 abdominal thrusts, if needed. If the blockage still isn't dislodged, repeat."
	reprompt_text = "If someone is choking, stand behind the person. Wrap your arms" \
					"around the waist. Tip the person forward slightly." \
					"Make a fist with one hand. Position it slightly above the person's navel." \
					"Grasp the fist with the other hand. Press hard into the abdomen with a quick, upward thrust — as if trying to lift the person up." \
					"Perform a total of 5 abdominal thrusts, if needed. If the blockage still isn't dislodged, repeat."
elif (current_condition == "overdosing") or (current_condition == "overdosed") or (current_condition == "OD'd"):
	speech_output = "If someone had a drug overdose, call an ambulance immediately" \
					"Don’t give them anything to eat or drink. Adding another thing to their system could put more stress on their body." \
					"Don’t put them under a shower. Moving someone can be dangerous and the sudden change in temperature could send them into shock." \
					"Don’t allow them to sleep. Try to keep them awake as long as possible." /
					"Don’t encourage them to throw up. There’s a chance they could choke on their vomit." /
					"If the person is conscious, try to find out what they took and how much. This could help staff at the hospital know how to help."
	reprompt_text = "If someone had a drug overdose, call an ambulance immediately" \
					"Don’t give them anything to eat or drink. Adding another thing to their system could put more stress on their body." \
					"Don’t put them under a shower. Moving someone can be dangerous and the sudden change in temperature could send them into shock." \
					"Don’t allow them to sleep. Try to keep them awake as long as possible." /
					"Don’t encourage them to throw up. There’s a chance they could choke on their vomit." /
					"If the person is conscious, try to find out what they took and how much. This could help staff at the hospital know how to help."