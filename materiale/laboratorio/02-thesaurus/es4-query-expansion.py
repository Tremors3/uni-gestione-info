import nltk

import yake # pip install yake
from rake_nltk import Rake # pip install rake-nltk

# Importazione di risorse da NLTK
from nltk.corpus import stopwords
from nltk.corpus import wordnet

# Stemmers e lemmatizzatori
from nltk.stem.porter import PorterStemmer
from nltk import WordNetLemmatizer

# Other Imports
from common.acquire import acquireText, urls
from common.preprocess import preprocessText
from common.wsd import disambiguateTerms

"""
WSD : Word Sense Disambiguation
Implementazione di un semplice algoritmo di Word Sense Disambiguation.
"""

def withYake(text:str):
    
    language = "en"
    max_ngram_size = 1
    deduplication_thresold = 0.9 # Frequenza: quanti documenti contengono quella parola
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    kw_extractor = yake.KeywordExtractor(
        lan=language, 
        n=max_ngram_size, 
        dedupLim=deduplication_thresold, 
        dedupFunc=deduplication_algo, 
        windowsSize=windowSize, 
        top=numOfKeywords
    )
    
    keywords = kw_extractor.extract_keywords(str(text))

    return keywords

def withRake(text: str):
    
    r = Rake(
        min_length=1, 
        max_length=1, 
        include_repeated_phrases=False
    )

    r.extract_keywords_from_text("Feature extraction is not that complex. There are many algorithms available that can help you with feature extraction. Rapid Automatic Key Word Extraction is one of those")

    return r.get_ranked_phrases()

if __name__ == "__main__":
    
    ## Ottengo il testo
    text = acquireText(urls[1])
    #text = "The cat is on the table, inside the house by the fire."

    ## Preprocesso il testo di esempio
    text = preprocessText(text)
    
    ## Disambiguo i termini preprocessati
    #text = disambiguateTerms(text)
    
    ## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ##
    ## Keyword Extraction with Yake
    ## https://liaad.github.io/yake/docs/getting_started.html
    
    print("\n%%%%%% YAKE KEYWORDS %%%%%%")
    for keyword, val in withYake(text): print(keyword)
    
    ## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ##
    ## Keyword Extraction with Rake
    
    print("\n%%%%%% RAKE KEYWORDS %%%%%%")
    for keyword in withRake(text): print(keyword)
    
    ## %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% ##
    ## Keyword Extraction with Spacy
    ## https://spacy.io/