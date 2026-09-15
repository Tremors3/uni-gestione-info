from bisect import bisect_left
from collections.abc import Set

class Document:
    def __init__(self, doc_id, content):
        self.doc_id = doc_id
        self.content = content
        self.word_positions = self.build_word_positions()

    def build_word_positions(self):
        """
        Costruisce un dizionario che mappa ogni parola alle sue posizioni all'interno del documento.
        """
        positions = {}
        words = self.content.split()
        for index, word in enumerate(words):
            if word not in positions:
                positions[word] = []
            positions[word].append(index)
        return positions

def contiguity_check_algorithm(documents: Set[Document], keywords: Set[str]):
    """
    Implementa l'algoritmo di contiguità per verificare se tutte le parole chiave appaiono contigue in ciascun documento.
    
    Parameters:
    - documents: Lista di Documenti.
    - keywords: Lista delle parole chiave (k1, k2, ..., km).
    
    Returns:
    - Set dei documenti che contengono le parole chiave in modo contiguo.
    """
    retrieved_docs = set()

    for doc in documents:
        word_positions = [doc.word_positions.get(k, []) for k in keywords]

        # Trova l'array più corto tra quelli delle posizioni di parole
        shortest_positions = min(word_positions, key=len)
        
        # Per ogni posizione della parola ks nell'array più corto
        for pos_s in shortest_positions:
            
            is_contiguous = True
            
            # Controlla se tutte le altre parole si trovano nelle posizioni contigue
            for i, positions in enumerate(word_positions):
                
                if positions == shortest_positions:
                    continue
                
                target_pos = pos_s + i
                
                # Binary search per trovare la posizione contigua
                idx = bisect_left(positions, target_pos)
                
                if idx == len(positions) or positions[idx] != target_pos:
                    is_contiguous = False
                    break

            if is_contiguous:
                retrieved_docs.add(doc.doc_id)
                break

    return retrieved_docs

if __name__ == '__main__':

    # Esempio di utilizzo:
    documents = [
        Document(1, "the quick brown fox jumps over the lazy dog"),
        Document(2, "the brown fox is quick and the dog is lazy"),
        Document(3, "the quick brown fox jumps quickly"),
    ]

    keywords = ["quick", "brown", "fox"]
    result = contiguity_check_algorithm(documents, keywords)
    print(f"Documenti con parole contigue: {result}")