from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

class LLM():
    def __init__(self):
        self.hello = "Hello, this is a test."

    def translator(self, text):
        load_dotenv()
        self.model = ChatOpenAI(model="gpt-3.5-turbo")

        self.prompt = ChatPromptTemplate.from_template(
        """Translate the following text to {language}:

        text: {text}
        """)

        self.chain = self.prompt | self.model

        self.response = ""

        for s in self.chain.stream({"text": text, "language": "en"}):
            self.response += str(s.content)  # Convert AIMessageChunk to str

        print(self.response)
        
        return self.response

if __name__ == "__main__":
    llm = LLM()
    llm.translator("Your text goes here")  # Provide the text you want to translate
    print(llm.response)
