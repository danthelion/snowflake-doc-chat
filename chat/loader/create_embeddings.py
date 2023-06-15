from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from utils.document_serde import load_docs_from_jsonl
from utils.constants import VECTOR_DB_DIR, RAW_DATA_DIR


def create_embeddings():
    docs = load_docs_from_jsonl(f"{RAW_DATA_DIR}/data.jsonl")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        length_function=len,
        chunk_overlap=200,
        separators=["\n", "\n\n", "\n\n\n"],
    )

    print(f"Splitting {len(docs)} documents")
    texts = splitter.split_documents(docs)

    embedding = OpenAIEmbeddings()

    print(f"Creating embeddings for {len(texts)} new documents")
    vectordb = Chroma.from_documents(
        documents=texts, embedding=embedding, persist_directory=VECTOR_DB_DIR
    )

    print(f"Persisting {len(texts)} embeddings to {VECTOR_DB_DIR}")
    vectordb.persist()
