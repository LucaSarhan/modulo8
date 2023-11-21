# Import necessary libraries
import requests
import json
import gradio as gr

# Define the URL and headers for the language model API
url = "http://localhost:11434/api/generate"
headers = {
    'Content-Type': 'application/json',
}

# Initialize a list to store the conversation history
history_conversation = []

# Function to generate a response based on user input and uploaded files
def response_generate(prompt, uploaded_file=None):
    # Assuming you want to include the file contents in the prompt
    if uploaded_file:
        # Read the content of the uploaded file
        with open(uploaded_file.name, 'r') as file:
            file_content = file.read()
        # Append the file content to the original prompt with a newline separator
        prompt += "\n" + file_content

    # Append the updated prompt to the conversation history
    history_conversation.append(prompt)

    # Create the full conversation history by joining elements with newline separators
    full_prompt = "\n".join(history_conversation)

    # Construct data to be sent in the POST request
    data = {
        "model": "dolphin2.2-mistral",
        "stream": False,
        "prompt": full_prompt,
    }

    # Make a POST request to the specified URL
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Handle the response
    if response.status_code == 200:
        # Process the response text and extract the actual response
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data["response"]
        # Append the actual response to the conversation history
        history_conversation.append(actual_response)
        return actual_response
    else:
        # Print an error message if the response status code is not 200
        print("Error:", response.status_code, response.text)
        return None

# Main function to set up and launch the Gradio interface
def main():
    # Create a Gradio interface with a Textbox for user input and a File input for uploaded files
    iface = gr.Interface(
        fn=response_generate,
        inputs=[gr.Textbox(lines=2, placeholder="Enter your prompt here..."),
                gr.File()],
        outputs="text"
    )

    # Launch the Gradio interface
    iface.launch()

# Entry point for the script
if __name__ == "__main__":
    main()
