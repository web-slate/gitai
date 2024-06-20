## Overview
This project extracts and processes content from a list of URLs, generating a JSONL file in a specific format. The extracted data is from Git Documentation, structured as chat messages for a virtual assistant. After generating the JSONL file, you will need to perform a train-test-validation split to prepare the data for fine-tuning a language model (LLM).

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `jsonlines`

You can install the required libraries using pip:
```bash
pip install requests beautifulsoup4 jsonlines
```


## Usage

1. **Prepare the List of URLs**:
   Modify the `urls` list to include the URLs you want to process.

2. **Run the Script**:
   Run the Python script to generate the JSONL file.
   ```bash
   python GitDocsScrapper.py
   ```

3. **Output**:
   The output will be saved to `data.jsonl` in the following format:
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

## Train-Test-Validation Split

After generating the `data.jsonl` file, you need to perform a train-test-validation split to prepare the data for fine-tuning a language model. This can be done using a Python script.



### Running the Split Script

To perform the split, run the following command:
```bash
python TrainTestValSplit.py
```

This will create three files: `train.jsonl`, `val.jsonl`, and `test.jsonl`, containing 80%, 10%, and 10% of the original data, respectively.

