from flask import Flask, request, render_template
import whisper
import pydub

app = Flask(__name__)

def transcribe(audio_file):
    audio = pydub.AudioSegment.from_file(audio_file)
    audio.export("audio.wav", format="wav")
    model = whisper.load_model("base")
    result = model.transcribe("audio.wav")
    return result["text"]

def save_transcription(text):
    with open("transcription.txt", "w") as file:
        file.write(text)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        audio_file = request.files['audio']
        text = transcribe(audio_file)
        save_transcription(text)
        return render_template('A_t_T.html', text=text)
    return render_template('A_t_T.html')

if __name__ == "__main__":
    app.run(debug=True)