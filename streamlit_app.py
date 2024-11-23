import streamlit as st
import httpx

# Set up the Streamlit interface
st.title("Huggingface API Image Generator")
st.write("Enter a prompt and select a style to generate an image.")

# Collect user input
prompt = st.text_input("Prompt", "A beautiful landscape")
style = st.selectbox("Style", ["Realistic", "Cartoon", "Abstract"])

# Function to call the Huggingface API
def generate_image(prompt, style):
    # Replace 'your_api_key' with your actual Huggingface API key
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": prompt, "options": {"style": style}}
    
    # Make a request to the Huggingface API
    response = httpx.post("https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to generate image. Please try again.")
        return None

# Generate image on button click
if st.button("Generate Image"):
    result = generate_image(prompt, style)
    if result:
        st.image(result["image"], caption="Generated Image")
        st.write("Response:", result["text"])
