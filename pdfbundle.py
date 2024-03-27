from src.pdfBundle.pinecone import connector, query_vectors
from src.pdfBundle.read_pdf import read_document
from src.pdfBundle.chunk_data import chunk_data
from src.pdfBundle.transformer import encoder


# Pinecone Connection
pc, index = connector()

# Read the document
doc=read_document('research/documents/')

# Chunck the data
documents=chunk_data(docs=doc)

# Page content of the document as a list of sentences
sentences = [document.page_content for document in documents]

# Embeddings of the sentences by a toy model, which can ben replaced by a real model later on
model, embeddings = encoder(sentences)

# Query the embeddings
our_prompt = "Document AI is a growing research field that focuses on the comprehension and extraction of information"
query_response = query_vectors(index, model, prompt=our_prompt)


