# Git Commands Retrieval System

This approach implements a retrieval system for commonly used Git commands using vector embeddings and similarity search. It consists of two main components: a vector store creation script and a query interface.

## Components

### 1. VectorStore

This script creates a vector store from a JSON file containing Git commands.

#### Features:
- Loads Git commands from a JSON file
- Uses HuggingFace embeddings (all-MiniLM-L6-v2 model) - Sentence Transformers
- Creates a persistent Chroma vector store

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
  },
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

## Contributing

We welcome contributions to improve and expand the Git Commands Retrieval System. Here are some ways you can contribute:

### Enhancing the JSON Data

1. Open the `GitCommands.json` file in the `CommandRetrieval` directory.
2. Add new Git commands or improve existing ones following the established format:
   ```json
   {
     "command": "git command",
     "description": "Detailed description of the command.",
     "parameters": [
       {
         "param": "parameter_name",
         "param_description": "Description of the parameter."
       }
     ]
   }
   ```
3. Ensure the JSON is valid after your changes.
4. Submit a pull request with your updates.

### Improving the Code

1. Fork the repository and create a new branch for your changes.
2. Make your improvements to either `VectorStore.py` or `GitCommands.py`.
3. Test your changes thoroughly.
4. Submit a pull request with a clear description of your improvements.

### Adding New Features

1. Open an issue to discuss the new feature you'd like to add.
2. Once approved, implement the feature in a new branch.
3. Update the README to reflect the new functionality.
4. Submit a pull request with your changes.

### Reporting Issues

If you encounter any bugs or have suggestions for improvements:

1. Check if the issue already exists in the project's issue tracker.
2. If not, create a new issue with a clear title and description.
3. Include steps to reproduce the problem and any relevant error messages.

By contributing, you help make this Git Commands Retrieval System more comprehensive and useful for everyone. Thank you for your support!
