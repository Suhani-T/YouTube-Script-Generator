import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import os

load_dotenv()
gemini_key = os.getenv("GEMINI_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=gemini_key,
    temperature=0
)

def summarize_transcript(transcript_text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=8000,
        chunk_overlap=500,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = text_splitter.split_text(transcript_text)
    docs = [Document(page_content=chunk) for chunk in chunks]
    summarize_chain = load_summarize_chain(
        llm,
        chain_type="map_reduce",
    )
    summary = summarize_chain.run(docs)
    return summary
