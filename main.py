import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="X Planet Science", layout="wide")

# API Configuration - Key ကို စာကြောင်းတစ်ကြောင်းတည်းဖြစ်အောင် သေချာထည့်ပါ
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")

# UI Design
st.title("🪐 X Planet Science")
st.subheader("Future of Science Learning by Neon")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")

if st.button("Explain"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                # Model ကို 'gemini-pro' လို့ ပြောင်းသုံးကြည့်ပါမယ် (ပိုငြိမ်လို့ပါ)
                model = genai.GenerativeModel('gemini-pro')
                res = model.generate_content(f"Explain clearly in Burmese: {query}")
                st.markdown(res.text)
                
                # Visuals
                if "solar system" in query.lower() or "စကြာဝဠာ" in query:
                    [attachment_0](attachment)
                elif "heart" in query.lower() or "နှလုံး" in query:
                    
                    
            except Exception as e:
                # Error ထပ်တက်ရင် Model နာမည် ထပ်ပြောင်းဖို့ ကြိုးစားပါမယ်
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    res = model.generate_content(f"Explain clearly in Burmese: {query}")
                    st.markdown(res.text)
                except Exception as e2:
                    st.error(f"ချိတ်ဆက်မှု အဆင်မပြေပါ- {e2}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
                
