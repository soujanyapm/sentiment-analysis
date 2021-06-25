import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv('./assets/scrapped_reviews_final.csv')

df.shape

df.head()
reviewslist = df.iloc[:,0].values


global pickle_model
file = open("./assets/pickle_model.pkl",'rb')
pickle_model = pickle.load(file)
    
global vocab
file = open("./assets/features.pkl",'rb')
vocab = pickle.load(file)

def check_review(reviewText):

    #reviewText has to be vectorised, that vectorizer is not saved yet
    #load the vectorize and call transform and then pass that to model preidctor
    #load it later

    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace",vocabulary=vocab)
    vectorised_review = transformer.fit_transform(loaded_vec.fit_transform([reviewText]))


    # Add code to test the sentiment of using both the model
    # 0 == negative   1 == positive
    
    return pickle_model.predict(vectorised_review)    

posneg=[]

for review in reviewslist:
    response = check_review(review)
    if(response[0]==0):
            result ='Negative'
    else:
            result = 'Positive'
       
    posneg.append(result)
    
reviewDf = pd.DataFrame()
reviewDf['predictions']   =  posneg 
   
reviewDf.to_csv('./assets/predictions.csv',index=False)
