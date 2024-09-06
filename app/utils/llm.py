from langchain_groq.chat_models import ChatGroq

llm=ChatGroq(model="llama3-groq-70b-8192-tool-use-preview", temperature=0.2)