from endee import Endee, Precision

client = Endee()
index_name = "heart_risk_assist"
try:
    client.delete_index(name=index_name)
    print(f"Deleted old index: {index_name}")
except Exception:
    print("No old index to delete.")

client.create_index(
    name=index_name,
    dimension=384,
    space_type="cosine",
    precision=Precision.INT8
)

print(f"Created fresh index: {index_name}")