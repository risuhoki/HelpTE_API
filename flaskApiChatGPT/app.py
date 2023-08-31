from flask import Flask, jsonify, request, send_file
from config import config
import openai
import speech_recognition as sr
from gtts import gTTS

app = Flask(__name__)

@app.route('/audio_texto', methods=['POST'])
def audio_texto():
    file = request.files['audio']

    r = sr.Recognizer()

    with sr.AudioFile(file) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio, language='pt-BR')
        return jsonify({'content': text})
    except sr.UnknownValueError:
        return jsonify({'error':'não foi possível transcrever o áudio'})
    except sr.RequestError:
        return jsonify({'error':'não foi possível estabelecer conexão com o serviço de reconhecimento de fala'})

@app.route('/texto_audio', methods=['POST'])
def texto_audio():
    text = request.json['text']
    audio_file = gTTS(text, lang='pt-br')
    audio_file_path = 'audio.wav'
    audio_file.save(audio_file_path)
    return audio_file_path

@app.route('/tradutor', methods=['POST'])
def tradutor():
    openai.api_key = config['development'].OPENAI_KEY

    messages = []
    messages.append({"role": "system", "content": "Você é um assistente que retorna as emoções contidas no texto."})
    
    question = {}
    question['role'] = 'user'
    question['content'] = request.json['content']

    messages.append(question)

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)

    try:
        answer = response['choices'][0]['message']['content']
    except:
        answer = 'oops! deu ruim.'

    return answer


if __name__ == '__main__':
    app.run()