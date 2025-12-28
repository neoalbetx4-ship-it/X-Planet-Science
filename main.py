import streamlit as st
import google.generativeai as genai
from datetime import datetime
import pytz
from PIL import Image
import time

# --- 🪐 X PLANET SCIENCE CONFIG ---
APP_NAME = "X Planet Science"
FOUNDER = "Neon (Htet Wai Yan Aung)"
genai.configure(api_key="AIzaSyCIdLE7izxix3nk3KKSgLeROI7n8boHltc")
model = genai.GenerativeModel('gemini-1.5-flash')
mm_tz = pytz.timezone('Asia/Yangon')

# --- 🎨 UI DESIGN ---
st.set_page_config(page_title=APP_NAME, layout="wide", page_icon="🪐")
st.markdown(f"""
    <style>
    .main {{ background-color: #0b0d11; color: #e0e0e0; }}
    .stButton>button {{ width: 100%; border-radius: 25px; background: linear-gradient(45deg, #00ffcc, #0099ff); color: black; font-weight: bold; height: 3.5em; }}
    h1 {{ color: #00ffcc; text-align: center; }}
    </style>
    """, unsafe_allow_html=True)

# --- 💾 SESSION MANAGEMENT ---
if "user" not in st.session_state: st.session_state.user = None
if "page" not in st.session_state: st.session_state.page = "Home"

# --- 👤 LOGIN ---
if not st.session_state.user:
    st.markdown(f"<h1>🪐 {APP_NAME}</h1>", unsafe_allow_html=True)
    u_id = st.text_input("Enter Scout Name to start:", placeholder="Neon...")
    if st.button("LAUNCH 🚀"):
        if u_id:
            st.session_state.user = u_id
            st.rerun()
else:
    with st.sidebar:
        st.header(f"🧪 {APP_NAME}")
        if st.button("🏠 Home"): st.session_state.page = "Home"
        if st.button("🥼 Virtual Lab"): st.session_state.page = "Lab"
        st.divider()
        if st.button("Logout"):
            st.session_state.user = None
            st.rerun()

    # --- 📄 CONTENT ---
    if st.session_state.page == "Home":
        st.header("🧬 AI Science Tutor")
        query = st.text_input("သိပ္ပံမေးခွန်းကို မြန်မာလို မေးမြန်းပါ:")
        if st.button("Explain"):
            with st.spinner("AI is thinking..."):
                res = model.generate_content(f"Explain clearly in Burmese: {query}")
                st.markdown(res.text)
                
                # Visual Support (Automated)
                low_q = query.lower()
                if "heart" in low_q:
                                    elif "cell" in low_q:
                    
    elif st.session_state.page == "Lab":
        st.header("🥼 Virtual Lab")
        st.info("အဆင့်မြင့် စမ်းသပ်ချက်များကို ဤနေရာတွင် လေ့လာပါ။")
        if st.button("Show Light Refraction Guide"):
                        st.write("အလင်းယိုင်ခြင်း စမ်းသပ်ချက် လမ်းညွှန်...")
