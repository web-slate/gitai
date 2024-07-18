
# GitAI Data Preparation

This folder contains scripts to prepare and split data for training a LLM model. It combines Q&A data from Git documentation and Stack Overflow, then splits it into training, testing, and validation sets.


## Scripts

```python
python split.py
```

This script combines all JSONL files from the GitDocs and StackOverflow folders, then splits the data into training (80%), testing (10%), and validation (10%) sets.


## Data Format

The JSONL files should contain entries in the following format:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "<question>"
    },
    {
      "role": "assistant",
      "content": "<answer>"
    }
  ]
}
```

This format is suitable for fine-tuning language models.

