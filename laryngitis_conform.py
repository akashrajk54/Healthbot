def laryngitis_adult_or_children (age):
	if int(age) >= 18:

		msg1 ='''
		1. hoarseness
		2. difficulty with speech
		3. throat pain
		4. low fever
		5. persistent cough
		6. frequent throat clearing
		7. headache
		8. swelling in the glands
		9. runny nose
		10. pain while swallowing
		11. fatigue and malaise
		'''
		return(msg1)
	if int(age) >=10 and int(age) <=18:

		msg1 = '''
		1. difficulty with breathing or swallowing
        2. a fever of over 103° Fahrenheit or 39.4° Celsius
        3. drooling
        4. loud, high-pitched breathing sounds when inhaling
		       '''
		return(msg1)
	#if age < 18 and age >10 :
		#msg = "breathing difficulties,rapid breathing,bluish face or lips,chest pain or ribs pulling inward as they breathe,severe aches,dehydration not urinating for 8 hours and crying dry tears,lack of alertness or interaction with others,a fever above 104°Fa fever or cough that goes away but then comes back,"
	

def laryngitis_treatment(age):
	if int(age) >= 18:

		msg22 = '''For laryngitis, rest means limiting the use of the larynx. Avoid talking, singing, or using the voice box.
		Although whispering may seem like a gentler alternative to speaking at normal volume, this requires that the vocal cords are tightly stretched, hampering their recovery. Whispering should also be avoided.'''

		msg2 = '''
		home remedies include:

		1. avoiding decongestants, as these dry out the throat
		2. breathing moist air
		3. using acetaminophens, such as paracetamol, or ibuprofen to control the pain
		4. avoiding inhalation of irritants, such as smoking or second-hand smoke
		5. drinking plenty of fluids'''
		return(msg2)

def laryngitis_treatment_cost(age):
	if int(age) >= 18:
		msg3 = "Treatment cost will be approximately INR 3000"
		return(msg3)
		#return(msg)
	#if age <18:
		#msg = "Treatment cost will be INR 1000"
	

def health_insurance_plan_laryngitis(location):
	if location == location:
		msg4 = '''
		some best suit insurance plans are:
		1.Sefty health plan,
		2.Life saving health plan'''
		return(msg4)


#age=44
#print(laryngitis_treatment(int(age)))


