# Spec: `generate_response()`

**File:** `generator.py`
**Status:** Spec incomplete — fill in all blank fields before implementing

---

## Purpose

Given a user query and a list of retrieved rule chunks, generate a response that directly answers the question using only the retrieved text as context. The response must be grounded — it should not draw on the model's general knowledge of board games, only on what was retrieved.

---

## Input / Output Contract

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `query` | `str` | The user's original question |
| `retrieved_chunks` | `list[dict]` | Ranked list of chunks from `retrieve()`, each with `"text"`, `"game"`, and `"distance"` |

**Output:** `str`

A plain string containing the response to show the user. The response should:
- Answer the question using only the retrieved rule text
- Identify which game the answer comes from
- Acknowledge clearly when the answer is not found in the loaded rules

Returns a fallback string (not an error) when `retrieved_chunks` is empty.

---

## Design Decisions

*Complete the fields below before writing any code. Use your AI tool in Plan or Ask mode to help you reason through what belongs here — but the decisions are yours.*

---

### Context formatting

*How will you format the retrieved chunks before passing them to the LLM? Describe the structure — not the code. Consider: will you label chunks by game? Include distance scores? Separate chunks with delimiters?*

```
[your answer here]
```

---

### System prompt — grounding instruction

*Write the exact system prompt instruction you will use to prevent the model from answering beyond the retrieved text. This is the most important design decision in this function.*

```
[your answer here]
```

---

### System prompt — citation instruction

*Write the exact instruction you will use to tell the model to identify which game its answer comes from.*

```
[your answer here]
```

---

### Fallback behavior

*What should the response say when the answer isn't found in the loaded rule books? Write the exact fallback message.*

```
[your answer here]
```

---

### Handling low-relevance chunks

*`retrieved_chunks` may include chunks with high distance scores (weak relevance). Will you filter these out before building context, pass them all in, or handle them another way? What are the tradeoffs?*

```
The current implementation passes all retrieved chunks through without filtering 
by distance score. The tradeoff is simplicity — no relevant chunks are accidentally 
dropped — but it risks sending weakly related context to the model, which could 
pull the response off-track. An alternative would be filtering out chunks above a 
distance threshold (e.g. 0.7), which improves precision but could leave the model 
with no context at all for unusual queries. For a rules bot with only 8 games, 
passing all chunks is a reasonable default since N_RESULTS is already capped at 3.
```

---

### Message structure

*Describe how you will structure the messages list for the API call — what goes in the system message vs. the user message?*

```
The system message contains two things: the grounding instructions (telling the 
model to answer only from the retrieved context, cite the game, and admit when 
the answer isn't in the rules) and the full formatted context block of retrieved 
chunks. The user message contains only the raw query string. This keeps the 
model's behavioral constraints and reference material separate from the question 
itself, which is the standard structure for RAG prompt design.
```

---

## Implementation Notes

*Fill this in after implementing and testing.*

**Test query and response:**

```
Query: [your test query]
Response: [abbreviated response]
Correctly grounded? [yes / no]
Cited the right game? [yes / no]
```

**One thing you changed from your original spec after seeing the actual output:**

```
[your answer here]
```
