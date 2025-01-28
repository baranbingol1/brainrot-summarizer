from dotenv import load_dotenv, find_dotenv
import os
import tiktoken
from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

def load_env(): load_dotenv(find_dotenv(), override=True)

def load_document(file):
    _, ext = os.path.splitext(file)

    if ext == '.pdf':
        loader = PyPDFLoader(file)
        return loader.load()
    elif ext == '.docx':
        loader = Docx2txtLoader(file)
        return loader.load()
    elif ext == '.txt':
        loader = TextLoader(file, encoding='utf-8')
        return loader.load()
    else:
        raise ValueError(f'Unsupported file type: {ext}. The given document must be PDF, DOCX, or TXT.')
    
def get_token_count(model_name: str, text: str):
    enc = tiktoken.encoding_for_model(model_name)
    return len(enc.encode(text))