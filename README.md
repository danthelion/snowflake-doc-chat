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
    python chat/retrieve.py \
     --query "You want to block certain IP addresses from establishing a connection to your Snowflake account.
            Which mechanism would you use?"

    
    You can use a network policy to block certain IP addresses from connecting to your Snowflake account.
    This can be done by creating or editing a network policy and adding the IP addresses to the blocked IP address list.

    Sources:

    https://docs.snowflake.com/en/user-guide/network-policies
    https://docs.snowflake.com/en/user-guide/privatelink-azure
    ```
