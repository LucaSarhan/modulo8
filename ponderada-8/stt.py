import speech_recognition as sr

class SpeechToTextNode():
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen_for_speech(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            text = self.recognizer.recognize_google(audio, language='pt-br')
            print("You said:", text)
            return text

def main(args=None):
    speech_to_text_node = SpeechToTextNode()
    speech_to_text_node.listen_for_speech()

if __name__ == "__main__":
    main()
