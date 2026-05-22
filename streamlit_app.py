import streamlit as st

st.title("🎈 alifia's app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("Haii")
st.title("_SEMANGATT_ YAA :blue[SAYANG] :sunglasses:")
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
