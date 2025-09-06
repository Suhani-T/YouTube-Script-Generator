import json
from datasets import Dataset

def format_prompt_script(input_file = "data/ad_free_transcripts.json" ) :
    
    """format data into prompt and script pairs for finetuning purpose"""

    with open(input_file, "r") as f:
        transcripts = json.load(f)

    formatted_pairs = []
    for entry in transcripts:
        summary = entry["summary"]
        transcript = entry["transcript"]

        prompt_text = f"Generate a YouTube video script about the following topic:\n{summary}"
        
        formatted_pairs.append({
            "prompt": prompt_text,
            "script": transcript
        })

    
    dataset = Dataset.from_list(formatted_pairs)
    return dataset


    # with open(output_file, "w") as f:
    #     json.dump(formatted_pairs, f, indent=2)


if __name__ == "__main__":
    format_prompt_script()