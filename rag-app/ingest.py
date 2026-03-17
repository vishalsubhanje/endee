from pathlib import Path
import numpy as np
import msgpack
import requests
from sentence_transformers import SentenceTransformer
from endee.index import json_zip

model = SentenceTransformer("all-MiniLM-L6-v2")
data_folder = Path("data")

documents = []
ids = []
metas = []

for i, file_path in enumerate(data_folder.glob("*.txt"), start=1):
    text = file_path.read_text(encoding="utf-8").strip()
    if text:
        documents.append(text)
        ids.append(f"doc_{i}")
        metas.append({"source": file_path.name, "text": text})

vectors = model.encode(documents)
norms = np.linalg.norm(vectors, axis=1)

vector_batch = []
for i in range(len(documents)):
    obj = [
        ids[i],                 # id
        json_zip(metas[i]),     # meta
        "{}",                   # filter
        float(norms[i]),        # norm
        vectors[i].tolist()     # vector
    ]
    vector_batch.append(obj)

payload = msgpack.packb(vector_batch, use_bin_type=True, use_single_float=True)

url = "http://localhost:8080/api/v1/index/heart_risk_assist/vector/insert"
headers = {
    "Content-Type": "application/msgpack"
}

response = requests.post(url, data=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.text)