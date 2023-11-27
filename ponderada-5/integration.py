import gradio as gr
from langchain.llms import Ollama
import requests

conversation_history = ["Answer prompts like you are a safety expert for industrial environments"]

def obter_texto_do_link(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        texto = response.text
        return texto
    except requests.exceptions.RequestException as e:
        return f"Erro ao obter conteúdo do link: {e}"

def generate_response(prompt, link_context):
    contexto = obter_texto_do_link(link_context)
    if "Erro" in contexto:
        return contexto

    conversation_history.append(prompt)
    full_prompt = "\n".join(conversation_history)
    
    opa = Ollama(base_url='http://localhost:11434', model="llama2")
    resposta = opa(full_prompt)
    
    return resposta

def main():
    iface = gr.Interface(
        fn=generate_response,
        inputs=[gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
                gr.Textbox(placeholder="Enter the link for context")],
        outputs="text"
    )
    iface.launch()
    
if __name__ == "__main__":
    main()
