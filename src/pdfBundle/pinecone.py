import os
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()


def connector():
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    list_indexes = pc.list_indexes()
    pinecone_host = list_indexes[0]['host']
    index = pc.Index(host=pinecone_host)
    return pc, index, pinecone_host


def upsert_vectors(index, sentences, embeddings):

    vectors = []

    for count, (sentence, embedding) in enumerate(zip(sentences, embeddings), start=1):
        embedding = [float(i) for i in embedding]
        tupl = ("VectorID"+str(count), embedding, {"sentence": sentence})
        vectors.append(tupl)

    upsert_response = index.upsert(
    vectors=vectors,
    namespace="example-namespace"
    )

    return upsert_response


def query_vectors(index, model, prompt, k=2, namespace="example-namespace"):

    embedded_prompt = model.encode(prompt)

    query_response = index.query(
        namespace=namespace,
        vector=[float(i) for i in embedded_prompt],
        top_k=k,
        include_values=True,
        include_metadata=True,
    )

    return query_response
