import re
import unicodedata
import json

def normalize_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text) #non-UTF chars
    
    text = re.sub(r"[\x00-\x1F\x7F-\x9F]", " ", text) # remove control chars
    
    text = re.sub(r"\s+", " ", text) #remove multiple spaces

    text = text.replace("\u00A0", " ").replace("\u200B", "") #replace weird spcaes with normal space 
    
    text = re.sub(r"[^\w\s.,!?']", "", text) # remove symbols, emoji
    
    return text.strip()

def normalize_transcripts(input_file="data/raw_transcripts.json", output_file="data/clean_transcripts.json"):
    with open(input_file, "r", encoding="utf-8") as f:
        transcripts = json.load(f)

    clean = []
    for entry in transcripts:
        normalized_transcript = normalize_text(entry["transcript"])
        clean.append({
            "title": entry["title"],
            "transcript": normalized_transcript
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(clean, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    normalize_transcripts()


