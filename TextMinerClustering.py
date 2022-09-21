# Importing necessary library
import pandas as pd
import numpy as np
import nltk
import os
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize# Passing the string text into word tokenize for breaking the sentences
import nltk.corpus# sample text for performing tokenization
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
from tika import parser 
from os import listdir
from os.path import isfile, join
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
words = set(nltk.corpus.words.words())
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
import string
#from pattern.text.en import singularize
from nltk.stem.wordnet import WordNetLemmatizer
import inflect
import matplotlib.pyplot as plt


if __name__ == '__main__':

    ## IMPORT TEXT ##
    files = [f for f in listdir('DocumentsSCRM') if isfile(join('DocumentsSCRM', f))]
    print(files)
    

    

    for file in files:
        if file.endswith('.pdf'):
            raw = parser.from_file("./DocumentsSCRM/"+file)
            text = text + raw['content']



    ## STOPWORDS ##
    a = set(stopwords.words("english"))
    text_lower = word_tokenize(text.lower())
    text_noSW = [str(x) for x in text_lower if str(x) not in a]


    ## PUNCTUATION ##
    words = [word for word in text_noSW if word.isalpha()]


    # LEMMATIZATION ##
    lemmatizer = WordNetLemmatizer() 
    lemmatized = [lemmatizer.lemmatize(word) for word in words]


    ## ADDITIONAL STOPWORDS ##
    engine = inflect.engine()
    stemmed_new = []
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
                            'author','term','http']

    for i in lemmatized:
        if i not in additional_stopwords:
            
            if engine.singular_noun(i) != False:
                #singl = engine.singular_noun(i)
                stemmed_new.append(i)
            else:
                stemmed_new.append(i)




    ## EVALUATION ##
    fdist = FreqDist(stemmed_new)
    print(fdist.most_common(40))
    fdist.plot(50,cumulative=False)
    plt.show()




    ## WORDCLOUD ##
    comment_words = ''
    for words in stemmed_new: 
        comment_words = comment_words + words + ' '

    wordcloud = WordCloud(width=1000, 
                        height=1000,
                        prefer_horizontal=0.5,
                        background_color="rgba(255, 255, 255, 0)", 
                        mode="RGBA").generate(comment_words)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


    ## CLUSTERING ##
    from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
    vec = TfidfVectorizer(max_features=5000, stop_words="english", max_df=0.95, min_df=2)
    features = vec.fit_transform()

    from sklearn.decomposition import NMF
    cls = NMF(n_components=5, random_state=42)
    cls.fit(features)
