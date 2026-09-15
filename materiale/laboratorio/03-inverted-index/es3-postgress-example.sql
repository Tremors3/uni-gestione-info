
-- Converte la stringa in un tipo tsvector, che è una rappresentazione di un documento 
-- come un insieme di token per il full-text search in PostgreSQL.
--
SELECT 'there are two cats in the room'::tsvector;

-- Utilizza la funzione to_tsvector specificando la lingua (english) per tokenizzare la frase, applicando:
-- 1) Stemming,
-- 2) Lemmatization,
-- 3) Rimozione stopwords
-- Restituendo l'output nel seguente formato:
-- 		'<token1>':<posizione> '<token2>':<posizione> ...
--
SELECT to_tsvector( 'english', 'there are two cats in the room' );

-- Converte la stringa in un tipo tsquery, che rappresenta una query di ricerca full-text, 
-- dove "cat" e "room" devono essere entrambi presenti nel documento per restituire un risultato positivo.
--
SELECT 'cats & room'::tsquery;

-- Come il precedente, ma utilizza la funzione to_tsquery per creare una query di full-text search in inglese.
-- La query cerca i termini "cat" e "room", riducendo le parole alla loro radice, se possibile (ad esempio "cats" diventa "cat").
--
SELECT to_tsquery('english','cats & room');

-- Crea una query che cerca "Cats" o "Rooms". Qui l'operatore | indica che uno dei due termini deve essere presente.
--
SELECT to_tsquery('english','Cats | Rooms');

-- Esegue una ricerca utilizzando un tsvector e un tsquery.
-- Controlla se la frase "there are two cats in the room" contiene sia "cat" che "room". Il risultato è un valore booleano.
--
SELECT 'there are two cats in the room'::tsvector @@ 'cat & room'::tsquery;

-- Esegue la stessa ricerca ma con la funzione to_tsvector e to_tsquery in inglese. Cerca se i termini "Cats" e "Rooms" 
-- (dopo lo stemming "cat" e "room") sono presenti nel testo anchesso stemmizzato.
--
SELECT to_tsvector('english','there are two cats in the room') @@ to_tsquery('english','Cats & Rooms');

-- Esegue una ricerca di prossimità, controllando se "fatal" ed "error" appaiono vicini (in questo caso direttamente adiacenti) nel testo.
-- L'operatore <-> indica che i due termini devono essere l'uno accanto all'altro. L'ordine è importante.
--
SELECT to_tsvector('fatal error') @@ to_tsquery('fatal <-> error');
SELECT to_tsvector('fatal error') @@ to_tsquery('error <-> fatal');

-- Esegue una ricerca di prossimità, controllando se "error" ed "fatal" appaiono vicini (in questo caso a distanza massima N) nel testo.
-- L'operatore <N> indica che i due termini devono essere l'uno distante massimo N parole dall'altro.
-- Anche in questo caso l'ordine delle parole è importante.
--
SELECT to_tsvector('error is not fatal') @@ to_tsquery('error <3> fatal');
SELECT to_tsvector('error is not fatal') @@ to_tsquery('error <2> fatal');