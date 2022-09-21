# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
#nltk.download('punkt')
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
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
words = set(nltk.corpus.words.words())


## IMPORT TEXT ##
files = [f for f in listdir('DocumentsSCRM') if isfile(join('DocumentsSCRM', f))]
print(files)
text = ""

for file in files:
    if file.endswith('.pdf'):
        raw = parser.from_file("./DocumentsSCRM/"+file)
        text = text + raw['content']



token = word_tokenize(text)
tags = nltk.pos_tag(token)
reg = "NP: {<NN>+}"
a = nltk.RegexpParser(reg)
result = a.parse(tags)
print(result)




## STOPWORDS ##
a = set(stopwords.words("english"))
additional_stopwords  = [',','.', '(', ')','&', ':', 'n', '1','2','c','ti','en', '•','et','r','g','er','e','p','l','u','s','l']
#text_lower = word_tokenize(text.lower())
#text_noSW = [x for x in text if x not in a]
#text_noSW = [x for x in text_noSW if x not in additional_stopwords]

sent = " ".join(w for w in nltk.wordpunct_tokenize(text) if w.lower() in words or not w.isalpha())


## TOKEN ##
#token = word_tokenize(text)


fdist = FreqDist(sent)
fdist1 = fdist.most_common(20)


from nltk.probability import FreqDist
fdist = FreqDist(sent)
print(fdist)




## STEMMER ##


