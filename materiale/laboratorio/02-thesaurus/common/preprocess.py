import nltk

# Importazione di risorse da NLTK
from nltk.corpus import stopwords

# Stemmers e lemmatizzatori
from nltk.stem.porter import PorterStemmer
from nltk import WordNetLemmatizer

# Funzione per preprocessare il testo
def preprocessText(text: str, remove_stopwords: bool = True, use_lemmatizer: bool = False, use_stemmer: bool = False) -> list:
    
    if use_lemmatizer:
        wnl = WordNetLemmatizer()
    
    if use_stemmer:
        porter_stemmer = PorterStemmer()

    if remove_stopwords:
        stop_words = set(stopwords.words('english'))

    index_tokens = []
    
    for token, tag in nltk.pos_tag(nltk.word_tokenize(text)):
        
        token = token.lower()
        
        if not remove_stopwords or token not in stop_words:
            
            if tag.startswith('NN'):
                
                if use_lemmatizer:
                    token = wnl.lemmatize(token)
                
                if use_stemmer:
                    token = porter_stemmer.stem(token)
                
                index_tokens.append(token)

    return index_tokens