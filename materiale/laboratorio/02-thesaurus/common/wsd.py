# Importazione di risorse da NLTK
from nltk.corpus import wordnet

# Funzione per disambiguare i termini preprocessati
def disambiguateTerms(tokens: list) -> list[dict]:

    disambiguated_terms = []
    
    for term_i in tokens:
        
        selScore = 0.0
        selSynset = None
        
        for synset_i in wordnet.synsets(term_i, wordnet.NOUN):
            
            score_i = 0.0
            
            for term_j in tokens:                
                if term_j == term_i: continue

                bestScore = 0.0
                
                for synset_j in wordnet.synsets(term_j, wordnet.NOUN):

                    tmpScore = synset_i.wup_similarity(synset_j)
                    
                    if bestScore < tmpScore:    
                        bestScore = tmpScore
        
                score_i = score_i + bestScore
                
            if selScore < score_i:
                selScore = score_i
                selSynset = synset_i

        if term_i is not None:
            disambiguated_terms.append({term_i, selSynset})
    
    return disambiguated_terms