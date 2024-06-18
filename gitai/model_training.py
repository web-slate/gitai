import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import os
import pickle

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'data.csv')

# Load data
data = pd.read_csv(data_path)

# Debug: Print the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Debug: Print shapes of train and test data
print(f"Train data shape: {train_data.shape}")
print(f"Test data shape: {test_data.shape}")

# Preprocess text data
def preprocess_text(text):
    return text.lower().strip()

train_data['question'] = train_data['question'].apply(preprocess_text)
train_data['answer'] = train_data['answer'].apply(preprocess_text)
test_data['question'] = test_data['question'].apply(preprocess_text)
test_data['answer'] = test_data['answer'].apply(preprocess_text)

# Tokenize the text
question_tokenizer = tf.keras.preprocessing.text.Tokenizer()
question_tokenizer.fit_on_texts(train_data['question'])

answer_tokenizer = tf.keras.preprocessing.text.Tokenizer()
answer_tokenizer.fit_on_texts(train_data['answer'])

# Convert text to sequences
train_sequences = question_tokenizer.texts_to_sequences(train_data['question'])
train_padded = tf.keras.preprocessing.sequence.pad_sequences(train_sequences, padding='post')

train_labels_sequences = answer_tokenizer.texts_to_sequences(train_data['answer'])
train_labels_padded = tf.keras.preprocessing.sequence.pad_sequences(train_labels_sequences, padding='post')

# Ensure labels are one-dimensional
train_labels = train_labels_padded[:, 0]  # Use only the first token as the label

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(question_tokenizer.word_index) + 1, output_dim=64),
    tf.keras.layers.LSTM(128, return_sequences=True),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),  # Added dropout to prevent overfitting
    tf.keras.layers.Dense(len(answer_tokenizer.word_index) + 1, activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(train_padded, train_labels, epochs=20, validation_split=0.2)  # Increased epochs to 20

# Save the model
model.save('git_ai_model.keras')

# Save the tokenizers
with open('question_tokenizer.pkl', 'wb') as f:
    pickle.dump(question_tokenizer, f)

with open('answer_tokenizer.pkl', 'wb') as f:
    pickle.dump(answer_tokenizer, f)

# Load and preprocess test data
test_sequences = question_tokenizer.texts_to_sequences(test_data['question'])
test_padded = tf.keras.preprocessing.sequence.pad_sequences(test_sequences, padding='post')

test_labels_sequences = answer_tokenizer.texts_to_sequences(test_data['answer'])
test_labels_padded = tf.keras.preprocessing.sequence.pad_sequences(test_labels_sequences, padding='post')

# Debug: Print shapes and contents of test labels
print(f"Test labels shape: {test_labels_padded.shape}")
print(f"Test labels preview: {test_labels_padded}")

# Ensure test labels are one-dimensional
if test_labels_padded.shape[1] > 0:
    test_labels = test_labels_padded[:, 0]  # Use only the first token as the label
else:
    test_labels = []

# Evaluate the model
if len(test_labels) > 0:
    loss, accuracy = model.evaluate(test_padded, test_labels)
    print(f'Test Accuracy: {accuracy}')
else:
    print("Test labels are empty. Evaluation skipped.")
