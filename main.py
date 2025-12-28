import streamlit as st
import google.generativeai as genai

# 1. Page Design & Theme
st.set_page_config(page_title="X Planet Science", layout="wide", page_icon="🪐")

# CSS for styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 2. AI Configuration
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. Sidebar for Info
with st.sidebar:
    st.title("🚀 Navigation")
    st.info("X Planet Science သည် ကလေးများအတွက် သိပ္ပံဗဟုသုတ ရှာဖွေရာနေရာ ဖြစ်သည်။")
    st.image("https://img.freepik.com/free-vector/outer-space-exploration-abstract-concept-vector-illustration_335657-1906.jpg")

# 4. Main Body
st.title("🪐 X Planet Science")
st.write("စကြဝဠာရဲ့ လျှို့ဝှက်ချက်တွေကို အတူတူ ရှာဖွေကြရအောင်!")

query = st.text_input("သိပ္ပံမေးခွန်းတစ်ခုခုကို မြန်မာလို ရိုက်ထည့်ပါ:", placeholder="ဥပမာ- လကမ္ဘာအကြောင်း ရှင်းပြပါ")

if st.button("အဖြေရှာမယ်"):
    if query:
        with st.spinner("AI က အဖြေရှာပေးနေပါတယ်..."):
            try:
                prompt = f"Explain this science topic simply in Burmese with 5 bullet points and a conclusion: {query}"
                res = model.generate_content(prompt)
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.success("ရှာဖွေမှု ရလဒ်-")
                    st.markdown(res.text)
                
                with col2:
                    # Logic for visual diagrams
                    low_q = query.lower()
                    if "sun" in low_q or "နေ" in low_q:
                        st.write("☀️ **နေ၏ တည်ဆောက်ပုံ**")
                        
                    elif "moon" in low_q or "လ" in low_q:
                        st.write("🌙 **လ၏ အဆင့်ဆင့်ပြောင်းလဲပုံ**")
                        [attachment_0](attachment)
                    elif "plant" in low_q or "အပင်" in low_q:
                        st.write("🌱 **အပင်၏ အစိတ်အပိုင်းများ**")
                        
                        
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("မေးခွန်းတစ်ခုခု အရင်ရိုက်ထည့်ပါဗျာ။")
        
