import gradio as gr
import requests

# Ollama local API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Your model
MODEL_NAME = "codegemma:2b"


def generate_code(prompt):
    if not prompt:
        return "Please enter a prompt."

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        result = response.json()
        return result.get("response", "No response received.")

    except Exception as e:
        return f"Error: {str(e)}"


# Gradio Interface
interface = gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(
        lines=5,
        label="Enter your prompt",
        placeholder="e.g. Write a Python function for binary search"
    ),
    outputs=gr.Textbox(label="Generated Output"),
    title="Local AI Coding Assistant",
    description="Runs locally using Ollama (codegemma:2b)."
)


# Run the app
if __name__ == "__main__":
    interface.launch()