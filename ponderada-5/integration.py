import gradio as gr
from langchain.llms import Ollama
import PyPDF2
import logging
import io
import fitz
from pdfminer.high_level import extract_text

conversation_history = []

def ler_pdf(arquivo_pdf):
    try:
        # Check if arquivo_pdf is already in bytes format
        if isinstance(arquivo_pdf, bytes):
            bytes_data = arquivo_pdf
        else:
            # If it's not in bytes format, assume it's a string and encode it to bytes
            bytes_data = arquivo_pdf.encode('utf-8')

        texto = extract_text(io.BytesIO(bytes_data))
        return texto
    except Exception as e:
        logging.error(f"Erro ao ler PDF: {e}")
        return "Erro ao processar o arquivo PDF."


def preparar_prompt(pergunta, contexto=''):
    prompt = f"""
    Pergunta do usuário: '{pergunta}'
    Contexto: {contexto} Responda primeiro com uma breve explicação, seguida de bullet points que destaquem os principais aspectos ou recomendações relacionadas à pergunta. As respostas devem ser informativas e refletir as melhores práticas e regulamentações do setor industrial.
    """
    return prompt

def generate_response(pergunta, arquivo_pdf=None):
    if arquivo_pdf is not None:
        contexto = ler_pdf(arquivo_pdf)
        logging.info(f"PDF carregado para contextualização.")
    else:
        contexto = ""
        
    # Append the user's prompt to the conversation history
    conversation_history.append(pergunta)

    opa = Ollama(base_url='http://localhost:11434', model="llama2")
    resposta = ""
    for chunk in opa.stream(preparar_prompt(pergunta, contexto)):
        resposta += chunk
    logging.info(f"Pergunta: {pergunta} | Resposta: {resposta[:50]}...")
    
    # conversation_history.append(prompt)  # Commented out as it might not be needed
    full_prompt = "\n".join(conversation_history)
    return opa(full_prompt)

def main():
    iface = gr.Interface(
        fn=generate_response,
        inputs=[gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
                gr.File(label="Or upload a PDF file")],
        outputs="text"
    )
    iface.launch()

if __name__ == "__main__":
    main()
