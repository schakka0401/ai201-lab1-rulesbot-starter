import os
from config import DOCS_PATH


def load_documents():
    documents = []
    for filename in sorted(os.listdir(DOCS_PATH)):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCS_PATH, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
            game_name = filename.replace(".txt", "").replace("_", " ").title()
            documents.append({
                "game": game_name,
                "filename": filename,
                "text": text,
            })
    print(f"Loaded {len(documents)} rule document(s): {[d['game'] for d in documents]}")
    return documents


def chunk_document(text, game_name):
    chunk_size = 300
    overlap = 50
    min_length = 50
    step = chunk_size - overlap
    prefix = game_name.lower().replace(" ", "_")
    raw = (text[start:start + chunk_size].strip()
           for start in range(0, len(text), step))
    return [
        {"text": chunk, "game": game_name, "chunk_id": f"{prefix}_{i}"}
        for i, chunk in enumerate(c for c in raw if len(c) >= min_length)
    ]
