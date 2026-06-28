import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Pro Summary", page_icon="⚡", layout="centered")

# Tasarımı daha "premium" yapmak için modern CSS
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .stTextArea label { font-size: 1.2rem; color: #58a6ff !important; }
    .stButton>button { 
        background: linear-gradient(90deg, #58a6ff, #1f6feb); 
        color: white; border: none; border-radius: 6px; 
        padding: 0.6rem 2rem; font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ AI Content Summarizer")
st.write("---")

api_key = st.sidebar.text_input("Gemini API Key", type="password")

text = st.text_area("Özetlenecek İçerik:", placeholder="Metni buraya yapıştırın...", height=200)

if st.button("Özetleme İşlemini Başlat"):
    if api_key and text:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-pro')
            with st.spinner('Yapay zeka zihnini çalıştırıyor...'):
                response = model.generate_content(f"Lütfen şu metni profesyonel bir özet haline getir:\n{text}")
                st.subheader("📝 Özet")
                st.markdown(f"**{response.text}**")
        except Exception as e:
            st.error(f"Hata: {e}")
    else:
        st.warning("Lütfen API Key ve metin girin.")