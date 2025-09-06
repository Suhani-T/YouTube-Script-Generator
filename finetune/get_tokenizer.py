from transformers import AutoTokenizer

def get_tokenizer(model_name="google/gemma-2b-it"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token
    return tokenizer
