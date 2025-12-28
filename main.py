import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="X Planet Science", layout="wide")

# 2. AI Configuration
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")

# 3. User Interface
st.title("🪐 X Planet Science")
st.subheader("Future of Science Learning by Neon")

query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")

if st.button("Explain"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                # 4. Model Selection (gemini-1.5-flash ကို တိုက်ရိုက်ခေါ်သည်)
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Explain this science topic clearly in Burmese for students: {query}"
                res = model.generate_content(prompt)
                st.markdown(res.text)
                
                # Visual Support
                low_q = query.lower()
                if "solar system" in low_q or "နေအဖွဲ့အစည်း" in low_q:
                    st.info("💡 နေအဖွဲ့အစည်း")
                    [attachment_0](attachment)
                elif "cell" in low_q or "ဆဲလ်" in low_q:
                    st.info("💡 ဆဲလ်တည်ဆောက်ပုံ")
                    [attachment_1](attachment)
            
            except Exception as e:
                # Error ထပ်တက်ရင် ဘာကြောင့်လဲဆိုတာ သေချာပြရန်
                st.error(f"ချိတ်ဆက်မှု အဆင်မပြေပါ- {e}")
                st.info("💡 API Key သို့မဟုတ် Model Name ကို ပြန်လည်စစ်ဆေးနေပါသည်။")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
        
