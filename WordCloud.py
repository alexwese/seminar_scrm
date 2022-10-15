# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
from nltk.tokenize import word_tokenize
import nltk.corpus
from nltk import word_tokenize
from nltk.corpus import stopwords
from tika import parser 
from os import listdir
from os.path import isfile, join
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.stem.wordnet import WordNetLemmatizer
import inflect
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
words = set(nltk.corpus.words.words())


    
def createWordcloud(dir:str):

    ## IMPORT TEXT ##
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    print(files)
    text = ""

    for file in files:
        if file.endswith('.pdf'):
            raw = parser.from_file("./"+dir+"/"+file)
            text = text + raw['content']


    ## STOPWORDS ##
    a = set(stopwords.words("english"))
    additional_stopwords  = [',','.', '(', ')','&', ':', 'n', '1','2','c','ti','en', '•','et',
                            'r','g','er','e','b','p','l','u','s','l','e','i','r','t','a','s','h',
                            'o','s','_','.','https','al','fig','','also','x','may','used','one','two',
                            'might','research','article','according','within','among','literature','thu',
                            'number','sc','need','part','table','many','another','study','three','see', 
                            'journal','focu','example','datum','time','show','following','several','source',
                            'lo','specific','focus','first','paper','based','though','dates','become','using',
                            'often','set','refer','able','must','needs','need','shown','thus','possible','make',
                            'even','various','tion','consider','related','certain','figure','figures',
                            'use','including','identified','way','required','ing','due','defined','chapter',
                            'theory', 'int ', 'int', 'int j', 'int i', 'show', 'shows', 'ment','j','given',
                            'author','term','http', 'eg','pp', 'ie', 'kleindorfer','saad','vol' ,'f f', 'f', 'fi',
                            'rm','mentzer','manuj','well','zsidisin','said','ic','el','te','review','st','sy',
                            'em','finding','k','le', 'st','since','de','initial','wang','k','em','finding',
                            'k','le','annals','important','increase','provide','considered']

    text_lower = word_tokenize(text.lower())
    text_noSW = [str(x) for x in text_lower if str(x) not in a]


    ## PUNCTUATION ##
    words = [word for word in text_noSW if word.isalpha()]



    ## LEMMATIZER ##
    lemmatizer = WordNetLemmatizer() 
    lemmatized = [lemmatizer.lemmatize(word) for word in words]


    ## ADDITIONAL STOPWORDS ##
    engine = inflect.engine()
    stemmed_new = []

    for i in lemmatized:
        if i not in additional_stopwords:
                stemmed_new.append(i)


    comment_words = ''
    for words in stemmed_new: 
        comment_words = comment_words + words + ' '


    ## WORDCLOUD ##
    wordcloud = WordCloud(width=2000, 
                        height=2000,
                        prefer_horizontal=0.5,
                        max_words= 100,
                        background_color="rgba(255, 255, 255, 0)", 
                        mode="RGBA").generate(comment_words)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()




# main Function
if __name__ == "__main__":  

    createWordcloud("2012")
    createWordcloud("2022")
    createWordcloud("Literature")





