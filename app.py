import streamlit as st
import requests
import os
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# Streamlit UI
st.set_page_config(page_title="Image Generator", layout="centered")
st.title("AI Image Generator")
st.markdown("Enter a prompt below to generate a photorealistic image.")

# Prompt input
prompt = st.text_area("Enter your Imagination:", placeholder="e.g. A photorealistic image of a tiger in a jungle")

# Image Generation
if st.button("Generate Image"):
    if not API_KEY or not BASE_URL:
        st.error("Missing API key or base URL in the .env file.")
    elif not prompt:
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": "provider-4/imagen-4",
                "prompt": prompt,
                "n": 1,
                "size": "1024x1024"
            }

            try:
                response = requests.post(f"{BASE_URL}/images/generations", headers=headers, json=payload)
                response.raise_for_status()
                image_url = response.json()["data"][0]["url"]

                # Display image
                st.image(image_url, caption="Generated Image", use_column_width=True)

                # Download option
                img_data = requests.get(image_url).content
                st.download_button(
                    label="Download Image",
                    data=img_data,
                    file_name="generated_image.png",
                    mime="image/png"
                )
            except requests.exceptions.RequestException as e:
                st.error(f"Error generating image: {e}")
