## Overview
This project extracts and processes content from a list of URLs, generating a JSONL file in a specific format. The extracted data includes sections of the webpage and their descriptions, structured as chat messages for a virtual assistant.

## Requirements
```bash
pip install requests beautifulsoup4 jsonlines
```

#### Key Steps:
- Extract the title from the first paragraph within the section.
- Extract specific sections with class `sect1`.
- For each section:
  - Extract the section text from `sectionbody` and `h2` tags.
  - If `dl` tags are present, process `dt` and `dd` pairs:
    - Gather all `dt` tags until encountering a `dd` tag.
    - Create structured messages for the virtual assistant.
- Return the extracted data as a list of JSONL entries.

#### Output
   The output will be saved to `GitDocs.jsonl` in the following format:
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




