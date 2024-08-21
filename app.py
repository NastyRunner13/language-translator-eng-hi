import streamlit as st
import pickle
from transformers import TFAutoModelForSeq2SeqLM

with open('tokenizer.pkl', 'rb') as file:
    loaded_tokenizer = pickle.load(file)

model = TFAutoModelForSeq2SeqLM.from_pretrained("tf_model/")

st.title("TRANSLATE YOUR TEXT FROM ENGLISH TO HINDI")

source_lan = st.text_input(label="Please provide text you want to translate to hindi")

submit_button = st.button(label="Sumbit to translate text")

if source_lan and submit_button:

    tokenized = loaded_tokenizer([source_lan], return_tensors='np')
    out = model.generate(**tokenized, max_length=128)

    with loaded_tokenizer.as_target_tokenizer():
        output_text = loaded_tokenizer.decode(out[0], skip_special_tokens=True)

    st.write(output_text)