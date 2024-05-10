import streamlit as st
import google.generativeai as genai
from PIL import Image
import os

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

model=genai.GenerativeModel('gemini-1.5-pro-latest')
input_prompt = """
As an HTML and CSS expert, your task is to create complete HTML and CSS code based on the provided screenshot, ensuring clear and functional markup. Provide a main.html file with inline CSS that replicates the exact color and style as shown in the given screenshot.
Output structure:
Start and end with (```)
"""

def generate_response(input_prompt,image):
    response = model.generate_content([input_prompt,image[0]])
    # print(response.text)
    return response.text

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")
    
st.title("SCREENSHOT - HTML CODE📃")
st.text("Uploade your demo webpage image Here:")

upload_file = st.file_uploader('',type=['jpg','jpeg','png'])
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
submit = st.button('Create a webpage')
if submit:
    image_data = input_image_setup(uploaded_file=upload_file)
    with st.spinner("Building the Webpage..."):
        response = generate_response(input_prompt, image_data)
        st.subheader("CODE:")
        st.markdown(response)
