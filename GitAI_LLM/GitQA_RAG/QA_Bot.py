# from langchain_community.vectorstores import Chroma
# from langchain_huggingface import HuggingFaceEmbeddings

# embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# # load from disk
# vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)

# docs = vectorstore.similarity_search("How to share a private repo")

# # retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
# # docs = retriever.get_relevant_documents("How to clone a github repo")

# for i in range(len(docs)):
#   print(docs[i].metadata['question'])
#   # print(docs[i])
#   print('='*50)



import gradio as gr
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embedding function and vector store
embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)

def search_documents(query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
    docs = retriever.get_relevant_documents(query)
    
    return set([doc.page_content.splitlines()[0] for doc in docs]), docs

def show_qa_pair(doc):
    return doc.metadata['question'], doc.metadata['answer']

def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# Git ChatBot")
        
        with gr.Row():
            query_input = gr.Textbox(label="Search Query")
            search_button = gr.Button("Search")
        
        with gr.Row():
            doc_list = gr.Radio(label="Related Documents", interactive=True)
        
        with gr.Row():
            question_box = gr.Textbox(label="Question", lines=3, interactive=False, visible=False)
            answer_box = gr.Textbox(label="Answer", lines=5, interactive=False, visible=False)
        
        docs = gr.State([])
        
        def update_doc_list(query):
            doc_titles, all_docs = search_documents(query)
            docs.value = all_docs
            return (
                gr.Radio(choices=doc_titles, value=None),
                gr.Textbox(visible=False),
                gr.Textbox(visible=False)
            )
        
        def update_qa(choice):
            if choice is None:
                return (
                    gr.Textbox(visible=False),
                    gr.Textbox(visible=False)
                )
            selected_doc = next(doc for doc in docs.value if doc.page_content.splitlines()[0] == choice)
            question, answer = show_qa_pair(selected_doc)
            return (
                gr.Textbox(value=question, visible=True),
                gr.Textbox(value=answer, visible=True)
            )
        
        search_button.click(update_doc_list, inputs=query_input, outputs=[doc_list, question_box, answer_box])
        doc_list.change(update_qa, inputs=doc_list, outputs=[question_box, answer_box])
    
    return demo

# Launch the Gradio interface
if __name__ == "__main__":
    ui = create_ui()
    ui.launch(debug=True)