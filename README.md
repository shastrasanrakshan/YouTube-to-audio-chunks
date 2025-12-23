# YouTube → 15-Minute MP3 Chunker

**Dependency Setup & Usage Guide**

This project downloads audio from a YouTube video and splits it into **15-minute MP3 chunks**, saving them inside a folder named after the video title.

---

## 1. System Requirements

* Python **3.8+**
* Internet connection
* Terminal access

Check Python:

```bash
python3 --version
```

If Python is not installed, install it from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## 2. Install Homebrew (macOS only)

Homebrew is the easiest way to install system tools like `ffmpeg`.

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After installation, restart Terminal or run:

```bash
source ~/.zshrc
```

Verify:

```bash
brew --version
```

---

## 3. Install ffmpeg (REQUIRED)

`ffmpeg` provides:

* MP3 conversion
* Audio duration detection (`ffprobe`)
* Chunk splitting

Install:

```bash
brew install ffmpeg
```

Verify **both** commands work:

```bash
ffmpeg -version
ffprobe -version
```

If either fails → the script will NOT work.

---

## 4. Install yt-dlp (REQUIRED)

`yt-dlp` downloads audio from YouTube.

### Recommended (Python-based install)

```bash
python3 -m pip install --upgrade yt-dlp
```

Verify:

```bash
yt-dlp --version
```

If `yt-dlp` is **not found**, add pip’s bin directory to PATH:

```bash
echo 'export PATH="$HOME/Library/Python/3.9/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

(Adjust `3.9` if your Python version differs.)

---

## 5. Verify All Dependencies (IMPORTANT)

Run **all** of these successfully:

```bash
python3 --version
yt-dlp --version
ffmpeg -version
ffprobe -version
```

If **any one fails**, fix it before proceeding.

---

## 6. Script File Setup

1. Save the script as:

```
yt_to_15min_mp3.py
```

2. Place it in any directory (e.g. Desktop).

3. No configuration needed inside the script.

---

## 7. Run the Script

From the directory containing the script:

```bash
python yt_to_15min_mp3.py
```

The script will immediately prompt:

```
Enter YouTube video URL:
```

Paste the YouTube URL and press **Enter**.

---

## 8. Output Structure

For a 32-minute video titled:

```
System Design Interview
```

Output will be:

```
System Design Interview/
├── full_audio.mp3
├── chunk_01.mp3   (0–15 min)
├── chunk_02.mp3   (15–30 min)
└── chunk_03.mp3   (30–32 min)
```

* Folder name = **video title**
* Chunk duration = **exactly 15 minutes**
* Last chunk may be shorter
* Unicode titles (Hindi, etc.) are fully supported

---

## 9. Common Errors & Fixes

### ❌ `yt-dlp not found`

Fix:

```bash
python3 -m pip install yt-dlp
```

or

```bash
brew install yt-dlp
```

---

### ❌ `ffmpeg / ffprobe not found`

Fix:

```bash
brew install ffmpeg
```

---

### ❌ Permission errors

Run:

```bash
chmod +x yt_to_15min_mp3.py
```

---

## 10. Notes on YouTube Live Videos

* Past live streams are supported
* Very long videos may take time to download
* Chunking is **fast** because audio is not re-encoded

---

## 11. Linux Notes (Quick)

```bash
sudo apt update
sudo apt install ffmpeg python3-pip
pip3 install yt-dlp
```

---

## 12. Windows Notes (Quick)

1. Install Python from python.org
2. Install ffmpeg from [https://ffmpeg.org](https://ffmpeg.org)

   * Add `ffmpeg/bin` to PATH
3. Install yt-dlp:

```powershell
pip install yt-dlp
```

---

## 13. Final Checklist ✅

* [ ] Python installed
* [ ] yt-dlp installed & in PATH
* [ ] ffmpeg + ffprobe installed & in PATH
* [ ] Script saved correctly

If all are checked, **the script will work reliably**.
