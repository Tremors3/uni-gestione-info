from urllib import request
import ssl

urls = ["https://www.gutenberg.org/files/2554/2554-0.txt", 
        "https://www.gutenberg.org/files/66419/66419-0.txt"]

def acquireText(url: str) -> str:
    """
    Acquisisce il testo da un URL fornito e lo restituisce come stringa.
    
    Parametri:
        url (str): L'URL del testo da scaricare.
    
    Ritorna:
        str: Il contenuto del testo recuperato dall'URL, decodificato in UTF-8.
    """
    
    # Creazione di un contesto SSL che non verifica i certificati, necessario per evitare errori SSL
    context = ssl._create_unverified_context()
    
    # Apertura dell'URL con il contesto SSL non verificato
    response = request.urlopen(url, context=context)
    
    # Lettura del contenuto e decodifica come UTF-8
    return response.read().decode('utf8')