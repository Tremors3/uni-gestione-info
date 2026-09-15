from nltk.corpus import wordnet as wn

"""
Script che mostra le funzionalità del Thesaurus WordNet.
"""

if __name__ == '__main__':
    
    ## Ottenere tutti i sinset della parola dog
    ##
    print(wn.synsets('dog'))
    
    ## Specificare il tipo di synset da ritirare
    ## In questo caso un verbo.
    ##
    print(wn.synsets('dog', wn.VERB))
    
    ## Accedere alla definizione di quel significato (synset)
    ##
    dog = wn.synset('dog.n.01')
    print(
        dog.definition(), '\n', 
        dog.examples(), '\n',
        dog.hypernyms()
    )
    
    ## Funzione che permette di recondurre l'espresisone alla sua
    ## parola base che troviamo dentro WordNet (come un Lemmatizer)
    ##
    print(wn.morphy('denied', wn.VERB))
    print(wn.morphy('abaci'))