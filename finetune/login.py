from google.colab import userdata
from huggingface_hub import login

hf_token = userdata.get('HF_TOKEN')
login(token=hf_token)
