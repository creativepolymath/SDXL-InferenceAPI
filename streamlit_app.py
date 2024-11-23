import streamlit as st
import logging
from huggingface_hub import InferenceClient

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the InferenceClient with the model and token
client = InferenceClient("stabilityai/stable-diffusion-xl-base-1.0", token="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")

# Set up the Streamlit interface
st.title("Huggingface API Image Generator")
st.write("Enter a prompt and select a style to generate an image.")

# Collect user input
prompt = st.text_input("Prompt", "A beautiful landscape")

# Function to call the Huggingface API using InferenceClient
def generate_image(prompt):
    try:
        logger.info("Generating image with prompt: %s", prompt)
        result = client.text_to_image(prompt)
        logger.info("Image generated successfully")
        return result
    except Exception as e:
        logger.error("An error occurred: %s", str(e))
        st.error(f"An error occurred: {str(e)}")
        return None

# Generate image on button click
if st.button("Generate Image"):
    result = generate_image(prompt)
    if result:
        if isinstance(result, bytes):
            st.image(result, caption="Generated Image")
