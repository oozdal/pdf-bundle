from src.pdfBundle.pinecone import connector, query_vectors
from src.pdfBundle.read_pdf import read_document
from src.pdfBundle.chunk_data import chunk_data
from src.pdfBundle.transformer import encoder
from src.pdfBundle.download_file import download_file_from_s3
from src.pdfBundle.upload_file import upload_file_to_s3
from pydantic import BaseModel, constr
from fastapi import FastAPI
from fastapi import status
import json, os


app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'Healthy'}



@app.post("/query_search")
async def query_search(prompt: str = "rshar-Tnitldy.KnmfOXodpr(:6636-66460Ctakhm:HqdkZmc.\u0000rrnbhZshnmenqBnlotsZshnmZkKhmfthrshbr0Wt:X0",
                    n_top: int = 2):

    # Pinecone Connection
    _, index, *_ = connector()

    # Download the input file from AWS S3 bucket
    bucket_name = 'pdfbundle'
    filename = '2401.15050.pdf'
    local_file_path = './research/documents/sample_test.pdf'

    # Check if the file already exists
    if not os.path.isfile(local_file_path):
        print(f"{local_file_path} not found. Downloading from S3...")
        download_file_from_s3(bucket_name, filename, local_file_path)
    else:
        print(f"{local_file_path} already exists. No need to download.")

    # Read the document
    doc=read_document(local_file_path)

    # Chunck the data
    documents=chunk_data(docs=doc)

    # Page content of the document as a list of sentences
    sentences = [document.page_content for document in documents]

    # Embeddings of the sentences by a toy model, which can ben replaced by a real model later on
    model, _ = encoder(sentences)

    # Query the embeddings
    query_response = query_vectors(index, model, prompt=prompt, k=n_top)
    
    results = {"ID" : [], "cosine_similarity": []}
    matches = query_response.get("matches")
    for count in range(len(matches)):
        results['ID'].append(matches[count]['id'])
        results['cosine_similarity'].append(matches[count]['score'])

    # Save query response as a json file
    response = query_response.to_dict()
    response_file_path = 'responses/query_response.json'
    with open(response_file_path, 'w') as outfile:
        json.dump(response, outfile)

    # Upload the response json to AWS S3 bucket
    # upload_file_to_s3(response_file_path, bucket_name, )

    # Return a simplified version of the query response
    return {"Response" : results}
