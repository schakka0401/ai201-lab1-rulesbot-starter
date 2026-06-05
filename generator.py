def retrieve(query, n_results=N_RESULTS):
    if _collection.count() == 0:
        return []

    results = _collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return [
        {
            "text": doc,
            "game": meta["game"],
            "distance": dist,
        }
        for doc, meta, dist in zip(documents, metadatas, distances)
    ]