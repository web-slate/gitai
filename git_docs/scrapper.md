
## Overview
This project extracts and processes content from a list of URLs, generating a JSONL file in a specific format. The extracted data includes sections of the webpage and their descriptions, structured as chat messages for a virtual assistant.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `jsonlines`

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4 jsonlines
```

## Script Description

The provided Python script performs the following steps:

1. **Fetch Content**: It fetches the HTML content from the specified URLs.
2. **Parse HTML**: It parses the HTML content to extract relevant sections and their descriptions.
3. **Generate JSONL**: It generates JSONL formatted entries for each section and writes them to an output file.

### Function `extract_content(url)`
This function takes a URL as input, fetches the webpage content, and processes it to extract the required information.

#### Key Steps:
- Fetch the webpage content using `requests`.
- Parse the HTML using `BeautifulSoup`.
- Extract the title from the first paragraph within the section.
- Extract specific sections with class `sect1`.
- For each section:
  - Extract the section text from `sectionbody` and `h2` tags.
  - If `dl` tags are present, process `dt` and `dd` pairs:
    - Gather all `dt` tags until encountering a `dd` tag.
    - Create structured messages for the virtual assistant.
- Return the extracted data as a list of JSONL entries.

### Main Script
- Define a list of URLs to process.
- Define the output file path.
- For each URL, call the `extract_content` function and write the output to the JSONL file.

## Usage

1. **Prepare the List of URLs**:
   Modify the `urls` list to include the URLs you want to process.

2. **Run the Script**:
   Run the Python script to generate the JSONL file.
   ```bash
   python git_docs_scrapper.py
   ```

3. **Output**:
   The output will be saved to `train.jsonl` in the following format:
   ```json
   {
     "messages": [
       {
         "role": "system",
         "content": "You are a helpful assistant."
       },
       {
         "role": "user",
         "content": "title dt_content"
       },
       {
         "role": "assistant",
         "content": "dd_content"
       }
     ]
   }
   ```




