import streamlit as st
import google.generativeai as genai

# --- CONFIG ---
st.set_page_config(page_title="X Planet Science", layout="wide")
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
model = genai.GenerativeModel('gemini-1.5-flash')

# --- UI ---
st.title("🪐 X Planet Science")
st.write("Welcome to the Future of Science Learning!")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")
if st.button("Explain"):
    if query:
        with st.spinner("AI thinking..."):
            res = model.generate_content(f"Explain this in Burmese for students: {query}")
            st.markdown(res.text)
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပါဗျာ။")
        
