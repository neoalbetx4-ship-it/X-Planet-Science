import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="X Planet Science", layout="wide")

# 2. AI Configuration
# API Key ကို စာကြောင်းတစ်ကြောင်းတည်းဖြစ်အောင် ထည့်ထားသည်
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")

# 3. User Interface
st.title("🪐 X Planet Science")
st.subheader("Future of Science Learning by Neon")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")

if st.button("Explain"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                # Model နာမည်ကို gemini-pro ဟု ပြောင်းလဲအသုံးပြုသည်
                model = genai.GenerativeModel('gemini-pro')
                res = model.generate_content(f"Explain this science topic clearly in Burmese for students: {query}")
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
                # Error ထပ်တက်လျှင် တခြား Model တစ်ခုဖြင့် ထပ်စမ်းရန်
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash-latest')
                    res = model.generate_content(f"Explain in Burmese: {query}")
                    st.markdown(res.text)
                except Exception as e2:
                    st.error(f"ချိတ်ဆက်မှု အဆင်မပြေပါ- {e2}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
        
