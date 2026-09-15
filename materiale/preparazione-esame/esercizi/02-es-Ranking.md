<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO - BOOLEAN MODEL vs FUZZY MODEL

#### QUESITO

Facendo riferimento ai tre documenti precedenti, mostrare il risultato dell’esecuzione della query *"autobus AND viaggio"* integrando i dati mancanti con valori a piacere, utilizzando modello Booleano e modello Fuzzy.

```
Doc1: "venire casa autobus"
Doc2: "autobus autobus treno viaggio"
Doc3: "casa viaggio viaggio"
```

#### RISPOSTA

MODELLO BOOLEANO:

- Un documento è rilevante solamente se contiene entrambi i termini *"autobus"* e *"viaggio"*.
```
DOC  "autobus" "viaggio" RILEVANTE?
doc1    1          0         no
doc2    1          1         SI
doc3    0          1         no
```

- Risultato: Solamente il Documento 2 viene restituito.

MODELLO FUZZY:

- Per ogni documento definiamo un grado di appartenenza in base alla frequenza dei termini.

    $$ \mu(d) = \min\frac{TF("autobus", d)}{\max_{\forall{d_j}} TF("autobus", d_j) }, \frac{TF("viaggio", d)}{\max_{\forall d_j}TF("viaggio", d_j)} $$

    Dove normalizziamo la frequenza del termine rispetto al massimo valore presente nei documenti.

    - Doc1: "autobus" appare **1 volta** (su max 2), "viaggio" **non appare** $\rightarrow\mu=0$
    - Doc2: "autobus" appare **2 volte** (su max 2), "viaggio" appare **1 volta** (su max 2) $\rightarrow\mu=\min{(\frac{2}{2},\frac{1}{2})}=\frac{1}{2}$
    - Doc3: "autobus" **non appare**, "viaggio" appare **1 volta** (su max 2) $\rightarrow\mu=0$

RISULTATO:

- Doc1 = $0$
- Doc2 = $0.5$
- Doc3 = $0$

Il **Documento 2** è il più rilevante, ma con un peso fuzzy di $0.5$ invece di $1$

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO - VECTOR SPACE MODEL: ESERCIZIO SIMILARITA' COSENO 

#### QUESITO

Data la seguente matrice di incidenza calcola i valori di similarità di ciascun documento nei confronti della query. Per semplicità tutti i pesi della tabella sono impostati a valore 1.

Q = *"gold silver truck"*

```
   arrive damage deliver fire gold silver shipment truck
D1  0       1       0      1    1    0       1       0
D2  1       0       1      0    0    1       0       1
D3  1       0       0      0    1    0       1       1
D4  1       1       0      0    1    0       1       1
Q   0       0       0      0    1    1       0       1
```

#### RISPOSTA

Formula della similarità coseno:

$$ sim(\vec{d_j}, \vec{q}) = \frac{\vec{d_j}\cdot\vec{q}}{|\vec{d_j}|\cdot|\vec{q}|} = \frac{\sum_{i=1}^t w_{ij}\cdot w_{iq}}{\sqrt{\sum_{i=1}^t w_{ij}^2}\cdot\sqrt{\sum_{i=1}^t w_{iq}^2}} = \frac{\sum_{i=1}^t w_{ij}\cdot w_{iq}}{\sqrt{\sum_{i=1}^t w_{ij}^2}} $$

PROCEDURA RISOLUTIVA:

Per ciascun documento dobbiamo calcolare la similarità coseno rispetto alla query Q:

1. Andando da sinistra verso destra moltiplichiamo il valore sulla riga del documento per il corrispettivo sulla stessa colonna ma nella riga della query; sommando i valori e ottenendo il risultato al numeratore.

2. Per il denominatore ci basta andare da sinistra verso destra sulla riga del documento contando e sommando le frequenze dei termini. Poi poniamo il risultato sotto la radice quadrata

3. Evitiamo di specificare la seconda parte del denominatore perchè è costante e possiamo non considerarla, evitando così di perdere del tempo.

RISOLUZIONE:

$$ \text{Document 1°: } sim(\vec{d_1}, \vec{q}) = \frac{1}{\sqrt{4}} \approx 0.50 $$

$$ \text{Document 2°: } sim(\vec{d_2}, \vec{q}) = \frac{2}{\sqrt{4}} = 1 $$

$$ \text{Document 3°: } sim(\vec{d_3}, \vec{q}) = \frac{2}{\sqrt{4}} = 1 $$

$$ \text{Document 4°: } sim(\vec{d_4}, \vec{q}) = \frac{2}{\sqrt{5}} \approx 0.89 $$

RANKING:

$$ \text{Ranking} = d_3, d_2, d_4, d_1 $$

#### OSSERVAZIONE

- Nel caso **non ci venga fornita la matrice di incidenza**, dobbiamo realizzarla noi:
    1. Per ciascun termine $t_i$ di ciascun documento $d_j$ calcoliamo il valore $w_{ij} = \textit{TF-IDF}(t_i, d_j, D)$.
    2. Nel frattempo andiamo a costruire la matrice di incidenza con i documenti sulle righe e i termini sulle colonne.
    3. Inseriamo all'interno della matrice i valori dei pesi appena calcolati fino a riempire la tabella.
    4. Inseriamo la riga relativa alla query in fondo alla tabella.
- **ATTENZIONE**: Ricordarsi di seguire la formula; i pesi non saranno più uguali ad $1$ quindi al denominatore andranno elevati al quadrato prima di sommarli.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO - VECTOR SPACE MODEL: ESERCIZIO TF-IDF

#### QUESITO

Calcolare il peso dei termini del vocabolario e rispetto ai documenti forniti, assumendo di usare la formula **TF * IDF**.

```
Doc1: "venire casa autobus"
Doc2: "autobus autobus treno viaggio"
Doc3: "casa viaggio viaggio"
```

#### RISPOSTA

Formula della frequenza del termine, della frequenza inversa del documento e TF-IDF:

$$ \text{TermFrequency}(t, d) = \text{\# of t in document d} $$

$$ \text{InverseDocumentFrequency}(t, D) = \log{\frac{N}{|\{d \in D: t \in d\}|}}$$

$$ \text{TF-IDF}(t, d, D) = \text{TF}(t, d) \cdot \text{IDF}(t, D) $$

PROCEDURA RISOLUTIVA:

Per ciascuna parola di ciascun documento dobbiamo calcolare il corrispettivo peso:

  1. Primo documento:

  $$ w_{\text{venire,}1} = 1 \cdot \log{ \frac{3}{1} } \approx 0.47 $$

  $$ w_{\text{casa,}1} = 1 \cdot \log{ \frac{3}{2} } \approx 0.17 $$

  $$ w_{\text{autobus,}1} = 1 \cdot \log{ \frac{3}{2} } \approx 0.17 $$

  2. Secondo Documento:

  $$ w_{\text{autobus,}2} = 2 \cdot \log{ \frac{3}{2} } \approx 0.35 $$

  $$ w_{\text{treno,}2} = 1 \cdot \log{ \frac{3}{1} } \approx 0.47 $$

  $$ w_{\text{viaggio,}2} = 1 \cdot \log{ \frac{3}{2} } \approx 0.17 $$

  1. Terzo Documento:

  $$ w_{\text{casa,}3} = 1 \cdot \log{ \frac{3}{2} } \approx 0.17 $$

  $$ w_{\text{viaggio,}3} = 2 \cdot \log{ \frac{3}{2} } \approx 0.35 $$

Successivamente è possibile costruire la matrice di incidenza e compilarla con i pesi appena calcolati.

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO - BINARY INDIPENDENCE MODEL: ESERCIZIO RANKING

#### QUESITO

Dato l'insieme dei documenti $\{D1,D2,D3\}$ e la queru $Q$, effettuare il ranking utilizzando le formule descritte nel **BMI**.

```
Q: "gold silver truck"

D1: "Shipment of gold dameged in a fire."
D2: "Delivery of silver arrived in a silver truck."
D3: "Shipment of gold arrived in a truck."

Assumi: V = {D2, D3}
```

#### RISPOSTA

Formule probabilità successive con lo smoothing:

$$P(k_i|R) = \frac{V_i + 0.5}{V + 1} \hspace{20pt} P(k_i|\bar{R}) = \frac{n_i - V_i + 0.5}{N - V + 1} $$

Formula del discriminatore di rilevanza:

$$ c_i = \log{ \frac{V_i + 0.5}{V - V_i + 0.5} \; \div \; \frac{n_i - V_i + 0.5}{(N - n_i) - (V - V_i) + 0.5} }$$

PROCEDURA RISOLUTIVA:

0. Nel caso in cui non sia stato indicato nell'esercizio, scegliere un insieme iniziale V. In questo caso ci è già stato fornito:

    - $V = \{D2, D3\}$

1. Costruzione della seguente tabella:

    | TIPO  | gold | silver | truck | DESC |
    |-------|------|--------|-------| ---- |
    | N     | 3    | 3      | 3     | Numero totale di documenti. |
    | V     | 2    | 2      | 2     | Numero di documenti rilevanti. |
    | $n_i$ | 2    | 1      | 2     | Numero di documenti che contengono il termine $k_i$. |
    | $V_i$ | 1    | 1      | 2     | Numero di documenti rilevanti che contengono il termine $k_i$. |

3. Per ciascun termine indicizzato $\{gold, silver, truck\}$ andiamo a calcolare il valore di $c_i$, nel seguente modo:

    $$ c_{\text{gold}} = \log \frac{1 + 0.5}{2 - 1 + 0.5} \; \div \; \frac{2 - 1 + 0.5}{(3 - 2) - (2 - 1) + 0.5} = \log \frac{1}{3} = -0.477 $$

    $$ c_{\text{silver}} = \log \frac{1 + 0.5}{2 - 1 + 0.5} \; \div \; \frac{1 - 1 + 0.5}{(3 - 1) - (2 - 1) + 0.5} = \log \frac{1}{0.333} = 0.477 $$

    $$ c_{\text{truck}} = \log \frac{2 + 0.5}{2 - 2 + 0.5} \; \div \; \frac{2 - 2 + 0.5}{(3 - 2) - (2 - 2) + 0.5} = \log \frac{5}{0.333} = 1.176 $$

4. Somma dei valori $c_i$ per ciascun documento:

    - $R_{\text{D1}} = c_{\text{gold}} = - 0.477$

    - $R_{\text{D2}} = c_{\text{silver}} + c_{\text{truck}} = 0.477 + 1.176 = 1.653$

    - $R_{\text{D3}} = c_{\text{gold}} + c_{\text{truck}} = -0.477 + 1.176 = 0.699$

    **RICORDA**: Il BMI **non considera la frequenza dei termini quando si calcola la Rilevanza**! Quindi anche se il documento $D2$ contiene due istanze della parola ***"silver"***, viene sommato una sola volta $c_{\text{silver}}$ invece di due!

#### FINE






<!-- XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX -->

## ESERCIZIO - FUZZY SET MODEL: ESERCIZIO CALCOLO GRADO DI RILEVANZA

#### QUESITO

Calcola il grado di rilevanza dei documenti rispetto alle query fornite:

```
For the Query: D_gold   = {(d1,0.8), (d2,0.5)}
For the Query: D_silver = {(d1,0.5), (d2,0.4)}
                              ^         ^
                              |         |
                     GUARDA LE COLONNE! NON LE RIGHE.
```

#### RISPOSTA

Formule:

$$ sim(Q_{and}, d) = \mu_{D_{A_1}} \cap \dotsc \cap \mu_{D_{A_n}} (d) = \min\{\mu_{A_i}(d) | i = 1 \dotsc n \} $$
$$ sim(Q_{or}, d) = \mu_{D_{A_1}} \cup \dotsc \cup \mu_{D_{A_n}} (d) = \max\{\mu_{A_i}(d) | i = 1 \dotsc n \} $$

PROCEDURA RISOLUTIVA:

- Per ciascuna colonna di gradi di appartenenza fornitaci dalla prof, nel caso di un AND prendiamo il valore minore, nel caso di un OR prendiamo il valore maggiore (MAX/MIN TRA LE COLONNE, NON LE RIGHE).
- Nel caso in cui per una data query, il punteggio è unguale a 0, se la query è di tipo AND allora il punteggio sarà per forza 0 perchè è il valore minore tra quelli possibili; se la query è di tipo OR allora il punteggio sarà comunque uguale al punteggio maggiore possibile: se però i punteggi sono tutti uguali a 0 allora il punteggio risultante è comunque 0.

    $$D_\text{gold AND silver} = \{(d_1, \min\{0.8, 0.5\}), (d_2, \min\{0.5, 0.4\})\} = \{(d_1,0.5), (d_2,0.4)\}$$
    $$D_\text{gold OR silver} = \{(d_1, \max\{0.8, 0.5\}), (d_2, \max\{0.5, 0.4\})\} = \{(d_1,0.8), (d_2,0.5)\}$$

#### FINE