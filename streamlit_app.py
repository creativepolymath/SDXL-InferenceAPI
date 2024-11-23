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
    
    try:
        # Make a request to the Huggingface API
        response = httpx.post("https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0", headers=headers, json=payload)
        response.raise_for_status()

        # Check if the response is JSON or binary
        if response.headers['Content-Type'] == 'application/json':
            return response.json()
        else:
            return response.content

    except httpx.HTTPStatusError as e:
        st.error(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        st.write("Please check if the model name and API key are correct.")
    except httpx.RequestError as e:
        st.error(f"Request error occurred: {str(e)}")
        st.write("There might be a network issue. Please try again later.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        st.write("Please check the logs for more details.")
    return None

# Generate image on button click
if st.button("Generate Image"):
    result = generate_image(prompt, style)
    if result:
        if isinstance(result, bytes):
            st.image(result, caption="Generated Image")
        else:
            st.write("Response:", result.get("text", "No text response"))
