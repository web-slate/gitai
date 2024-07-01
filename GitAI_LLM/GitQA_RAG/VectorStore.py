from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def metadata_func(record: dict, metadata: dict) -> dict:

    metadata["question"] = record.get('question')
    metadata["answer"] = record.get('answer')

    return metadata


loader = JSONLoader(
    file_path='GitHub_QA.jsonl',
    jq_schema='.',
    content_key='question',
    text_content=False,
    metadata_func=metadata_func,
    json_lines=True)

git = loader.load()


#checking format
# print(git[0])

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# save to disk
vectorstore = Chroma.from_documents(git, embedding_function, persist_directory="./chroma_db")

