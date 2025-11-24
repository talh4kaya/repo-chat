import streamlit as st

st.set_page_config(page_title="Repo-Chat", page_icon="🤖")

st.title("🤖 Repo-Chat: Kodlarınla Konuş")

st.write("GitHub linkini yapıştır, yapay zeka kodlarını okusun, sen sor o cevaplasın!")

repo_url = st.text_input("GitHub Repo Linki:", placeholder="https://github.com/username/project")

if repo_url:
    st.success(f"Analiz edilecek repo: {repo_url}")
    if st.button("Analizi Başlat 🚀"):
        st.write("⏳ Kodlar indiriliyor ve okunuyor... (Simülasyon)")