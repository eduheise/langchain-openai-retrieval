from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

# Custom imports
from documents import Documents


class LanguageModel:
    def __init__(self):
        load_dotenv()
        text_splitter = CharacterTextSplitter(
                separator=' ',  # by tokens
                chunk_size=100,  # how many words within a chunk
                chunk_overlap=20
                )

        documents = Documents()
        texts = text_splitter.split_text(
                documents.gather_documents())

        embeddings = OpenAIEmbeddings()
        retriever = FAISS.from_texts(texts, embeddings)\
                .as_retriever(search_type='similarity',
                                search_kwargs={'k': 5})

        self.retrieval_qa = RetrievalQA.from_chain_type(
                llm=OpenAI(),
                chain_type='stuff',
                retriever=retriever,
                return_source_documents=True)

    def ask(self, query):
        return self.retrieval_qa(query)


if __name__ == '__main__':
    model = LanguageModel()
    print(model.ask('What is ADADRIFT?'))
