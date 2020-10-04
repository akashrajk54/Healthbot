def akash (psymptoms):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    #%matplotlib inline

    import re
    import string
    #import nltk
    #from nltk.corpus import stopwords
    from sklearn.metrics import f1_score
    from sklearn.model_selection import train_test_split
    #from nltk.stem.snowball import SnowballStemmer
    #from nlppreprocess import NLP

    import math
    import string
    punct = string.punctuation
    import spacy
    import en_core_web_sm
    nlp = en_core_web_sm.load()
    #nlp = spacy.load("en_core_web_sm")
    from spacy.lang.en.stop_words import STOP_WORDS

    from sklearn.metrics import confusion_matrix,accuracy_score, classification_report, roc_curve, auc

    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()


    #r"C:\Users\xxxx\Desktop\student-intervention-system\student-data.csv"

    w = pd.read_csv(r"C:\Users\hp\symptom_disease.csv")

    X = w.drop(["Disease"],axis=1)
    m = w["Disease"]
    data = [1,2,3,4,5,6,7,8,9,10]
    y = pd.DataFrame(data,columns=["disease"])

    gnb=gnb.fit(X,np.ravel(y))

    import spacy
    nlp = spacy.load("en_core_web_sm")
    t = ['Passing much less urine','Bleeding from any body part','Feeling extremely lethargic/weak','Excessive sleepiness/restlessness','Altered mental status','Seizure/fits','Breathlessness','Blood in sputum','Chest pain','Sound/noise in breathing','Drooling of saliva','Difficulty in opening mouth','Eye irritation','Runny nose','Stuffy nose','watery eyes','Sneezing','itchy nose','itchy throat','fever','headache','intense pain','fatigue','dry cough','bloody stools','loose stools','nausea','shortness of breath','tight chest','cough','short of breath','muscle pains','diarrhoea','sweats and chills','difficulty breathing','sweating and shivering','rapid heartbeat','sweating','shivering','loss of appetite','coughing up blood','vomiting','Weakness','Stomach pain','constipation','Cough','Chills','Abdominal pain','Yellow skin color','skin color yellow','Dark-colored urine','clay-colored stool','yellow color urine','weight loss','itchy skin']
    #t = ['Passing much less urine', 'Bleeding from any body part', 'Feeling extremely lethargic/weak', 'Excessive sleepiness/restlessness', 'Altered mental status', 'Seizure/fits', 'Breathlessness', 'Blood in sputum', 'Chest pain', 'Sound/noise in breathing', 'Drooling of saliva', 'Difficulty in opening mouth']
    docs = nlp.pipe(t)

    l1= []
    for doc in docs:
        clean_doc = " ".join([tok.lemma_.lower() for tok in doc if not tok.is_stop and not tok.is_punct])
        l1.append(clean_doc)


    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    #print(l2)


    import spacy
    nlp = spacy.load("en_core_web_sm")

    psymptoms = ['Passing much less urine','Bleeding from any body part','Feeling extremely lethargic/weak']

    docs = nlp.pipe(psymptoms)

    sym= []
    for doc in docs:
        clean_doc = " ".join([tok.lemma_.lower() for tok in doc if not tok.is_stop and not tok.is_punct])
        sym.append(clean_doc)

    #psymptoms = ["Feeling extremely lethargic/weak",]
    for k in range(0,len(l1)):
        for z in sym:
            #print(z)
            if(z==l1[k]):
                #print(z)
                l2[k]=1

    inputtest = [l2]


    #print(inputtest)
    predict = gnb.predict(inputtest)

    predicted=predict[0]

    return(m[predicted-1])