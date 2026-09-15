from whoosh.index import (create_in, open_dir)
from whoosh.fields import *
import os, os.path

if __name__ == '__main__':
    
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT)
    
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")
    
    ix = create_in("indexdir", schema)
    
    writer = ix.writer()
    
    writer.add_document(title=u"First Document", path=u"/a", content=u"This is the first document we've added!")
    
    writer.add_document(title=u"Second Document", path=u"/b", content=u"This one is even more interesting!")
    
    writer.commit()