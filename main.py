import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="X Planet Science", layout="wide")

# AI Configuration
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
model = genai.GenerativeModel('gemini-1.5-flash')

# User Interface
st.title("🪐 X Planet Science")
st.subheader("Future of Science Learning by Neon")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")

if st.button("Explain"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                res = model.generate_content(f"Explain clearly in Burmese: {query}")
                st.markdown(res.text)
                
                # Visual Support
                low_q = query.lower()
                if "solar system" in low_q or "စကြာဝဠာ" in low_q:
                    st.info("💡 နေအဖွဲ့အစည်း")
                    [attachment_0](attachment)
                elif "cell" in low_q or "ဆဲလ်" in low_q:
                    st.info("💡 ဆဲလ်တည်ဆောက်ပုံ")
                    [attachment_1](attachment)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
        
