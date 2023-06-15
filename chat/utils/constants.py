import os

WORKING_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "working",
)
RAW_DATA_DIR = os.path.join(WORKING_DIR, "raw_data")
VECTOR_DB_DIR = os.path.join(WORKING_DIR, "db")
