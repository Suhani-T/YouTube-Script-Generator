import json
from datasets import Dataset

def load_dataset(file_path="ad_free_transcripts.json"):

    with open(file_path) as f:

        dataset = Dataset.from_list([
            {"prompt": f"Generate a YouTube video script about: {d['summary']}", "script": d['transcript']}
            for d in json.load(f)
        ])
        
    return dataset

def train_test_split(dataset, test_size=0.1, seed=42):
    split = dataset.train_test_split(test_size=test_size, seed=seed)
    return split['train'], split['test']
