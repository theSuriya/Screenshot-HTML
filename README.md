# Screenshot to HTML Converter using Gemini 1.5

## Project Overview
**Objective**:
The objective of this project is to create a tool that converts a screenshot of a webpage into HTML and CSS code. This allows users to easily replicate the design and layout of a webpage by simply providing an image of it.

## Key Features:

- **Streamlit Web App**: The project is built using Streamlit, a Python library for creating web applications. Users interact with the application through a user-friendly interface.
- **Gemini 1.5 Model**: The project utilizes the Gemini 1.5 model provided by Google GenerativeAI. This model is capable of understanding the structure and design of a webpage from an image and generating corresponding HTML and CSS code.
- **Upload Image**: Users can upload a screenshot of the webpage they want to convert. The application accepts image files in common formats such as JPG, JPEG, and PNG.
- **Generate Code**: Once the image is uploaded, users can click a button to initiate the code generation process. The Gemini 1.5 model analyzes the screenshot and generates HTML and CSS code that replicates the design of the webpage.
- **View Generated Code**: The generated HTML and CSS code is displayed within the application, allowing users to inspect and copy it for use in their own projects.

## Application Demo

here is the demo of an App in huggingface click [here](https://huggingface.co/spaces/suriya7/Screenshot-HTML)
  
## Usage

1. **Upload Image**: Upload a screenshot of the webpage you want to convert.
2. **Generate Code**: Click on the "Create a webpage" button to generate HTML and CSS code based on the uploaded screenshot.
3. **View Code**: The generated HTML and CSS code will be displayed below.

## Prerequisites

- Python 3.x
- Streamlit
- Google GenerativeAI library
- Gemini 1.5 API key (set as `GOOGLE_API_KEY` environment variable)

## Installation

1. **Clone the repositor**:

```bash
git clone https://github.com/theSuriya/Screenshot-HTML
```
2. **Open in Your Favorite IDE**: Open the cloned directory in your preferred Integrated Development Environment (IDE) such as Visual Studio Code, PyCharm, or any other IDE of your choice.

3. **Google API KEY**:Go to this site to generate api key [HERE](https://aistudio.google.com) You can see left side generate api thn click and copy. Once you have the api key, locate the .env file in your project directory. Open it and paste your aoi key like this:
  ```bash
  GOOGLE_API_KEY = "paste the api key here"
  ```
4. **Install Dependencies**: Make sure you have Python installed on your system. Then, In your terminal or command prompt within the project directory, run:
```bash
pip install -r requirements.txt
```
5. **Run the Application**: Navigate to the project directory and run the following command:
 ```bash
 streamlit run app.py
 ```

## Acknowledgments
- Streamlit - For creating interactive web apps with Python.
- Google GenerativeAI - For providing access to the Gemini 1.5 model.
  
## Contributing
Contributions are welcome. Please open an issue to discuss changes or propose a pull request.
