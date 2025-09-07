import json

def train_test_split(dataset, test_size=0.1, seed=42):
    split = dataset.train_test_split(test_size=test_size, seed=seed)
    return split['train'], split['test']
