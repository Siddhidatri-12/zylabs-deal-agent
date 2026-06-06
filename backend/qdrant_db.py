from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import uuid
COLLECTION_NAME = "zylabs_kb"

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to Qdrant
client = QdrantClient("localhost", port=6333)


def create_collection():
    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION_NAME not in existing:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )
        print("Collection created")
    else:
        print("Collection already exists")


def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_text(text)


def store_chunks(chunks):

    points = []

    for chunk in chunks:
        vector = embedding_model.encode(chunk).tolist()

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "text": chunk
                }
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )

    print(f"{len(chunks)} chunks stored")


if __name__ == "__main__":

    create_collection()

    text = load_documents("data/knowledge_base.txt")

    chunks = chunk_text(text)

    store_chunks(chunks)

    print("Knowledge Base Loaded Successfully")