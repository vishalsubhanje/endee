import requests
import msgpack
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_relevant_context(question):
    query_vector = model.encode(question).tolist()

    url = "http://localhost:8080/api/v1/index/heart_risk_assist/search"
    payload = {
        "k": 2,
        "ef": 50,
        "include_vectors": False,
        "vector": query_vector,
        "filter_params": {
            "prefilter_threshold": 1000,
            "boost_percentage": 10
        }
    }

    response = requests.post(url, json=payload)
    results = msgpack.unpackb(response.content, raw=False)

    contexts = []

    if isinstance(results, list):
        for item in results:
            try:
                if isinstance(item, list) and len(item) >= 2:
                    meta = item[1]
                    if isinstance(meta, dict):
                        text = meta.get("text")
                        if text:
                            contexts.append(text)
                elif isinstance(item, dict):
                    meta = item.get("meta", {})
                    if isinstance(meta, dict):
                        text = meta.get("text")
                        if text:
                            contexts.append(text)
            except Exception:
                pass

    return "\n\n".join(contexts) if contexts else "No relevant context found."