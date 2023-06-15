# Snowflake docs chatbot

This is a chatbot that can answer questions about Snowflake documentation.


## Installation

```bash
pip install -r requirements.txt
```

## Usage

0. Export OPENAI_API_KEY environment variable.

    ```bash
    export OPENAI_API_KEY=<your key>
    ```

1. Download data from docs.snowflake.com, create embeddings and save them to a local vector database.

    ```bash
    python chat/prep.py
    ```

2. Ask questions!
    
    ```bash
    python chat/chat.py
    ```
