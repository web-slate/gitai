# RAG QA Bot 

This is a Retrieval-Augmented Generation (RAG) Question Answering Bot specifically designed for Git-related queries. It uses the EmbedChain library to create a QA system with customizable language models, embeddings, and vector databases.

## Features
- Uses Mistral-7B-Instruct-v0.2 as the language model (Hugging Face Inference)
- Employs sentence-transformers/all-mpnet-base-v2 for text embeddings
- Utilizes Chroma as the vector database for efficient retrieval
- Provides natural language answers to Git-related questions

## Prerequisites
- Hugging Face account and access token
- Internet connection for downloading models

## Installation
Install the required dependencies:
   ```
   pip install embedchain
   ```

Set up your Hugging Face access token:
   ```
   export HUGGINGFACE_ACCESS_TOKEN=your_access_token_here
   ```

## Configuration

```
config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  },
  'vectordb': {
    'provider': 'chroma',
    'config': {
        'collection_name': 'GitAI',
        'dir': './RAGQABot/chroma_db'
    }
  }
}
```

## Usage

```python
app.query("How to find difference between 2 git commits")
```

## Customization
- To use a different language model, modify the `model` under the `llm` configuration.
- To change the embedding model, update the `model` under the `embedder` configuration.
- To use a different vector database, change the `provider` and `config` under the `vectordb` configuration.

