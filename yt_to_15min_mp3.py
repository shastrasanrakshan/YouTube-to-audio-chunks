import subprocess
import os
import math
import re
import sys

CHUNK_SECONDS = 15 * 60  # 15 minutes

def run(cmd):
    try:
        subprocess.run(cmd, check=True)
    except FileNotFoundError as e:
        print("Error: Required tool not found.")
        print("Make sure BOTH 'yt-dlp' and 'ffmpeg' are installed and available in PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Error: Command failed:")
        print(" ".join(cmd))
        sys.exit(1)

def sanitize_filename(name):
    # Remove only characters illegal in filesystems; keep Unicode
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'\s+', ' ', name)
    return name.strip()

def get_video_title(url):
    try:
        cmd = ["yt-dlp", "--print", "%(title)s", url]
        title = subprocess.check_output(cmd).decode("utf-8", errors="ignore").strip()
        return sanitize_filename(title)
    except FileNotFoundError:
        print("Error: yt-dlp not found. Install it using:")
        print("  python3 -m pip install yt-dlp  OR  brew install yt-dlp")
        sys.exit(1)

def download_audio(url, output_dir):
    output_template = os.path.join(output_dir, "full_audio.%(ext)s")
    cmd = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "-o", output_template,
        url
    ]
    run(cmd)
    return os.path.join(output_dir, "full_audio.mp3")

def get_audio_duration(filename):
    try:
        cmd = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            filename
        ]
        return float(subprocess.check_output(cmd).decode().strip())
    except FileNotFoundError:
        print("Error: ffprobe not found. Install ffmpeg:")
        print("  brew install ffmpeg")
        sys.exit(1)

def split_audio(input_file, output_dir):
    duration = get_audio_duration(input_file)
    chunks = math.ceil(duration / CHUNK_SECONDS)

    for i in range(chunks):
        start = i * CHUNK_SECONDS
        length = min(CHUNK_SECONDS, duration - start)

        output_file = os.path.join(
            output_dir,
            f"chunk_{i+1:02d}.mp3"
        )

        cmd = [
            "ffmpeg",
            "-y",
            "-ss", str(start),
            "-t", str(length),
            "-i", input_file,
            "-acodec", "copy",
            output_file
        ]
        run(cmd)
        print(f"Created {output_file}")

def main():
    url = input("Enter YouTube video URL: ").strip()

    if not url:
        print("Error: No URL provided.")
        sys.exit(1)

    print("Fetching video title...")
    title = get_video_title(url)

    output_dir = os.path.join(os.getcwd(), title)
    os.makedirs(output_dir, exist_ok=True)

    print(f"Output folder: {output_dir}")
    print("Downloading audio...")

    audio_file = download_audio(url, output_dir)

    print("Splitting into 15-minute chunks...")
    split_audio(audio_file, output_dir)

    print("Done!")

if __name__ == "__main__":
    main()
