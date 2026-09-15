import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic

"""
Script per testing della Similarità.
Utilizzando il thesaurus di WordNet
"""

if __name__ == '__main__':
    
    # Istanziamo cane e gatto selezionando come synset il concetto di animale
    cat = wn.synset('cat.n.01')
    dog = wn.synset('dog.n.01')
    computer = wn.synset('computer.n.01') # Andiamo a pescare il primo synset di computer
    
    ## Calcoliamo la similarità tra Dog (animale) e Cat (animale)
    ## Utilizzando la similarità di Path Distance Similarity
    print("Path Distance (Dog-Cat): ", dog.path_similarity(cat))
    
    ## Calcoliamo la similarità tra Dog (animale) e Cat (animale)
    ## Utilizzando la similarità di Path Distance Similarity
    print("Path Distance (Dog-Computer): ", dog.path_similarity(computer))

    print() #####################################################
    
    ## Calcoliamo la similarità tra Dog (animale) e Cat (animale)
    ## Utilizzando la similarità di Wu-Palmer (WUP)
    print("Wu-Palmer (Dog-Cat): ", dog.wup_similarity(cat))
    
    ## Calcoliamo la similarità tra Dog (animale) e Cat (animale)
    ## Utilizzando la similarità di Wu-Palmer (WUP)
    print("Wu-Palmer (Dog-Computer): ", dog.wup_similarity(computer))
    
    print() #####################################################
    
    ## Scegliamo e Istanziamo un corpus da nltk
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    
    ## Calcoliamo la similarità tra Dog (animale) e Cat (animale)
    ## Utilizzando la similarità di Resnik
    print("Resnik (Dog-Cat): ", dog.res_similarity(cat, brown_ic))
    
    ## Calcoliamo la similarità tra Dog (animale) e Computer (dispositivo)
    ## Utilizzando la similarità di Resnik
    print("Resnik (Dog-Computer): ", dog.res_similarity(computer, brown_ic))