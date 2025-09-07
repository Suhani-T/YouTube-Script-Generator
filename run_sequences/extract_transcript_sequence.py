import json
from typing import List, Dict
from transcript_extraction.extract_urls import extract_youtube_urls_from_file
from transcript_extraction.extract_transcript import get_video_transcript



def process_youtube_urls_to_json(input_file: str, output_file: str = 'youtube_data.json') -> List[Dict]:
    urls = extract_youtube_urls_from_file(input_file)
    if not urls:
        return []

    data = []
    for _, url in enumerate(urls, 1):
        video_data = get_video_transcript(url)
        if not video_data['success']:
            continue
        entry = {
            "summary": video_data['summary'],
            "transcript": video_data['transcript']
        }
        data.append(entry)

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception:
        pass
    return data

def validate_json_output(json_file: str):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        required_fields = ['summary', 'transcript']

        for entry in data:
            missing_fields = [field for field in required_fields if field not in entry]
            if missing_fields:
                return False
            
        return True
    
    except Exception:
        return False

if __name__ == "__main__":
    INPUT_FILE = "data/urls.txt"
    OUTPUT_FILE = "data/raw_transcripts.json"
    processed_data = process_youtube_urls_to_json(INPUT_FILE, OUTPUT_FILE)
    if processed_data:
        validate_json_output(OUTPUT_FILE)
