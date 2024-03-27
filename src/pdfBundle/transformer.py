from sentence_transformers import SentenceTransformer

def encoder(sentences):

    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Sentences are encoded by calling model.encode()
    embeddings = model.encode(sentences)

    return model, embeddings