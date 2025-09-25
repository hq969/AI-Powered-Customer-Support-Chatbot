from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class CustomerSupportAgent:
    def __init__(self, collection_name="customer_support"):
        self.embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.vectorstore = Chroma(collection_name=collection_name, embedding_function=self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model_name="gpt-4", temperature=0, openai_api_key=OPENAI_API_KEY),
            retriever=self.vectorstore.as_retriever()
        )

    def get_answer(self, question: str) -> str:
        return self.qa_chain.run(question)
