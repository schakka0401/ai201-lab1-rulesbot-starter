from documents import load_documents, chunk_document

total = sum(len(chunk_document(d["text"], d["game"]))
            for d in load_documents())
print(total)