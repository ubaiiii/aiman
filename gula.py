from langchain.agents import load_tools, initialize_agent
from langchain.llms import OpenAI
from serpapi import GoogleSearch
import os
import streamlit as st

from base64 import b64decode
import webbrowser
import openai


# Set Api key
os.environ["OPENAI_API_KEY"] = st.secrets["openai_pass"]
os.environ["SERPAPI_API_KEY"] = st.secrets["serpapi_pass"]


# Source : https://www.youtube.com/watch?app=desktop&v=ILGTMBKIDuc
def generateImage(prompt, image_count):
    images = []
    response = openai.Image.create (
        prompt = prompt,
        n = image_count,
        size = '256x256',
        response_format='url'
    )

    for image in response['data']:
       # return webbrowser.open(image.url)
       return image.url


st.header ("Ask me a question? ")
question_text = st.text_input('Enter your desire : ')

if len(question_text) > 10 :   
    llm = OpenAI(temperature=0)
    tools = load_tools(["serpapi"])
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    res = agent.run(question_text)
    #st.write('Result : ', res)
    st.write('**Result :** ', res )

    try:
        question_image = generateImage(question_text, image_count=1)
        st.image (question_image, use_column_width=True, caption="caption")
    except openai.InvalidRequestError:
        st.write('Your request was rejected as a result of our safety system. Your prompt may contain text that is not allowed by our safety system')
    except :
        st.write('Generic Error')


    