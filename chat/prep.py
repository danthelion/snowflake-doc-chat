import os
from loader.get_docs import get_docs
from loader.create_embeddings import create_embeddings
from utils.constants import WORKING_DIR, RAW_DATA_DIR, VECTOR_DB_DIR

if __name__ == "__main__":
    print(f"Working directory: {WORKING_DIR}")
    print(f"Raw data directory: {RAW_DATA_DIR}")
    print(f"Vector database directory: {VECTOR_DB_DIR}")

    os.makedirs(WORKING_DIR, exist_ok=True)
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    os.makedirs(VECTOR_DB_DIR, exist_ok=True)

    get_docs()
    create_embeddings()
