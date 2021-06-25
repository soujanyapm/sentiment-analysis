import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

from wordcloud import (WordCloud, get_single_color_func)
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt
import random
nltk.download('stopwords') 

india_mask = np.array(Image.open('./assets/india.png'))

df = pd.read_csv('./assets/scrapped_reviews_final.csv')
corpus = []


for i in range(0,df.shape[0]):
    #------STEP 1 : Remove all that which are not between A-Z and a-z like, special symbols, extra spaces, exclamatory marks, # tags---------------#
    
    review = re.sub('[^a-zA-Z]', ' ' , df.iloc[i,0]) # i th row and 1st column
    # replace all that is not between a-z and A-Z with space.
    # [^a-zA-Z] = select everything which is not in between a-z A-Z
    
    #-------STEP 2 : Convert everything to lower case---------------------#
    
    review = review.lower()
    
    #--------STEP 3 : Handle the extra spaces ---------------------------#
    
    # Split the review on space, after split the review will be converted into list of words.
    review = review.split()
    
    #---------STEP 4 : Remove the stopwords----------------------------#
    
    # run a loop, compare each word in a list called review with set of downloaded stopwords, if the word is in the list of stopwords, then don't select that word
    
    review = [eachword for eachword in review if not eachword in stopwords.words('english')]
    # for eachword in review list , if eachword is not in set of english stopwords, then return that eachword
    
    
    
    #-----Convert the list back to string------------#
    
    review = " ".join(review)
    # join each word in the list called review with space to convert it back to str
    
    # append each converted review to corpus list
    corpus.append(review)
    
    
vect = CountVectorizer(min_df=25).fit(corpus)

len(vect.get_feature_names())

print(vect.get_feature_names())   

vect_txt = " ".join(vect.get_feature_names()[0:50]) 

txt_file = open('./assets/frequent_words.txt','a')

txt_file.write(vect_txt)

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(100, 100%%, %d%%)" % random.randint(60, 100)

class GroupedColorFunc(object):
    """
    Uses different colors for different groups of words. 
    """
    
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]
        
        self.default_color_func = get_single_color_func(default_color)
    
    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func
        
        return color_func
    
    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)
        return self.get_color_func(word)(word, **kwargs)

color_to_words = {
        # words below will be colored with a green single color function
        '#00b7e3': vect.get_feature_names()[0:25],
        # will be colored with a red single color function
        '#ff7a59': vect.get_feature_names()[26:50]
    }

wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="#1b2a47", width=480, height=360).generate(vect_txt)


grouped_color_func = GroupedColorFunc(color_to_words, 'grey')
plt.figure()
plt.imshow(wordcloud.recolor(color_func=grouped_color_func, random_state=3), interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("./assets/wordscloud.png")

