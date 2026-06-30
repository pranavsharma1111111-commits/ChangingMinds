import os
from dotenv import load_dotenv

from llm.llm_wrapper import LLMWrapper

load_dotenv("../.env")

api_key = os.getenv("GEMINI_API_KEY")

llm = LLMWrapper(api_key)

response = llm.generate("Say hello in one sentence.")

print(response)