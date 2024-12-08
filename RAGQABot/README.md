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

```python
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

## Contributing

We welcome contributions to improve and expand the RAG QA Bot project. Here are some ways you can contribute:

### Areas for Contribution

1. Expanding the Git knowledge base
2. Improving answer quality
3. Performance optimization
4. Multi-language support

### Contributing Guidelines

1. Fork the repository and create a new branch for your feature or bug fix.
2. Follow the coding style and conventions used in the existing codebase.
3. Write clear, concise commit messages.
4. Add or update tests as necessary to cover your changes.
5. Update the documentation to reflect any changes in functionality or usage.
6. Submit a pull request with a clear description of your changes and their benefits.


### Reporting Issues

If you encounter any bugs or have suggestions for improvements:

1. Check if the issue already exists in the project's issue tracker.
2. If not, create a new issue with a clear title and description.
3. Include steps to reproduce the problem and any relevant error messages.

By contributing, you help make the RAG QA Bot more powerful, efficient, and user-friendly. Your efforts will benefit the entire Git community. Thank you for your support!