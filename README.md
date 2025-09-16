# 🎙️ Audio Transcriber  

A simple but powerful **speech-to-text tool** built with [OpenAI Whisper](https://github.com/openai/whisper).  
This project takes an **audio or video file** and automatically generates a **clean text transcription** — making it easy to analyze interviews, podcasts, lectures, or meeting recordings.  

---

## ✨ Features  
- 🎧 Supports multiple formats: `.mp3`, `.wav`, `.m4a`, `.ogg`, `.flac`, `.mp4`  
- ⚡ Uses OpenAI’s **Whisper** deep learning model for accurate transcription  
- 📄 Automatically saves results into a `.txt` file  
- 🖥️ Easy to run inside any VS Code project (via WSL or virtual environments)  
- 🔄 Flexible: transcribe a single file, or extend it to handle whole folders  

---

## 🎯 Project Purpose  
The goal of this project was to explore **state-of-the-art speech recognition** and build a lightweight, developer-friendly tool that can turn audio into text with just one command.  
While simple in design, it demonstrates how cutting-edge AI models like Whisper can be integrated into real-world workflows with minimal code.  

---

## ⚙️ Setup  

### 1️⃣ Clone the repo  
git clone https://github.com/your-username/whisper-transcriber.git
cd whisper-transcriber

### 2️⃣ Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

## ▶️ Usage
🎵 Transcribe a single file
python transcribe.py video_sound.mp3

### 📄 Example Output
Input: video_sound.mp3
Output: transcription.txt (contains the full transcript)

### 🔍 How It Works
- Loads the Whisper model (base by default).
- Accepts an audio or video file as input.
- Runs transcription locally (no need for internet after install).
- Saves the result in a .txt file for easy access.

## 🚀 Future Improvements
- 📂 Batch transcriptions for entire folders
- 📝 Export in .srt (subtitles) or .json formats
- 🔧 Support for different Whisper model sizes (small, medium, large)

## 🙌 What I Did
- Built a Python script around OpenAI’s Whisper library
- Integrated it into a VS Code project with a clean virtual environment setup
- Tested it on multiple file types to ensure compatibility
- Packaged the dependencies so anyone can download and use it easily