import lucene
lucene.initVM()

from org.apache.lucene.analysis import (
    Analyzer
)

from org.apache.lucene.analysis.standard import (
    StandardAnalyzer
)

from org.apache.lucene.document import (
    Document, Field, TextField, StringField
)

from org.apache.lucene import *

if __name__ == '__main__':
    
    ## CREATING A DOCUMENT WITH FIELDS
    
    doc = Document()
    doc.add(Field("title", "Lucene in action", TextField.TYPE_STORED))
    doc.add(Field("isbn", "19339881", StringField.TYPE_STORED))
    
    ## INDEXING
    
    #...