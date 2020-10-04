def flu_adult_or_children (age):
	if int(age) >= 18:

		msg1 = "breathing difficulties, pain or pressure in the chest or abdomen ,dizziness, confusion,loss of alertness,seizures,not urinating, which may indicate dehydration,severe pain, weakness, and unsteadiness,a fever or cough that goes away and then comes back,a worsening of other existing health conditions"
		return(msg1)
		#return(msg)
	#if age < 18 and age >10 :
		#msg = "breathing difficulties,rapid breathing,bluish face or lips,chest pain or ribs pulling inward as they breathe,severe aches,dehydration not urinating for 8 hours and crying dry tears,lack of alertness or interaction with others,a fever above 104°Fa fever or cough that goes away but then comes back,"
	

def flu_treatment(age):
	if int(age) >= 18:
		msg2 = "stay at home, avoid contact with other people if possible, keep warm and rest, consume plenty of liquids and healthful foods,avoid alcohol, stop smoking as this raises the risk of complications, chicken broth, herbal teas"
		return(msg2)

def flu_treatment_cost(age):
	if int(age) >= 18:
		msg3 = "Treatment cost will be approximately INR 2000"
		return(msg3)
		#return(msg)
	#if age <18:
		#msg = "Treatment cost will be INR 1000"
	

def health_insurance_plan_flu(location):
	if location == location:
		msg4 = "some best suit insurance plans are: 1.Sefty health plan, 2.Life saving health plan"
		return(msg4)


#age=44
#print(flu_adult_or_children(int(age)))


