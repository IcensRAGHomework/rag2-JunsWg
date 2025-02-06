from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(file_path=q1_pdf)
    docs = loader.load()
    #text_splitter = CharacterTextSplitter(chunk_overlap=0)
    #chunks = text_splitter.split_text(docs)
    return docs[-1]
    #pprint(docs[0])
    #pass

def hw02_2(q2_pdf):
    pass
