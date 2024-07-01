# GitHub Q&A Vector Search

This project implements a vector search system for GitHub-related questions and answers using LangChain, Sentence Transformers and Chroma.

## Overview

The system processes a JSON Lines file containing Git, GitHub and GitLab related Q&A pairs, embeds the questions using Hugging Face's sentence transformers, and stores them in a Chroma vector database. This allows for efficient similarity searches on GitHub-related queries.

## Features

- Loads Q&A pairs from a JSONL file
- Embeds questions using Hugging Face's `all-MiniLM-L6-v2` model
- Stores embeddings and metadata in a Chroma vector database
- Supports similarity search for relevant Q&A pairs

## Prerequisites

- Required libraries: `langchain_community`, `langchian_huggingface`, `chromadb`, `sentence_transformers`

