import os
import gradio as gr
import google.generativeai as genai

# Configure genai with the API key from the environment variable
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

PRE_INPUT_PROMPT = (
    "Generate an abstract starting point essay for the Scope of this idea's implementation, "
    "possible Technical Architecture, Challenges that can be addressed with the idea and "
    "Future Direction. Make the tonality professional and 95-99% not typical to AI and "
    "Employ transitions and logical connections to create a seamless flow of thought no bullet points"
)

def generate(drop_your_idea):
    """Generates text using the pre-input prompt and user input."""

    full_prompt = f"{PRE_INPUT_PROMPT} {drop_your_idea}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(
        full_prompt,
        generation_config={
            "max_output_tokens": 2048,
            "temperature": 0.9,
            "top_p": 1
        },
        stream=False
    )
    output = response.candidates[0].content.parts[0].text
    return output

iface = gr.Interface(
    fn=generate,
    inputs="text",
    outputs="markdown",
    title="Explore Your Ideas"
)

iface.launch()
