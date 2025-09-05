from normalize import normalize_transcripts
from remove_ads import rem_ads_transcripts
from segmentation import segment_transcripts
from tokenizer import prepare_prompt_pairs, tokenize_prompt_transcripts

if __name__ == "__main__":
    normalize_transcripts()
    rem_ads_transcripts()
    segment_transcripts()
    prepare_prompt_pairs()
    tokenized = tokenize_prompt_transcripts()
    
