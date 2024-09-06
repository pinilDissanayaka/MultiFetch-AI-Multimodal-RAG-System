output_path = "./temp"

import os
import uuid
import requests
import base64
from PIL import Image
from unstructured.partition.pdf import partition_pdf
from langchain_core.documents import Document
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_groq.chat_models import ChatGroq
from langchain_google_vertexai import ChatVertexAI
from langchain.embeddings import VertexAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema.document import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.messages import HumanMessage
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from google.colab import userdata



def extract_from_pdf(file_path:str):
    raw_pdf_elements = partition_pdf(
        filename=file_path,
        extract_images_in_pdf=True,
        infer_table_structure=True,
        chunking_strategy="by_title",
        max_characters=4000,
        new_after_n_chars=3800,
        combine_text_under_n_chars=2000,
        extract_image_block_output_dir=output_path,
    )
    
    return raw_pdf_elements


    
