import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="X Planet Science", layout="wide")

# 2. AI Configuration
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
                
                # Visual Support Section (Indentation မှန်အောင် ပြင်ပေးထားသည်)
                low_q = query.lower()
                if "solar system" in low_q or "စကြာဝဠာ" in low_q:
                    st.info("💡 နေအဖွဲ့အစည်း")
                    st.write("နေနှင့် ဂြိုဟ်များ၏ တည်နေရာပြပုံရိပ်")
                    [attachment_0](attachment)
                elif "cell" in low_q or "ဆဲလ်" in low_q:
                    st.info("💡 ဆဲလ်တည်ဆောက်ပုံ")
                    st.write("ဆဲလ်အတွင်းရှိ အစိတ်အပိုင်းများ")
                    [attachment_1](attachment)
                elif "heart" in low_q or "နှလုံး" in low_q:
                    st.info("💡 နှလုံးတည်ဆောက်ပုံ")
                    st.write("နှလုံး၏ အခန်းများနှင့် သွေးကြောများ")
                    
            
            except Exception as e:
                st.error(f"AI ချိတ်ဆက်မှု အဆင်မပြေပါ- {e}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
                
