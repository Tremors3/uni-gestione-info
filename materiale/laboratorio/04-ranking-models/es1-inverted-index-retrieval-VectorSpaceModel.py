import math
from collections import defaultdict

def inverted_index_retrieval(query_tokens, inverted_index, document_lengths):
    """
    Algoritmo di retrieval basato su Inverted Index.
    
    Parameters:
    - query_tokens: lista dei token della query.
    - inverted_index: dizionario con chiavi come token e valori come liste di (document_id, tf) (inverted index).
    - document_lengths: dizionario che mappa document_id alla lunghezza del documento.
    
    Returns:
    - Lista di tuple (document_id, normalized_score), ordinata per punteggio.
    """
    # Inizializza la hash table R per i documenti recuperati e i loro punteggi
    R = defaultdict(float)
    
    # Calcolo dei pesi della query
    query_weights = {}
    for token in query_tokens:
        if token in inverted_index:
            idf = math.log(1 + len(inverted_index) / len(inverted_index[token]))  # IDF del token
            tf = query_tokens.count(token)  # Conteggio del token nella query
            query_weights[token] = tf * idf  # Peso del token nella query

    # Processa ogni token della query
    for token, weight in query_weights.items():
        if token in inverted_index:
            postings = inverted_index[token]  # Lista delle occorrenze del token (documenti in cui appare)
            for doc_id, tf in postings:
                if doc_id not in R:
                    R[doc_id] = 0.0  # Inizializza il punteggio del documento
                R[doc_id] += weight * tf  # Incrementa il punteggio del documento

    # Calcola la lunghezza del vettore della query
    query_length = math.sqrt(sum(w ** 2 for w in query_weights.values()))

    # Normalizza i punteggi dei documenti
    normalized_scores = []
    for doc_id, score in R.items():
        doc_length = document_lengths.get(doc_id, 1.0)  # Lunghezza del documento (default: 1.0)
        normalized_score = score / (query_length * doc_length)
        normalized_scores.append((doc_id, normalized_score))

    # Ordina i documenti in base al punteggio normalizzato (in ordine decrescente)
    normalized_scores.sort(key=lambda x: x[1], reverse=True)

    return normalized_scores

if __name__ == '__main__':
    
    # Esempio di utilizzo
    query_tokens = ["information", "retrieval", "model"]
    inverted_index = {
        "information": [("doc1", 3), ("doc2", 5)],
        "retrieval": [("doc2", 2), ("doc3", 4)],
        "model": [("doc1", 1), ("doc3", 3)],
    }
    document_lengths = {
        "doc1": 2.0,
        "doc2": 3.0,
        "doc3": 4.0,
    }

    results = inverted_index_retrieval(query_tokens, inverted_index, document_lengths)
    print("Risultati:", results)