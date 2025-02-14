import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
api_key = st.secrets["huggingface"]["HUGGINGFACE_API_KEY"]
