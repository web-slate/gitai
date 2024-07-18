import os
import json
import random
from pathlib import Path

def load_jsonl(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f]

def save_jsonl(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')

def combine_and_split_data():
    # Define paths using absolute paths
    script_dir = Path(__file__).resolve().parent
    base_path = script_dir.parent.parent  # Assuming script is in gitai/DataPreparation/DataSplit
    data_prep_path = base_path / 'DataPreparation'
    output_path = base_path / 'data'

    # Create output directory and any missing parent directories
    output_path.mkdir(parents=True, exist_ok=True)

    # Collect all JSONL files
    jsonl_files = []
    for folder in ['GitDocs', 'StackOverflow']:
        folder_path = data_prep_path / folder
        jsonl_files.extend(folder_path.glob('*.jsonl'))

    # Combine all data
    all_data = []
    for file in jsonl_files:
        all_data.extend(load_jsonl(file))

    # Shuffle the data
    random.shuffle(all_data)

    # Calculate split sizes
    total = len(all_data)
    train_size = int(0.8 * total)
    test_size = int(0.1 * total)

    # Split the data
    train_data = all_data[:train_size]
    test_data = all_data[train_size:train_size+test_size]
    valid_data = all_data[train_size+test_size:]

    # Save the split data
    save_jsonl(train_data, output_path / 'train.jsonl')
    save_jsonl(test_data, output_path / 'test.jsonl')
    save_jsonl(valid_data, output_path / 'valid.jsonl')

    print(f"Data split and saved in {output_path}:")
    print(f"Train: {len(train_data)} samples")
    print(f"Test: {len(test_data)} samples")
    print(f"Validation: {len(valid_data)} samples")

if __name__ == "__main__":
    combine_and_split_data()