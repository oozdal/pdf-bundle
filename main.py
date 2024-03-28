from src.pdfBundle.pinecone import connector, query_vectors
from src.pdfBundle.read_pdf import read_document
from src.pdfBundle.chunk_data import chunk_data
from src.pdfBundle.transformer import encoder
from fastapi import FastAPI
from fastapi import status


app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'Healthy'}


@app.post("/query_search")
async def query_search(prompt: str = "rshar-Tnitldy.KnmfOXodpr(:6636-66460Ctakhm:HqdkZmc.\u0000rrnbhZshnmenqBnlotsZshnmZkKhmfthrshbr0Wt:X0",
                    k: int = 2):

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
    #our_prompt = "Document AI is a growing research field that focuses on the comprehension and extraction of information"
    query_response = query_vectors(index, model, prompt=prompt, k=k)
    
    results = {"ID" : [], "cosine_similarity": []}
    matches = query_response.get("matches")
    for count in range(len(matches)):
        results['ID'].append(matches[count]['id'])
        results['cosine_similarity'].append(matches[count]['score'])

    return {"Response" : results}
