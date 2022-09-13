# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
#nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize# Passing the string text into word tokenize for breaking the sentences
import nltk.corpus# sample text for performing tokenization
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from tika import parser 
from os import listdir
from os.path import isfile, join
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PIL import Image



## IMPORT TEXT ##
files = [f for f in listdir('DocumentsSCRM') if isfile(join('DocumentsSCRM', f))]
print(files)
text = ""

for file in files:
    raw = parser.from_file('DocumentsSCRM/Pournader2020.pdf')
    text = text + raw['content']



## STOPWORDS ##
a = set(stopwords.words("english"))
additional_stopwords  = [',','.', '(', ')','&', ':', 'n', '1','2','c','ti','en', '•','et','r','g','er','e','p','l','u']
text1 = word_tokenize(text.lower())
text_noSW = [x for x in text1 if x not in a]
text_noSW = [x for x in text_noSW if x not in additional_stopwords]




## TOKEN ##
#token = word_tokenize(text)


fdist = FreqDist(text_noSW)
fdist1 = fdist.most_common(20)
print(fdist1)



wordcloud = WordCloud(width=1000, 
                      height=1000,
                      prefer_horizontal=0.5,
                      background_color="rgba(255, 255, 255, 0)", 
                      mode="RGBA").generate(text)
# Display the generated image:
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

## STEMMER ##
#pst = PorterStemmer()
#pst.stem("waiting")
#stm = ["waited", "waiting", "waits"]
#for word in stm :
#   print(word+ ":" +pst.stem(word))

#lst = LancasterStemmer()
#stm = ["giving", "given", "given", "gave"]
#for word in stm :
# print(word+ ":" +lst.stem(word))

#from nltk.stem import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer() 
 
#print("rocks :", lemmatizer.lemmatize("rocks")) 
#print("corpora :", lemmatizer.lemmatize("corpora"))


