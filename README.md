# GitAI

GitAI is a project aimed at assisting developers in learning and using Git commands effectively. This README provides an in-depth look at the various approaches we've explored and their technical implementations.


### 1. Fine-tuned LLMs 
**[Hugging Face Link](https://huggingface.co/collections/YashJain/gitai-66716f5414a2d8e2b6d93bd9)**

We fine-tuned two smaller language models to run locally:

- **Qwen2 0.5B**
- **Gemma 2B**

**Training Data:**
- Git documentation
- Stack Overflow Q&A tagged with git, github, and gitlab

**Fine-tuning Process:**
- Used LORA (Low-Rank Adaptation) technique for fine-tuning
- Preprocessed the training data to create input-output pairs
- Fine-tuned the models on a MacBook Air M2 (16GB) with MLX-LM

**Inference:**
- Models can be run locally on CPU or GPU
- Input: Natural language query about Git
- Output: Relevant Git command or explanation

### 2. AI Agent 

**Technologies Used:**
- LangChain Agents
- ShellTool for executing terminal commands
- OpenAI GPT-3.5 as the language model

**How it works:**
1. User inputs a natural language request
2. LangChain Agent processes the input using GPT-3.5
3. Agent determines the appropriate Git command
4. ShellTool executes the command in the terminal

**Error Handling:**
- Uses language model as a reasoning engine to determine which actions to take and in which order
- Agent can interpret error messages and take actions on its own

### 3. Commonly Used Commands Retrieval

**Data Structure:**
- JSONLine file containing common Git commands, their descriptions, parameters, and syntax

**Retrieval Process:**
1. User input is converted into an embedding using SentenceTransformers
2. Chroma vector store performs cosine similarity search
3. Top K most similar commands are retrieved

**Technologies Used:**
- LangChain 
- Chroma as the vector store
- SentenceTransformers for embedding 

### 4. RAG QA Bot

**Knowledge Base:**
- Git documentation
- Stack Overflow Q&A tagged with git, github, and gitlab

**Technologies Used:**
- EmbedChain for RAG
- Mistral 7B as LLM (Hugging Face Inference)
- Chroma as the vector store
- SentenceTransformers for embedding

**How it works:**
1. Knowledge base is chunked and embedded
2. User question is embedded using the same model
3. Searches in Vector store for relevant chunks
4. Retrieved chunks are used to construct a prompt
5. Language model generates an answer based on the prompt

## Conclusion

After thorough testing and evaluation:

1. The **Commonly Used Commands Retrieval** system proved to be the most efficient for quick, local operations. Its speed and accuracy make it ideal for beginners who want to learn Git.

2. The **AI Agent** approach, while requiring an internet connection and OpenAI API, offers the most flexible and comprehensive solution, capable of handling complex queries and exectuing them on it's own.

<!-- ## Getting Started

(Add installation and usage instructions here)

## Contributing

(Provide guidelines for contributors)

## License

(Specify the license for your project) -->