import jsonlines
from sklearn.model_selection import train_test_split

# Input and output file paths
input_file = "data.jsonl"
train_file = "train.jsonl"
validation_file = "valid.jsonl"
test_file = "test.jsonl"

# Read the JSONL file into a list
with jsonlines.open(input_file, mode='r') as reader:
    data = [entry for entry in reader]

# Shuffle and split the data
train_data, temp_data = train_test_split(data, test_size=0.2, random_state=42)
validation_data, test_data = train_test_split(temp_data, test_size=0.5, random_state=42)

# Write the splits to their respective files
with jsonlines.open(train_file, mode='w') as writer:
    writer.write_all(train_data)

with jsonlines.open(validation_file, mode='w') as writer:
    writer.write_all(validation_data)

with jsonlines.open(test_file, mode='w') as writer:
    writer.write_all(test_data)

print(f"Train data saved to {train_file}")
print(f"Validation data saved to {validation_file}")
print(f"Test data saved to {test_file}")
