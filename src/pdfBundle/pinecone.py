import os
from pinecone import Pinecone
from dotenv import load_dotenv
import logging
from pinecone.core.client.exceptions import PineconeApiException

load_dotenv()


def connector():
    """
    Connect to the Pinecone server and return some connector objects
    """
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    pinecone_host = os.getenv('PINECONE_HOST')
    index = pc.Index(host=pinecone_host)

    return pc, index, pinecone_host


def upsert_vectors(index, sentences, embeddings):
    """
    Upsert the provided sentences and their embeddings into the Pinecone index
    """

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
    """
    Query the Pinecone index using the provided prompt and return the top k matching vectors
    """

    try:
        # Encode the prompt using the provided model
        embedded_prompt = model.encode(prompt)

        # Log the encoded prompt for debugging purposes
        logging.debug(f"Encoded prompt: {embedded_prompt}")

        # Ensure the encoded prompt is a list of floats
        vector = [float(i) for i in embedded_prompt]

        # Log the vector to be queried
        logging.debug(f"Query vector: {vector}")

        # Query the Pinecone index
        query_response = index.query(
            namespace=namespace,
            vector=vector,
            top_k=k,
            include_values=True,
            include_metadata=True,
        )

        # Log the query response
        logging.debug(f"Query response: {query_response}")

        return query_response

    except PineconeApiException as e:
        logging.error(f"Pinecone API Exception: {e}")
        raise e
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise e
