import streamlit as st
import logging
from huggingface_hub import InferenceClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the InferenceClient with the model and token
client = InferenceClient("stabilityai/stable-diffusion-xl-base-1.0", token="hf_YOUR_TOKEN_HERE")

# Set up the Streamlit interface
st.title("Huggingface API Image Generator")
st.write("Enter a prompt and select a style to generate an image.")

# Collect user input
prompt = st.text_input("Prompt", "A beautiful landscape")

# Collect user input for style
style = st.selectbox("Select Style", ["Realistic", "Artistic", "Cartoon", "Abstract"])

# Function to call the Huggingface API using InferenceClient
def generate_image(prompt, style):
    # Concatenate prompt and style
    styled_prompt = f"{prompt} in {style} style"
    try:
        logger.info("Generating image with styled prompt: %s", styled_prompt)
        result = client.text_to_image(styled_prompt)
        logger.info("Image generated successfully")
        return result
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        st.error(f"An error occurred: {str(e)}")
        return None

# Generate image on button click
if st.button("Generate Image"):
    result = generate_image(prompt, style)
    if result:
        if isinstance(result, bytes):
            st.image(result, caption="Generated Image")
        else:
            st.write("Response:", result)
