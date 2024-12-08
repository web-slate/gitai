import os
# Replace this with your HF token
os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "hf_xxx"

from embedchain import App

config = {
  'llm': {
    'provider': 'huggingface',
    'config': {
      'model': 'mistralai/Mistral-7B-Instruct-v0.2',
      'top_p': 0.5
    }
  },
  'embedder': {
    'provider': 'huggingface',
    'config': {
      'model': 'sentence-transformers/all-mpnet-base-v2'
    }
  },
  'vectordb': {
    'provider': 'chroma',
    'config': {
        'collection_name': 'GitAI',
        'dir': './RAGQABot/chroma_db'
    }}
}


app = App.from_config(config=config)
app.add("./RAGQABot/CombinedQA.jsonl")
response = app.query("git rebase vs git merge along with example commands")

print(response)


