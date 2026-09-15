from whoosh.index import open_dir
from whoosh.qparser import QueryParser

if __name__ == '__name__':
    
    ix = open_dir("indexdir")
    
    searcher = ix.searcher()
    
    parser = QueryParser("content", ix.schema)
    
    query = parser.parse(u"first")
    
    results = searcher.search(query)
    
    print(results[0])