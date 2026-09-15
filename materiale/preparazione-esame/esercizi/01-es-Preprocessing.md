
<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 1) Disegna la struttura Trie Corrispondente

#### QUESITO

Dato il seguente insieme di parole *{"car, cart, cat, dog, door"}* crea una struttura dati Trie appropriata. Mostra cosa comporta la presenza di parole prefisso di altre parole ed eventuali biforcazioni.

#### RISPOSTA

Disegno del Trie:

```                      
                           t* (fine parola "cart")
                          /
(root) + --- c --- a --- r* (fine parola "car")
       |            \
       |             t* (fine parola "cat")
       |
       d --- o --- g* (fine parola "dog")
              \
               o --- r* (fine parola "door")
```

#### SUGGERIMENTI

1. La prof potrebbe dirci di disegnare il relativo indverted index. In quel caso disegnamo il dizionario a fianco della trie con i termini ordinati in ordine alfabetico. Successivamente colleghiamo a matita i nodi foglia dell'albero al relativo termine. A destra del dizionario metteremo le posting lists. **Trie --> Dizionario --> PL.**
2. Ricordiamoci di inserire i caratteri speciali ($ o *) sui nodi foglia di ciascuna parola.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 2) Esegui la fase di Preprocessing e Costruisci un Inverted Index

#### SUGGERIMENTI

1. Solitamente i documenti sono 3 e composti da circa 4 parole ognuno.
2. In questo caso sono richiesti solamente il vettore dei termini e le Posting List, non il Trie.
3. A seconda delle fasi di preprocessing possiamo decidere di rimuovere anche i verbi. A volte lo stemming o la lemmatizzazione aiutano a ridurre il numero di parole da indicizzare.

#### QUESITO

1) **Dati i seguenti tre documenti, mostrami un possibile risultato della fase di pre-processing.**
2) **Successivamente mostra il relativo Inverted Index.**
    - **Mostra un esempio di Inverted Index di tipo:   *Document Based***
    - **Mostra un esempio di Inverted Index di tipo:  *Word Based***

- doc_1= *"che bello andare a scuola in bicicletta"*
- doc_2= *"la bicicletta è parcheggiata più avanti"*
- doc_3= *"è vietato parcheggiare vicino a scuola"*

#### RISPOSTA

FASE1: PREPROCESSING DEI DOCUMENTI

- Ho deciso di applicare le seguenti fasi della pipeline:

    1) Tokenizzazione
    2) Rimozione delle Stop Words
    3) Riduzione delle parole allo stesso lemma (Lemmatizer)
    4) Selezione dei termini di Indice (Tagger)

    Risultato:

    - doc_1= *"andare scuola bicicletta"*
    - doc_2= *"bicicletta parcheggiare"*
    - doc_3= *"parcheggiare scuola"*

FASE2: COSTRUZIONE DELL'INVERTED INDEX

- Le fasi per la costruzione dell'inverted index sono:

    1. Disegno del vettore dei termini:

    - andare
    - bicicletta
    - parcheggiare
    - scuola

    2.a Costruzione della Posting List (Document Based)

    ```
    TERM         Df  PL  Dc   Tf | Dc   Tf
    andare       1   --> doc1,f1 |
    bicicletta   2   --> doc1,f1 | doc2,f1
    parcheggiare 2   --> doc2,f1 | doc3,f1
    scuola       2   --> doc1,f1 | doc3,f1
    ```

    2.b Costruzione della Posting List (Word Based)

    ```
    TERM         Df  PL  Dc   Tp  | Dc   Tp
    andare       1   --> doc1,p1, |
    bicicletta   2   --> doc1,p3, | doc2,p1,
    parcheggiare 2   --> doc2,p2, | doc3,p1,
    scuola       2   --> doc1,p2, | doc3,p2,
    ```

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 3) DATA UNA TASSONOMIA CALCOLARE LA SIMILARITA' TRA DUE TERMINI

#### QUESITO

Data la seguente tassonomia di termini calcola la similarità tra i termini **"hill"** e **"coast"** utilizzando le formule:
- sim-path-distance
- sim-Wu-Palmer
- sim-Resnik

Inserendo valori a piacere dove mancano. La tassonomia è la seguente:

```
LIVELLO       TERMINI
1               ...
                 |
2               ...
                 |
3       geological-formation
            /             \
4   natural-elevation    shore
           |               |
5        hill            coast
```

#### RISPOSTA

FORMULE:

$$ \text{sim-path-distance(c1, c2)} = \frac{1}{dist(c1, c2) + 1} $$
$$ \text{sim-Wu-Palmer(c1, c2)} = \frac{2 \cdot depth(LCS(c1, c2))}{depth(c1) + depth(c2)} $$
$$ \text{sim-Resnik(c1, c2)} = - \hspace{3pt} log \hspace{3pt} P(LCS(c1, c2)) $$

1. **Calcolo della similarità sim-path-distance**:

    Utilizziamo la formula:
    
    $$ \text{sim-path-distance(c1, c2)} = \frac{1}{5 + 1} = \frac{1}{6} $$

2. **Calcolo della similarità sim-Wu-Palmer**:

    Utilizziamo la formula:
    
    $$ \text{sim-Wu-Palmer(c1, c2)} = \frac{2 \cdot depth(\text{geological-formation})}{depth(c1) + depth(c2)} = \frac{2 * 3}{5 + 5} = \frac{3}{5}$$

3. **Calcolo della similarità sim-Resnik**:

    Ipotizziamo: ***P(geological-formation) = 1.5***

    Utilizziamo la formula:

    $$ \text{sim-Resnik(c1, c2)} = -\log{P(\text{geological-formation})} = - \log{1.5} = -0.17 $$

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 4) BOOLEAN RETRIEVAL

#### QUESITO

Esegui la seguente Query Booleana basandoti sulla rappresentazione serializzata di un Indice Inverso.

```
QUERY: "database OR science AND case"

INVERTED INDEX

TERM      START n             | 002 001 004 001 003
boundary     0  1           0 +  3   2   1   1   2
case         1  2             | 002 003 001 002 003
computer     3  2           5 +  1   1   1   1   1
database     5  1             | 001 002 004 002 001
deliver      6  1          10 +  1   1   2   2   1
document     7  3             | 003 004 003
fan         10  3          15 +  2   1   1
play        13  1
position    14  1
science     15  2
System      17  1
```

#### RISPOSTA

PROCEDURA RISOLUTIVA:

1. L'ordine di esecuzione degli operatori prevede che l'operatore AND sia eseguito prima dell'operatore OR.
    
    La query Diventa: *"database OR (science AND case)"*

2. Disegno dell'albero di sintassi:

    ```
           OR
         /    \
        /      \
    database   AND
             /     \
            /       \
        science    case
    ```

3. Risoluzione della query:

    ```
    database OR (science AND case)

    database OR ( {003,004} intersect {001,004} )

    database OR {004}

    {002} union {004}

    Risultato: {002, 004}
    ```

#### PSEUDOCODICE ALGORITMO AND

```
INTERSECT(p1, p2)
answer <-- ()
while p1 != NIL AND p2 != NIL
do if docID(p1) = docID(p2)
    then ADD(answer, docID(p1))
        p1 <-- next(p1)
        p2 <-- next(p2)
    else if docID(p1) < docID(p2)
        then p1 <-- next(p1)
        else p2 <-- next(p2)
return answer
```
- La **INTERSEZIONE** (AND) usufruisce del fatto che le due posting lists sono ordinate.
- Il costo dell'intersezione è quindi $O(n)$.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 5.1) PHRASAL RETRIEVAL (CONTIGUITY CHECK ALGORITHM)

#### QUESITO

Esegui la Phrasal Retrieval Query specificata in seguito sulla seguente Posting List considerata.

```
QUERY: "information retrieval system"

POSTING LIST
information  --> ... DOC7: 1 10 27 338   ...
retrieval    --> ... DOC7: 2 28 939 3127 ...
system       --> ... DOC7: 4 29
```

#### RISPOSTA

PROCEDIMENTO DEL PHRASAL RETRIEVAL:

1. **CHECK TERM PRESENCE IN DOCUMENTS**: Troviamo tutti i documenti che contengono tutte e tre le parole "information", "retrieval" e "system". Ridurre il document set su cui vado a lavorare facendo un'intersezione.

    In questo caso solamente il doucmento 7 (DOC7) contiene tutte e tre le parole.

2. **SELECTING THE MAIN POSITION LIST**: Per ciascun documento che contiene tutte le parole della query (Doc7) selezioniamo la lista delle occorrenze più corta (con meno posizioni). Questa sarà la lista delle occorrenze che verrà iterata per prima e a cui faranno riferimento i parametri $p, i, s$.

    In questo caso la lista della parola "SYSTEM", che ha solamente due posizioni.

3. **CHECK ORDER CONTIGUITY**: Sono certo che queste tre parole ci siano nel documento ma devo controllare che esse siano contigue. In questo caso ci aiuta molto l'Il "Position Based Inverted Index".

    Formula: (p + i - s)

    - p = posizione della prima parola nel del documento D.
    - i = posizione della seconda parola nella query Q.
    - s = offset tra prima parola e seconda parola nella query Q.

    1. **Situazione Iniziale**

        ```
                                    p1
                                    v
        information  --> ... DOC7:  1   10      (27)    338     ...

                                    p2
                                    v
        retrieval    --> ... DOC7:  2   (28)    939     3127    ...

                                    p3
                                    v
        system       --> ... DOC7:  4   (29)                    ...
        
        ---

        p = 1
        i = 2
        s = 1

        pos(RETRIEVAL) = 1 + 2 - 1 = 2 = p2 --> OK

        p = 1
        i = 3
        s = 2

        pos(SYSTEM) = 1 + 3 - 2 = 3 != p3 = 4 --> NON CI SIAMO
        ```

    2. **Seconda Situazione**

        ```
                                        p1
                                        v
        information  --> ... DOC7:  1   10      (27)    338     ...

                                        p2
                                        v
        retrieval    --> ... DOC7:  2   (28)    939     3127    ...

                                        p3
                                        v
        system       --> ... DOC7:  4   (29)                    ...
        

        p = 10
        i = 2
        s = 1

        pos(RETRIEVAL) = 10 + 2 - 1 = 11 != p2 = 28 --> NON CI SIAMO
        ```

    3. **Terza Situazione**
    
        ```
                                                p1
                                                v
        information  --> ... DOC7:  1   10      (27)    338     ...

                                        p2
                                        v
        retrieval    --> ... DOC7:  2   (28)    939     3127    ...

                                        p3
                                        v
        system       --> ... DOC7:  4   (29)                    ...
        
        ---

        p = 27
        i = 2
        s = 1

        pos(RETRIEVAL) = 27 + 2 - 1 = 28 = p2 --> OK

        ---

        p = 27
        i = 3
        s = 2

        pos(SYSTEM) = 27 + 3 - 2 = 29 = p3 --> OK
        ```

    **CONCLUSIONI**

    Il documento 7 (DOC7) è ritornato dal sistema di IR perchè matcha la Phrasal Query correttamente.

#### IMPORTANTE

In realtà il l'esercizio svolto in precedenza non è completamente corretto... la **"lista delle posizioni principale"** è quella **più corta** tra quelle delle tre parole. Quindi la lista principale non è quella di *"information"* ma quella di *"system"*. Di conseguenza le descrizioni dei valori della formula diventano:

Formula: **(p + i - s)**

- **p** = posizione della parola Principale ("system") all'interno della sua posting list (indicata da p1).
- **i** = posizione di una parola secondaria ("information" o "retrieval") nella query.
- **s** = offset tra la parola Principale ("system") e la parola Secondaria ("information" o "retrieval") nella query.

#### PSEUDOCODICE ALGORITMO

1. **Inizializzazione**: Creiamo un insieme vuoto $R$, che conterrà i documenti in cui la frase appare esattamente.
2. **Iteriamo sui documenti candidati** (ovvero quelli che contengono tutte le parole della frase):
    - Per ogni documento $d$ in $D$:
        1. **Otteniamo le posizioni delle parole**: Per ogni parola $k_i$ nella frase, estraiamo l'array $P_i$ contenente le posizioni in cui appare in $d$.
        2. **Troviamo l'array più corto**: Scegliamo $Ps$, l'array con il minor numero di posizioni (per ridurre il numero di controlli).
        3. **Verifichiamo la sequenza di parole**
            - Per ogni posizione $p$ della parola centrale $ks$ in $Ps$:
                - Per ogni altra parola ki della frase:
                    1. Usiamo ricerca binaria per verificare se $(p + i - s)$ è presente in $P_i$ (cioè, se le parole appaiono in sequenza corretta).
        4. Se la frase appare in ordine corretto, aggiungiamo $d$ a $R$.
3. **Restituiamo** $R$, ovvero i documenti che contengono la frase nella sequenza richiesta.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO 5.2) PHRASAL RETRIEVAL

#### SPIEGAZIONE

- Se l'esercizio richiede di effettuare una Proximity Retrieval, il procedimento è lo stesso del Phrasal Retrieval ma invece di calcolare la posizione esatta dei termini successivi, si calcola un range di posizioni ammissibili. Attraverso le seguenti formule:

  - Posizione minima: (p + i - s)
  - Posizione massima: (p + i - s) + w - 1

- Tramite l'algoritmo della Binary Search cerco all'interno della lista di posizioni della seconda parola all'intenro del documento D una posizione che sia tra la posizione minima e la posizione massima calcolate.

- La modifica da apportare allo pseudocodice nel caso si parli di Proximity Retrieval è semplicemente una. Quando verifichiamo la sequenza delle parole, effettuiamo una ricerca binaria che accetta molteplici valori appartenenti ad un range. Il range dipende dalla distanza massima $w$ tra le parole.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->