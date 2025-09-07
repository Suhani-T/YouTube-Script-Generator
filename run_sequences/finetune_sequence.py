from finetune.login import *
from finetune.get_tokenizer import get_tokenizer
from finetune.get_dataset import train_test_split
from finetune.chunking import chunk_dataset
from finetune.tokenization import tokenize_dataset
from finetune.finetune_model import finetune_lora
from data_prep.prepare_pairs import format_prompt_script



if __name__ == "__main__":
    dataset = format_prompt_script()

    tokenizer = get_tokenizer()

    train_dataset, test_dataset = train_test_split(dataset)

    train_dataset = chunk_dataset(train_dataset, tokenizer)
    test_dataset = chunk_dataset(test_dataset, tokenizer)

    tokenized_train = tokenize_dataset(train_dataset, tokenizer)
    tokenized_test = tokenize_dataset(test_dataset, tokenizer)

    model, trainer = finetune_lora(tokenized_train, tokenized_test, tokenizer)
