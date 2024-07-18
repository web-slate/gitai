
# Git Commands Retrieval System

This appraoch implements a retrieval system for commonly used Git commands using vector embeddings and similarity search. It consists of two main components: a vector store creation script and a query interface.

## Components

### 1. VectorStore

This script creates a vector store from a JSON file containing Git commands.

#### Features:
- Loads Git commands from a JSON file
- Uses HuggingFace embeddings (all-MiniLM-L6-v2 model) - Sentence Transformers
- Creates a persistent a Chroma vector store


### 2. Git Commands Search

This script provides an interactive interface to query Git commands.

#### Features:
- Loads the pre-created Chroma vector store
- Accepts user queries in natural language
- Performs similarity search to find relevant Git commands
- Displays structured information about the retrieved commands

## Setup

1. Ensure you have the required dependencies installed:
   ```
   pip install langchain langchain_community langchain_huggingface chromadb sentence_transformers
   ```

2. Prepare your Git commands data in a JSON file named `GitCommands.json` in the `CommandRetrieval` directory.

3. Run `VectorStore.py` to create the vector store:

   ```
   python VectorStore.py
   ```

4. Use `GitCommands.py` to query Git commands:
   ```
   python GitCommands.py
   ```

## Data Format

The `GitCommands.json` file should contain an array of objects with the following structure:

```json
[
  {
    "command": "git diff <commit1> <commit2>",
    "description": "Displays the differences between two commits.",
    "parameters": [
      {
        "param": "<commit1>",
        "param_description": "The ID or reference of the first commit."
      },
      {
        "param": "<commit2>",
        "param_description": "The ID or reference of the second commit."
      }
    ]
  }
  ...
]
```

## How It Works

1. `VectorStore.py` loads the Git commands from the JSON file, creates embeddings for each command, and stores them in a Chroma vector store.

2. `GitCommands.py` loads the pre-created vector store and waits for user input.

3. When a user enters a query, the script performs a similarity search to find the most relevant Git commands.

4. The retrieved commands are displayed with their descriptions and parameters.

## Customization

- To use a different embedding model, modify the `model_name` parameter in the `HuggingFaceEmbeddings` initialization.
- Adjust the number of results returned by modifying the `k` parameter in the similarity search.

