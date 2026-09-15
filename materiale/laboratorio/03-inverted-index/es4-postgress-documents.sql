-- Creazione e Popolamento database dei documenti
CREATE TABLE IF NOT EXISTS documenti (title varchar(20), primiElementi varchar(50), altriElementi varchar(50));
DELETE FROM documenti;
INSERT INTO documenti(title, primiElementi, altriElementi) VALUES('frutta', 'mela pera', 'arancia pesca');
INSERT INTO documenti(title, primiElementi, altriElementi) VALUES('auto', 'alfa lancia', 'fiat mercedes');
INSERT INTO documenti(title, primiElementi, altriElementi) VALUES('vari', 'mela fiat', 'pera');
SELECT * FROM documenti;

-- TEST DI QUERY

-- Query di esempio
SELECT title FROM documenti WHERE to_tsvector(primiElementi)@@to_tsquery('mela');
SELECT title FROM documenti WHERE to_tsvector(primiElementi)@@to_tsquery('fiat');

-- TEST DI QUERY CON CONCATENAZIONE

-- Concatenando i campi interessati dalla query:
SELECT title FROM documenti WHERE to_tsvector(primiElementi || ' ' || altriElementi)@@to_tsquery('fiat');
-- se uno dei due campi è nullo NULL è necessario che utilizzo la funzione COALESCE();
-- che restituisce il primo valore non NULLO passato come argomento.
SELECT title FROM documenti WHERE to_tsvector(COALESCE(primiElementi, '') || ' ' || COALESCE(altriElementi, ''))
-- alternativamente utilizzare l'operatore OR:
SELECt title FROM documenti WHERE to_tsvector(primiElementi) @@ to_tsquery('fiat') OR to_tsvector(altriElementi) @@ to_tsquery('fiat')

-- CREAZIONE CAMPO

-- Creazione colonna tsvector
ALTER TABLE documenti ADD COLUMN primiEle_tsvector tsvector;
-- popolazione della colonna
UPDATE documenti SET primiEle_tsvector = to_tsvector(primiElementi);
-- specifichiamo l'indice invertito
CREATE INDEX primiEle_idx ON documenti USING GIN(primiEle_tsvector);

-- CREAZIONE CAMPO CONCATENATO

-- Creazione colonna tsvector
ALTER TABLE documenti ADD COLUMN tuttiEle_tsvector tsvector;
-- popolamento della colonna con il to_tsvector degli altri due campi concatenati.
UPDATE documenti SET tuttiEle_tsvector = to_tsvector(primiElementi || ' ' || altriElementi);
-- specifichiamo l'indice invertito
CREATE INDEX tuttiEle_idx ON documenti USING GIN(tuttiEle_tsvector)
-- test di una query con il nuovo campo composto dalla concatenazione degli altri due
SELECT title FROM documenti WHERE tuttiEle_tsvector@@to_tsquery('fiat');