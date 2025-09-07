import re
from typing import List

def extract_youtube_urls_from_file(file_path: str) -> List[str]:
    youtube_url_pattern = r'(?:https?://)(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    urls = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(youtube_url_pattern, content)
            for match in matches:
                url = f"https://www.youtube.com/watch?v={match}"
                urls.append(url)

    except FileNotFoundError:
        return []
    return urls
