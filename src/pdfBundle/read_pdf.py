import langchain
from langchain.document_loaders import PyPDFDirectoryLoader


def read_document(directory):
    """
    Reads the document
    """
    file_loader=PyPDFDirectoryLoader(directory)
    documents=file_loader.load()
    return documents