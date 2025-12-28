import streamlit as st
import google.generativeai as genai

# 1. Page Config
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
                # Model ကို အသစ်ဆုံးဖြစ်တဲ့ 1.5-flash နဲ့ စမ်းပါမယ်
                model = genai.GenerativeModel('gemini-1.5-flash')
                res = model.generate_content(f"Explain clearly in Burmese: {query}")
                st.markdown(res.text)
                
                # Visual Support (Specific Search)
                low_q = query.lower()
                if "solar system" in low_q or "စကြာဝဠာ" in low_q:
                    st.info("💡 နေအဖွဲ့အစည်း")
                    [attachment_0](attachment)
                elif "cell" in low_q or "ဆဲလ်" in low_q:
                    st.info("💡 ဆဲလ်တည်ဆောက်ပုံ")
                    [attachment_1](attachment)
                elif "water cycle" in low_q or "မိုးရွာ" in low_q:
                    st.info("💡 ရေစက်ဝန်း လည်ပတ်ပုံ")
                    [attachment_2](attachment)
            
            except Exception as e:
                # Error ဖြစ်ရင် ဘာကြောင့်လဲဆိုတာ အတိအကျပြဖို့
                st.error(f"Error အသေးစိတ်: {e}")
                st.info("💡 Streamlit 'Manage app' ထဲမှာ Reboot App ကို တစ်ချက်နှိပ်ပေးပါ။")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပေးပါဗျာ။")
