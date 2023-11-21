import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

history_conversation = []

def response_generate(prompt):
    history_conversation.append(prompt)

    full_prompt = "\n".join(history_conversation)

    data = {
        "model": "dolphin2.2-mistral",
        "stream": False,
        "prompt": full_prompt,
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        history_conversation.append(actual_response)
        return actual_response
    else:
        print("Error:", response.status_code, response.text)
        return None

def main():
    iface = gr.Interface(
        fn=response_generate,
        inputs=gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
        outputs="text"
    )

    iface.launch()

if __name__ == "__main__":
    main()