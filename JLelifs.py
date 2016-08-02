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
	speech_output = "If someone had a drug overdose, call an ambulance immediately." \
					"Don’t give them anything to eat or drink. Adding another thing to their system could put more stress on their body." \
					"Don’t put them under a shower. Moving someone can be dangerous and the sudden change in temperature could send them into shock." \
					"Don’t allow them to sleep. Try to keep them awake as long as possible." \
					"Don’t encourage them to throw up. There’s a chance they could choke on their vomit." \
					"If the person is conscious, try to find out what they took and how much. This could help staff at the hospital know how to help."
	reprompt_text = "If someone had a drug overdose, call an ambulance immediately." \
					"Don’t give them anything to eat or drink. Adding another thing to their system could put more stress on their body." \
					"Don’t put them under a shower. Moving someone can be dangerous and the sudden change in temperature could send them into shock." \
					"Don’t allow them to sleep. Try to keep them awake as long as possible." \
					"Don’t encourage them to throw up. There’s a chance they could choke on their vomit." \
					"If the person is conscious, try to find out what they took and how much. This could help staff at the hospital know how to help."

elif (current_condition == "having a stroke") or (current_condition == "stroking") or (current_condition =="stroke"):
	speech_output = "Call 9-1-1." \
					"If the person having a stroke is conscious, lay them down on their side with their head slightly raised and supported.	" \
					"Do not give them anything to eat or drink.  Loosen any restrictive clothing that could cause breathing difficulties. " \ 
					"If weakness is obvious in any limb, support it and avoid pulling on it when moving the person." \
					"If they are unconscious, check their breathing and pulse and put them on their side. If they do not have a pulse or are not breathing start CPR straight away."
	reprompt_text = "Call 9-1-1." \
					"If the person having a stroke is conscious, lay them down on their side with their head slightly raised and supported.	" \
					"Do not give them anything to eat or drink.  Loosen any restrictive clothing that could cause breathing difficulties. " \ 
					"If weakness is obvious in any limb, support it and avoid pulling on it when moving the person." \
					"If they are unconscious, check their breathing and pulse and put them on their side. If they do not have a pulse or are not breathing start CPR straight away."			
					
elif (current_condition == "fainted") or (current_condition == "fainting") or (current_condition == "had a concussion") or (current_condition == "concussion"):
	speech_output = "If someone fainted, Help them to lie down or sit with their head between their knees. " \
					"If the person faints and doesn't regain consciousness within one or two minutes, put them into the recovery position." \
					"To do this, place them on their side so they're supported by one leg and one arm." \
					"open their airway by tilting their head back and lifting their chin." \
					"monitor their breathing and pulse continuously."
	reprompt_text = "If someone fainted, Help them to lie down or sit with their head between their knees. " \
					"If the person faints and doesn't regain consciousness within one or two minutes, put them into the recovery position." \
					"To do this, place them on their side so they're supported by one leg and one arm." \
					"open their airway by tilting their head back and lifting their chin." \
					"monitor their breathing and pulse continuously."