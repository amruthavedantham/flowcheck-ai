import faiss
import numpy as np

def build_faiss_index(embeddings):
    """
    Create FAISS index from embeddings
    """

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index


def search_similar(index, query_embedding, k=2):
    """
    Find top k similar steps
    """

    query_embedding = np.array([query_embedding])

    distances, indices = index.search(query_embedding, k)

    return distances, indices