from langchain_community.document_loaders import JSONLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


loader = JSONLoader(
    file_path='GitAI_LLM/GitAI_fn_calling/GitAI_functions.json',
    jq_schema='.[]',
    # content_key='description',
    text_content=False,
    # metadata_func=metadata_func
    )

git = loader.load()


#checking format
# print(git[7])

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # save to disk
vectorstore = Chroma.from_documents(git, embedding_function, persist_directory="./GitAI_LLM/GitAI_fn_calling/chroma_db")