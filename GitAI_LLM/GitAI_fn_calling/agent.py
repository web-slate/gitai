from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import json

# Initialize the embedding function
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Initialize Chroma vector store
vectorstore = Chroma(persist_directory="./GitAI_LLM/GitAI_fn_calling/chroma_db", embedding_function=embedding_function)

query = input(
'''
GitAI: How Can I help you?
Human: '''
)

# Perform similarity search
docs = vectorstore.similarity_search(query)

# retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
# docs = retriever.get_relevant_documents("How to clone a github repo")

print("\n")
# Iterate through each document and print structured information
for doc in docs:
    data = json.loads(doc.page_content)
    print(f"Command: {data['command']}")
    print(f"Description: {data['description']}")
    print("Parameters:")
    for param in data['parameters']:
        print(f" - {param['param']}: {param['param_description']}")
    # print(data) 
    print('='*50)


    