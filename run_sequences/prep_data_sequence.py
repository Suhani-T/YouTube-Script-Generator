from data_prep.normalize import normalize_transcripts
from data_prep.remove_ads import rem_ads_transcripts

if __name__ == "__main__":
    normalize_transcripts()
    rem_ads_transcripts()
