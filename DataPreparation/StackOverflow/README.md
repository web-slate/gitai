# GitAI Q&A Data Preparation

This folder contains scripts to scrape and prepare Git-related Q&A data from Stack Overflow. The data can be used for training language models and building Q&A systems focused on Git, GitHub, and GitLab.

## Scripts

### 1. QALinks.py

This script extracts links to questions from Stack Overflow pages tagged with 'git', 'github', or 'gitlab'.

#### How it works:

1. Generates URLs for the first 300 pages of questions for a specific tag.
2. For each page, it extracts links to individual question pages.
3. Saves all extracted links to a JSON file.

#### Usage:

```python
python QALinks.py
```

Modify the `urls` list in the script to change the tag or number of pages to scrape.

#### Output:

- `links.json`: A JSON file containing all extracted question links.

### 2. QAScrapper.py

This script processes the links extracted by `QALinks.py`, scraping the content of each question and its accepted answer.

#### How it works:

1. Loads links from `links.json`.
2. For each link:
   - Extracts the question title, body, and accepted answer.
   - Creates a JSONL entry in a format suitable for fine-tuning language models.
3. Appends each entry to a JSONL file.

#### Usage:

```python
python QAScrapper.py
```

#### Output:

- `GitQA.jsonl`: A JSONL file containing the scraped Q&A data.

## Data Format

The output JSONL file contains entries in the following format:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "<question title>\n\n<question body>"
    },
    {
      "role": "assistant",
      "content": "<answer body>"
    }
  ]
}
```

## Features

- **Resumable Scraping**: The scraper keeps track of processed links, allowing you to resume scraping if interrupted.
- **Rate Limiting**: Includes a 1-second delay between requests to avoid overwhelming the server.
- **Error Handling**: Catches and reports errors for individual page processing without stopping the entire script.

## Requirements
```
pip install requests beautifulsoup4
```

## Customization
- To scrape different tags, modify the `urls` list in `QALinks.py`.
- To change the output file name or format, modify the relevant parts of `QAScrapper.py`.

