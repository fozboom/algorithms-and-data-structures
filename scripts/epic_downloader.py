import os
import re
import subprocess
from urllib.parse import parse_qs, urlparse

INPUT_FILE = '/Users/fozboom/Documents/Algorithms-and-Data-Structures/scripts/videos_to_download.txt'
OUTPUT_DIR = 'GEN_AI__Videos'

def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename).strip()


def download_video(iframe_url, title, index, total_count, output_dir):
    try:
        parsed_url = urlparse(iframe_url)
        query_params = parse_qs(parsed_url.query)
        
        video_id = query_params.get('video', [None])[0]
        resolution = query_params.get('resolution', ['1920x1080'])[0]

        if not video_id:
            print(f"Unable to find video ID in URL: {iframe_url}")
            return

        download_url = f"https://storagebud.videoportal.epam.com/video/iframe/file/{video_id}/mp4/{resolution}/play-by-vp"
        
        safe_title = sanitize_filename(title)
        output_filename = f"{safe_title}.mp4"
        output_path = os.path.join(output_dir, output_filename)

        print(f"\n[{index}/{total_count}] Downloading video: {safe_title}")

        command = [
            'yt-dlp',
            '--quiet',
            '--no-warnings',
            '--progress',
            '-o', output_path,
            download_url
        ]
        
        subprocess.run(command, check=True)
        
        print(f"Video successfully saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred while downloading video '{title}': {e}")


def main():
    print(f"Starting work. Reading file: {INPUT_FILE}")

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILE}' not found. Please create and fill it.")
        return
        
    if not lines:
        print("File is empty. Nothing to download.")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    total_videos = len(lines)
    print(f"Found {total_videos} videos to download.")
    
    for i, line in enumerate(lines, 1):
        parts = line.split(';', 1)
        if len(parts) != 2:
            print(f"Skipping line {i}, because it has an invalid format: {line}")
            continue
        
        iframe_url, title = parts
        download_video(iframe_url.strip(), title.strip(), i, total_videos, OUTPUT_DIR)

    print("\nWork completed!")


if __name__ == "__main__":
    main()