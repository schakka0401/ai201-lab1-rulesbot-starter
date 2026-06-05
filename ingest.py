from documents import load_documents, chunk_document
from retriever import embed_and_store

documents = load_documents()

for doc in documents:
    chunks = chunk_document(doc["text"], doc["game"])
    embed_and_store(chunks)