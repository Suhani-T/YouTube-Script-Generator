def chunk_text(text, tokenizer, max_tokens=640, stride=150):

    """ chunk the text so that each chunk fits the model token limit"""

    tokens = tokenizer.encode(text)
    chunks = []
    start = 0

    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunks.append(tokenizer.decode(tokens[start:end], skip_special_tokens=True))

        if end == len(tokens):
            break

        start += max_tokens - stride

    return chunks


def chunk_dataset(dataset, tokenizer):
    """prepare collection of chunks"""

    chunked = []
    
    for item in dataset.to_list():
        prompt = item['prompt']
        
        for chunk in chunk_text(item['script'], tokenizer):
            chunked.append({"prompt": prompt, "script": chunk})

    from datasets import Dataset
    return Dataset.from_list(chunked)
