# backend/rag.py

from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

COLLECTION_NAME = "zylabs_kb"

client = QdrantClient(
    host="localhost",
    port=6333
)

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_context(query, top_k=3):

    query_vector = embedding_model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=top_k
    )

    context = []

    for point in results.points:
        context.append(
            point.payload["text"]
        )

    return "\n".join(context)