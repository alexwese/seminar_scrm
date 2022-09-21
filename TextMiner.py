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
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
import string
#from pattern.text.en import singularize
from nltk.stem.wordnet import WordNetLemmatizer
import inflect


if __name__ == '__main__':

    ## IMPORT TEXT ##
    files = [f for f in listdir('DocumentsSCRM') if isfile(join('DocumentsSCRM', f))]
    print(files)
    text = ""

    for file in files:
        if file.endswith('.pdf'):
            raw = parser.from_file("./DocumentsSCRM/"+file)
            text = text + raw['content']


    token = word_tokenize(text.lower())
    stemmer = SnowballStemmer(language="english")
    #stems = [stemmer.stem(t) for t in token]  
    stems = " ".join(w for w in token)
    #print(stems)



    ## STOPWORDS ##
    a = set(stopwords.words("english"))
    additional_stopwords  = [',','.', '(', ')','&', ':', 'n', '1','2','c','ti','en', '•','et',
                            'r','g','er','e','p','l','u','s','l','e','i','r','t','a','s','h',
                            'o','s','_','.','https','al','fig','']
    text_lower = word_tokenize(text.lower())
    text_noSW = [str(x) for x in text_lower if str(x) not in a]
    #text_noSW = [x for x in text_noSW if x not in additional_stopwords]
    text_noSW_str = ' '.join(str(x) for x in text_noSW)
    #text_noSW = " ".join(x for x in text_noSW if x not in additional_stopwords)
    #text_noSW_eng = " ".join(w for w in nltk.wordpunct_tokenize(text_noSW) if w.lower() in words or not w.isalpha())


    ## REMOVE PUNCTUATION ##
    punctuations=list(string.punctuation)
    text_noSW_eng_noPunc=[]

    for i in text_noSW:
        if i not in punctuations:
            text_noSW_eng_noPunc.append(i)




    #
    #print(text_noSW_str)


    ## TOKEN ##
    #token = word_tokenize(text)



    ## PUNCTUATION ##
    words = [word for word in text_noSW if word.isalpha()]


    ## STEMMER ##
    porter = PorterStemmer()
    lancaster = SnowballStemmer(language="english")
    #stemmed = [lancaster.stem(word) for word in words]

    
    
    engine = inflect.engine()

    ## ADDITIONAL STOPWORDS ##
    stemmed_new = []
    for i in words:
        if i not in additional_stopwords:
            
            if engine.singular_noun(i) != False:
                singl = engine.singular_noun(i)
                stemmed_new.append(singl)
            else:
                stemmed_new.append(i)

    print(stemmed_new)




    ## EVALUATION ##
    fdist = FreqDist(stemmed_new)
    print(fdist.most_common(30))

    import matplotlib.pyplot as plt

    fdist.plot(50,cumulative=False)
    plt.show()



    ## WORDCLOUD ##
    wordcloud = WordCloud(width=1000, 
                        height=1000,
                        prefer_horizontal=0.5,
                        background_color="rgba(255, 255, 255, 0)", 
                        mode="RGBA").generate(words)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()




    ## STEMMER ##
    #pst = PorterStemmer()
    #pst.stem("waiting")
    #stm = ["waited", "waiting", "waits"]
    #for word in stm :
    #   print(word+ ":" +pst.stem(word))

    lst = LancasterStemmer()
    stm = ["firm", "scrm", "supply chain", "impact", "management"]
    for word in stm :
        print(word+ ":" +lst.stem(word))


    #from nltk.stem import WordNetLemmatizer
    #lemmatizer = WordNetLemmatizer() 
    
    #print("rocks :", lemmatizer.lemmatize("rocks")) 
    #print("corpora :", lemmatizer.lemmatize("corpora"))


