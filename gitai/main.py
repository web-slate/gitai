import pandas as pd
import os
import click

# Load the data for key-value retrieval
script_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_dir, 'data.csv')
data = pd.read_csv(data_path)

def preprocess_text(text):
    return text.lower().strip()

@click.command()
@click.argument('question')
def main(question):
    question = preprocess_text(question)
    
    # Key-value retrieval
    data['question'] = data['question'].apply(preprocess_text)
    if question in data['question'].values:
        answer = data[data['question'] == question]['answer'].values[0]
        print(f"Question: {question}")
        print(f"Answer: {answer}")
    else:
        print(f"Question: {question}")
        print("Answer: No matching answer found.")

if __name__ == "__main__":
    main()
