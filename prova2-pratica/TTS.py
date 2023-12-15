from gtts import gTTS
import os

class TTSNode:
    def __init__(self):
        self.message = None

    def text_to_speech(self, text, language='pt-br'):
        tts = gTTS(text, lang=language)
        audio_file = "speech.mp3"
        tts.save(audio_file)
        return audio_file

    def play_audio(self, audio_file="speech.mp3"):
        os.system(f"mpg321 {audio_file}")

def main():
    tts_node = TTSNode()
    tts_node.text_to_speech("Olá mundo!")  # Example usage of text_to_speech
    tts_node.play_audio("speech.mp3")  # Example usage of play_audio

if __name__ == "__main__":
    main()
