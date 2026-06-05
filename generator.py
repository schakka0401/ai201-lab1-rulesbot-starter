from groq import Groq
from config import GROQ_API_KEY, LLM_MODEL

_client = Groq(api_key=GROQ_API_KEY)


def generate_response(query, retrieved_chunks):
    if not retrieved_chunks:
        return (
            "I couldn't find anything relevant in the loaded rule books. "
            "Try rephrasing your question — or check that your ingestion pipeline is working."
        )

    context_parts = []
    for i, chunk in enumerate(retrieved_chunks, 1):
        context_parts.append(
            f"[Source {i} — Game: {chunk['game']}]\n{chunk['text']}"
        )
    context_block = "\n\n".join(context_parts)

    system_prompt = (
        "You are a board game rules assistant. Answer the user's question using "
        "ONLY the information in the provided context below. Follow these rules:\n"
        "1. Use only the retrieved context, not your own general knowledge.\n"
        "2. Always state which game the answer comes from.\n"
        "3. If the context does not contain the answer, say clearly that the "
        "answer isn't in the loaded rules — do not guess.\n\n"
        f"Context:\n{context_block}"
    )

    completion = _client.chat.completions.create(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ],
        temperature=0.2,
    )

    return completion.choices[0].message.content.strip()