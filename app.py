from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)


def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    


st.set_page_config(page_title="Image Info Generator")

st.header("Image Info Generator")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Generate")

input_prompt = """
You are an expert in understanding images and makeing judgements.
"""

# If submit button is clicked what should happen
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)

    st.subheader("The Response is")
    st.write(response)
