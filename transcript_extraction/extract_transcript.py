import re
from youtube_transcript_api import YouTubeTranscriptApi
from .summary import summarize_transcript


def extract_yt_id(url: str) -> str:
    video_id_pattern = r'(?:v=|/)([a-zA-Z0-9_-]{11})'
    match = re.search(video_id_pattern, url)
    if match:
        video_id = match.group(1)
    else:
        video_id = None
    return video_id

def get_transcript(url: str) -> str:
    video_id = extract_yt_id(url)

    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id)

    texts = [i.text for i in transcript.snippets]
    concatenated_string = ''.join(texts)

    return concatenated_string
    
def get_video_transcript(url: str) -> dict:
    try:
        transcript = get_transcript(url)
        summary = summarize_transcript(transcript)

        return {
            "summary": summary,
            "transcript": transcript,
            "success": True
        }
    except Exception as e:
        print(f"Error for URL {url}: {e}")
        return {"success": False, "error": str(e)}
