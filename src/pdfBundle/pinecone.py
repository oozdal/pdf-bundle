import os
from pinecone import Pinecone


def connector():
    pc = Pinecone(api_key="00de6be5-b2b9-49bc-8630-a2c2ed8d94a6")
    index = pc.Index(host='langchainvector-81vyvdw.svc.gcp-starter.pinecone.io')
    return pc, index


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
