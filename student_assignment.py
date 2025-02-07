from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)
import re
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
    loader = PyPDFLoader(file_path=q2_pdf)
    docs = loader.load()
    text = ""
    for i in range(len(docs)):
        text += docs[i].page_content
        if i != len(docs)-1:
            text +='\n'
    text = re.sub(r'(\n[ ]*第[\s]*[一二三四五六七八九十\d]+[\s]*章[^\n]*\n)', r'\n\n\t\1', text)
    #print(text)
    text = re.sub(r'(\n[ ]*第[\s]*[一二三四五六七八九十\d-]+[\s]*條[^\n]*\n)', r'\n\n\t\1', text)
    print(text)
    text_splitter = RecursiveCharacterTextSplitter(separators=['\n\n\t'],
                                                   chunk_size=10,
                                                   chunk_overlap=0)
    #print(f'after text {text}')
    #print(docs[0])
    chunks = text_splitter.split_text(text)
    # text_splitter = CharacterTextSplitter(chunk_overlap=0)
    # chunks = text_splitter.split_text(docs)

    #for i, chunk in enumerate(chunks):  # 只显示前5个chunk的示例
    #    print(i)
    #    print(chunk)
    #    print('\n')
    return len(chunks)-1
