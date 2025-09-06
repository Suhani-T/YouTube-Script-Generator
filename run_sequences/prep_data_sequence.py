from data_prep.normalize import normalize_transcripts
from data_prep.remove_ads import rem_ads_transcripts
from data_prep.prepare_pairs import format_prompt_script
# from tokenizer import 

if __name__ == "__main__":
    normalize_transcripts()
    rem_ads_transcripts()
    dataset =format_prompt_script()
