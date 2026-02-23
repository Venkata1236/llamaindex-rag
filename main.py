from dotenv import load_dotenv
import os

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
print("API Key Loaded:", bool(openai_key))


from llama_index.core import SimpleDirectoryReader

Documents = SimpleDirectoryReader("Documents").load_data()
print(f"Loaded {len(Documents)} Documents.")

from llama_index.llms.openai import OpenAI
from llama_index.core import Settings

llm = OpenAI(temperature=0, model="gpt-3.5-turbo")
Settings.llm = llm


from llama_index.core import VectorStoreIndex

index = VectorStoreIndex.from_documents(Documents)

query_engine = index.as_query_engine()

response = query_engine.query("Summarize the key points from the documents.")
print("Response from LlamaIndex:")
print(response)