import json
import spacy 
import numpy as np
from sentence_transformers import SentenceTransformer, util

nlp = spacy.load("en_core_web_sm")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

sponsor_prototypes = [
    "this video is sponsored by",
    "thanks to our sponsor",
    "check out today's sponsor",
    "use my discount code",
    "brought to you by",
    "thanks to brand for supporting this video"
]

prototype_embeddings = embedder.encode(sponsor_prototypes, convert_to_tensor=True)

def remove_sponsor_sentences(text: str, threshold: float = 0.5) -> str:
    """Remove sentences too similar to sponsoring and ads """
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    cleaned_sentences = []
    for sent in sentences:
        sent_embedding = embedder.encode(sent, convert_to_tensor=True)

        cos_scores = util.cos_sim(sent_embedding, prototype_embeddings)
        max_score = float(cos_scores.max())

        if max_score < threshold:  
            cleaned_sentences.append(sent)

    return " ".join(cleaned_sentences)


def rem_ads_transcripts(intput_file = "data/clean_transcripts.json" , output_file = "data/ad_free_transcripts.json") :
  with open("data/clean_transcripts.json", "r" , encoding = "utf-8") as f :
    transcripts = json.load(f) 

    processed= []
    for entry in transcripts:
      transcript_text = entry.get("transcript" ,"")
      entry["transcript"] = remove_sponsor_sentences(transcript_text) 
      processed.append(entry)

    with open("data/ad_free_transcripts.json", "w" , encoding = "utf-8") as f :
      json.dump(processed, f, indent=2, ensure_ascii=False) 


if __name__ == "__main__":
    rem_ads_transcripts()
