import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="X Planet Science", layout="wide")

# 2. AI Configuration
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
# Model နာမည်ကို models/gemini-1.5-flash ဟု ပြောင်းလဲလိုက်သည်
model = genai.GenerativeModel('models/gemini-1.5-flash')

# 3. User Interface
st.title("🪐 X Planet Science")
st.subheader("Future of Science Learning by Neon")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")

if st.button("Explain"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                prompt = f"Explain this science topic clearly in Burmese for students: {query}"
                res = model.generate_content(prompt)
                st.markdown(res.text)
                
                # Visual Support
                low_q = query.lower()
                if "solar system" in low_q or "နေအဖွဲ့အစည်း" in low_q:
                    st.info("💡 နေအဖွဲ့အစည်း၏ ပုံရိပ်လွှာ")
                                    elif "human heart" in low_q or "နှလုံး" in low_q:
                    st.info("💡 လူသားနှလုံး၏ တည်ဆောက်ပုံ")
                                
            except Exception as e:
                st.error(f"AI ချိတ်ဆက်မှု အခက်အခဲ ဖြစ်နေပါသည်: {e}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
                                        
