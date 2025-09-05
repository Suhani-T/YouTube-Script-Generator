import spacy
import json
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

classifier_model = "facebook/bart-large-mnli"
classifier = pipeline("zero-shot-classification", model=classifier_model)

labels = ["intro", "body", "outro"]


def segment_transcripts(input_file="data/ad_free_transcripts.json", output_file="data/segmented_transcripts.json"):

    with open( input_file, "r", encoding="utf-8") as f:
        transcripts = json.load(f)



    segmented_data = []

    for entry in transcripts:

        classified_sentences = {"intro": [], "body": [], "outro": []}

        transcript = entry["transcript"]
        doc = nlp(transcript)
        
        sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip()]
        
        for sentence in sentences:
            result = classifier(sentence, candidate_labels=labels)

            label = result["labels"][0] 
            classified_sentences[label].append(sentence)
        
        for key in classified_sentences:
            classified_sentences[key] = " ".join(classified_sentences[key])
        
        segmented_data.append({
            "title": entry["title"],
            "transcript_segments": classified_sentences
        })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(segmented_data, f, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    segment_transcripts()