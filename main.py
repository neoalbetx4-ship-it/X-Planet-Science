import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="X Planet Science", layout="wide")

# 2. AI Configuration
# API Key ကို စာကြောင်းတစ်ကြောင်းတည်းဖြစ်အောင် သေသေချာချာထည့်ထားပါသည်
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
model = genai.GenerativeModel('gemini-1.5-flash')

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
                
                # Visual Support Logic
                low_q = query.lower()
                if "cell" in low_q:
                    st.info("💡 ဆဲလ်အကြောင်း ပုံရိပ်လွှာ")
                    # [attachment_0](attachment)
                elif "heart" in low_q:
                    st.info("💡 နှလုံး၏ တည်ဆောက်ပုံ")
                    # 
                elif "atom" in low_q:
                    st.info("💡 အက်တမ်၏ တည်ဆောက်ပုံ")
                    # 
            
            except Exception as e:
                st.error(f"AI နှင့် ချိတ်ဆက်ရာတွင် အမှားရှိနေပါသည်: {e}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
                
