# let try this spaCy
# https://www.youtube.com/watch?v=6acv9LL6gHg 
# https://www.youtube.com/watch?v=DBBpLrhKzC8

import streamlit as st
import spacy
from textblob import TextBlob

def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    return tokens


def main():
    st.title("NLPiffy with Streamlit")
    st.subheader("Natural Language Processing on the Go")

    # Tokenization
    if st.checkbox("Show Token and Lemma"):
        st.subheader("Tokenize Your Text")
        message = st.text_area("Enter Your Text", "Type Here")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.success(nlp_result)


    # Named Entity
    # Sentiment Analysis
    # Text Summarization


if __name__ == '__main__':
    main()