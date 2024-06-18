import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# Load the trained model
model = tf.keras.models.load_model('git_ai_model.keras')

# Load the tokenizers
with open('question_tokenizer.pkl', 'rb') as f:
    question_tokenizer = pickle.load(f)

with open('answer_tokenizer.pkl', 'rb') as f:
    answer_tokenizer = pickle.load(f)

def preprocess_text(text):
    return text.lower().strip()

def predict_answer(question):
    question = preprocess_text(question)
    sequence = question_tokenizer.texts_to_sequences([question])
    padded = pad_sequences(sequence, padding='post', maxlen=50)  # Adjust maxlen if needed
    prediction = model.predict(padded)
    predicted_index = np.argmax(prediction[0])
    
    if predicted_index in answer_tokenizer.index_word:
        predicted_word = answer_tokenizer.index_word[predicted_index]
    else:
        predicted_word = "unknown"  # Handle unknown predictions
    
    return predicted_word, predicted_index

# Example usage
if __name__ == "__main__":
    question = "What is Git?"
    answer, index = predict_answer(question)
    print(f"Question: {question}")
    print(f"Predicted Index: {index}")
    print(f"Answer: {answer}")
