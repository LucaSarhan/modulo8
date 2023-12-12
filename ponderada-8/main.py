from stt import SpeechToTextNode
from tts import TTSNode
from llm import LLM


stt = SpeechToTextNode()
text = stt.listen_for_speech()

llm = LLM()
translated = llm.translator(text)

tts = TTSNode()
tts.text_to_speech(translated)
tts.play_audio()