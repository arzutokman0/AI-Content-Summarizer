import streamlit as st
import google.generativeai as genai

# Sayfa Yapılandırması
st.set_page_config(page_title="AI ProSummarizer", page_icon="⚡", layout="wide")

# Modern Premium Tasarım (CSS)
st.markdown("""
    <style>
    /* Ana Sayfa Arka Plan */
    .stApp { background-color: #0b0e14; }
    
    /* Kart Stilleri */
    div.stTextArea > label { color: #8892b0; font-weight: bold; }
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 3em; 
        background-image: linear-gradient(to right, #6c63ff, #9f9ae0);
        color: white; border: none; font-size: 1.1em;
    }
    
    /* Başlıklar */
    h1 { color: #e6edf3 !important; text-align: center; margin-bottom: 30px; }
    .css-1r6slb0 { background-color: #161b22; border-radius: 10px; padding: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Başlık
st.title("⚡ AI Content Summarizer Pro")

# Layout: İki sütun yapalım
col1, col2 = st.columns([1, 2])

with col1:
    st.sidebar.header("🔑 Authentication")
    api_key = st.sidebar.text_input("Gemini API Key", type="password")
    st.sidebar.markdown("---")
    st.sidebar.info("Profesyonel metin özetleme aracınız.")

with col2:
    text = st.text_area("Metninizi buraya yapıştırın:", height=300)
    if st.button("Özetleme İşlemini Başlat"):
        if api_key and text:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel('gemini-pro')
                with st.spinner('Yapay zeka metni analiz ediyor...'):
                    response = model.generate_content(f"Lütfen şu metni profesyonelce özetle:\n{text}")
                    st.success("✨ Özet Başarıyla Oluşturuldu")
                    st.markdown(f"--- \n {response.text}")
            except Exception as e:
                st.error(f"Hata: {e}")
        else:
            st.error("Lütfen önce API anahtarınızı girin ve bir metin yapıştırın.")