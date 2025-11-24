import streamlit as st
import time
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# SAYFA AYARLARI
st.set_page_config(page_title="Repo-Chat AI", page_icon="🧠", layout="centered")

# ÖZEL CSS (Mesaj Balonları için)
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stChatMessage[data-testid="stChatMessageUser"] {
        background-color: #E3F2FD;
        border-left: 5px solid #2196F3;
    }
    .stChatMessage[data-testid="stChatMessageAssistant"] {
        background-color: #F5F5F5;
        border-left: 5px solid #4CAF50;
    }
    h1 {
        color: #1F2937;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# YAN PANEL (SIDEBAR)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/chatbot.png", width=80)
    st.title("Repo-Chat v1.0")
    st.caption("🚀 Local RAG System")
    
    st.markdown("---")
    st.markdown("### ⚙️ Model Bilgisi")
    st.info("🧠 **Brain:** Llama 3 (8B)\n🗂️ **Memory:** ChromaDB")
    
    if st.button("🗑️ Sohbeti Temizle", type="primary"):
        st.session_state.messages = []
        st.rerun()
        
    st.markdown("---")
    st.markdown("Developed by **Talha Kaya**")

# ---------------------------------------------------------
# RAG SİSTEMİ YÜKLEME
# ---------------------------------------------------------
DB_PATH = "./chroma_db"

@st.cache_resource
def load_rag_system():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    llm = ChatOllama(model="llama3", temperature=0.1)
    
    template = """
    Sen uzman bir Kıdemli Yazılım Mühendisisin.
    Aşağıdaki kod parçalarını kullanarak kullanıcının sorusunu teknik olarak cevapla.
    Cevabın Türkçe olsun.
    
    Kodlar:
    {context}
    
    Soru: {question}
    
    Cevap:
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectordb.as_retriever(search_kwargs={"k": 4}),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
        return_source_documents=True
    )
    return qa_chain

try:
    qa = load_rag_system()
except Exception as e:
    st.error(f"Sistem yüklenemedi: {e}")
    st.stop()

# ---------------------------------------------------------
# ANA EKRAN
# ---------------------------------------------------------
st.title("💬 Kodlarınla Sohbet Et")
st.caption("GitHub reponuzdaki kodları analiz eder ve sorularınızı yanıtlar.")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Merhaba! Kodlarınızı inceledim. Bana mimari, fonksiyonlar veya hatalar hakkında soru sorabilirsin. 👋"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🧑‍💻" if message["role"] == "user" else "🤖"):
        st.markdown(message["content"])

if prompt := st.chat_input("Bir soru sor..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        with st.spinner("Kodlar taranıyor..."):
            result = qa.invoke({"query": prompt})
            response = result["result"]
            
            sources = list(set([doc.metadata.get("source", "Bilinmiyor") for doc in result["source_documents"]]))
            
            full_response = f"{response}\n\n---\n**📚 Kaynak Dosyalar:**\n"
            for src in sources:
                # Dosya yolunu temizle (sadece dosya adı kalsın)
                clean_src = src.split("\\")[-1].split("/")[-1]
                full_response += f"- `{clean_src}`\n"
            
            message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})