def tokenize_dataset(dataset, tokenizer, max_length=896):
    """concatenates prompt and script into a single input sequence , encodes the sequence"""
    def tokenize(example):

        tokens = tokenizer(
            example['prompt'],
            example['script'],
            truncation=True,
            padding="max_length",
            max_length=max_length
        )

        tokens["labels"] = tokens["input_ids"]
        return tokens
    
    return dataset.map(tokenize, batched=False)
