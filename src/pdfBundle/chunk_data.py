from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_data(docs,chunk_size=300,chunk_overlap=50):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    doc=text_splitter.split_documents(docs)
    return doc

