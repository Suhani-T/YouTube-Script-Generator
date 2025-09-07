from dotenv import load_dotenv
import os
from huggingface_hub import login

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
login(token=hf_token)
