import requests
import msgpack
from sentence_transformers import SentenceTransformer
from endee.index import json_unzip

model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_texts(obj):
    texts = []

    if isinstance(obj, dict):
        # direct text field
        if "text" in obj and isinstance(obj["text"], str):
            texts.append(obj["text"])

        # try unzip if this looks like zipped meta
        try:
            unzipped = json_unzip(obj)
            if isinstance(unzipped, dict) and "text" in unzipped and isinstance(unzipped["text"], str):
                texts.append(unzipped["text"])
        except Exception:
            pass

        for value in obj.values():
            texts.extend(extract_texts(value))

    elif isinstance(obj, list):
        for item in obj:
            texts.extend(extract_texts(item))

    elif isinstance(obj, tuple):
        for item in obj:
            texts.extend(extract_texts(item))

    elif isinstance(obj, bytes):
        try:
            decoded = obj.decode("utf-8", errors="ignore")
            if decoded.strip():
                texts.append(decoded)
        except Exception:
            pass

    return texts


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

    unpacker = msgpack.Unpacker(raw=False)
    unpacker.feed(response.content)
    results = list(unpacker)

    print("RAW ENDEE RESULTS:", results)

    contexts = extract_texts(results)

    # remove duplicates while preserving order
    unique_contexts = []
    seen = set()
    for text in contexts:
        cleaned = text.strip()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            unique_contexts.append(cleaned)

    return "\n\n".join(unique_contexts[:2]) if unique_contexts else "No relevant context found."