from TTS import TTSNode
from LLM import LLM

text = "Sua mãe"

llm = LLM()
translated = llm.translator(text)

tts = TTSNode()
tts.text_to_speech(translated)
tts.play_audio()