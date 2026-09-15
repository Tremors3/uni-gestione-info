def intersect(p1: list[int], p2: list[int]):
    """
    Implementa l'algoritmo di intersezione tra due posting list.
    
    Parameters:
    - p1: Lista di documenti per la parola chiave k1.
    - p2: Lista di documenti per la parola chiave k2.
    
    Returns:
    - answer: Lista dei documenti che contengono sia k1 che k2.
    """
    answer: list = []
    i, j = 0, 0
    
    # Esegui il ciclo finché entrambe le liste hanno elementi
    while i < len(p1) and j < len(p2):
        
        # Se gli ID dei documenti sono uguali, li aggiungiamo al risultato
        if p1[i] == p2[j]:
            answer.append(p1[i])
            i += 1
            j += 1
        
        # Altrimenti avanziamo il puntatore della lista che ha un ID più piccolo
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1
            
    return answer

if __name__ == '__main__':

    # Esempio di utilizzo:
    posting_list_1 = [1, 2, 4, 6, 9]  # Documenti per la keyword k1
    posting_list_2 = [2, 4, 6, 8]     # Documenti per la keyword k2

    result = intersect(posting_list_1, posting_list_2)
    print(f"Documenti che contengono sia k1 che k2: {result}")