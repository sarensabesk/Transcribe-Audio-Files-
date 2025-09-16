import whisper
import sys

# Load Whisper model
model = whisper.load_model("base")

# Get filename from command line
if len(sys.argv) < 2:
    print("Usage: python transcribe.py <audiofile>")
    sys.exit(1)

audio_file = sys.argv[1]
result = model.transcribe(audio_file)

# Save transcription
with open("transcription.txt", "w") as f:
    f.write(result["text"])

print("✅ Transcription saved to transcription.txt")
