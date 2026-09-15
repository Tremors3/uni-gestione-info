import nltk

# Importazione di risorse da NLTK
from nltk.corpus import stopwords
from nltk.corpus import wordnet

# Stemmers e lemmatizzatori
from nltk.stem.porter import PorterStemmer
from nltk import WordNetLemmatizer

# Other modules
from common.acquire import acquireText, urls
from common.preprocess import preprocessText

"""
WSD : Word Sense Disambiguation
Implementazione di un semplice algoritmo di Word Sense Disambiguation.
"""

# Funzione per disambiguare i termini preprocessati
def disambiguateTerms(tokens: list) -> list[dict]:
    # Si considerano solo i sostantivi, quindi utilizziamo wordnet.NOUN
    
    disambiguated_terms = []
    
    # Itero sui token preprocessati
    for term_i in tokens:
        
        selScore = 0.0  # Similarità massima corrente
        selSynset = None  # Il miglior significato corrente del termine (synset)
        
        # Itero sui synsets (significati) del termine corrente
        for synset_i in wordnet.synsets(term_i, wordnet.NOUN):
            
            score_i = 0.0  # Similarità totale per il synset corrente
            
            # Itero sugli altri termini
            for term_j in tokens:                
                if term_j == term_i: continue  # Salto il confronto del termine con se stesso

                bestScore = 0.0  # Similarità massima tra i synsets di term_i e term_j
                
                # Itero sui synsets del secondo termine
                for synset_j in wordnet.synsets(term_j, wordnet.NOUN):

                    # Calcolo la similarità Wu-Palmer tra i due synsets
                    tmpScore = synset_i.wup_similarity(synset_j)
                    
                    # Se la similarità è maggiore della precedente, aggiorno bestScore
                    if bestScore < tmpScore:    
                        bestScore = tmpScore
        
                score_i = score_i + bestScore  # Aggiungo la miglior similarità al punteggio corrente
                
            # Se il punteggio attuale è maggiore di quello precedente, aggiorno synset e score selezionati
            if selScore < score_i:
                selScore = score_i
                selSynset = synset_i

        # Aggiungo il termine e il synset selezionato alla lista dei termini disambiguati
        if term_i is not None:
            disambiguated_terms.append({term_i, selSynset})
    
    return disambiguated_terms  # Ritorno la lista dei termini disambiguati

# Funzione principale
if __name__ == "__main__":
    
    text = acquireText(urls[1])
    
    # Preprocesso il testo di esempio
    tokens_pre = preprocessText(text)
    
    # Disambiguo i termini preprocessati
    tokens_post = disambiguateTerms(tokens_pre)
    
    # Stampo i risultati
    print("Tokens after preprocessing: ", tokens_pre)
    print("Tokens after disambiguation: ", tokens_post)