from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
import tempfile

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")
text_splitter = CharacterTextSplitter()


def summarize_pdf(text: str) -> str:
    texts = text_splitter.split_text(text)
    docs = [Document(page_content=t) for t in texts]
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.run(docs)

    return summary


def summarize_pdf_gradio(gradio_file: tempfile._TemporaryFileWrapper):
    import requests

    url = "http://0.0.0.0:8000/summarize"

    payload = {}
    files = [
        ('file', ('temp.pdf',
                  open(gradio_file.name, 'rb'), 'application/pdf'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return response.json()["summary"]