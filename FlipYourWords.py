import streamlit as st

#Program Membalikkan Kata
st.title('Flip your words!')
String = st.text_input('Type a Word') [::-1]

if String:
    st.code(String)
