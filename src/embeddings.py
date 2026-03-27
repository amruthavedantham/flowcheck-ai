from sentence_transformers import SentenceTransformer

# load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(steps):
    """
    Convert list of steps into embeddings
    """

    embeddings = model.encode(steps)

    return embeddings