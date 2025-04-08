import streamlit as st
from test_module import run_typing_test
from tips_module import show_tips
from history_module import show_history

st.set_page_config(page_title="Typing Speed Pro", layout="wide")

st.title("🔥 Typing Speed Pro")

page = st.sidebar.selectbox("Go to", ["Typing Test", "Tips & Tricks", "Performance History"])
if page == "Typing Test":
    run_typing_test()
elif page == "Tips & Tricks":
    show_tips()
elif page == "Performance History":
    show_history()
