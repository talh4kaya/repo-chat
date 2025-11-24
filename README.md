# 🧠 Repo-Chat: Local RAG with Llama 3

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green.svg)
![Ollama](https://img.shields.io/badge/Model-Llama3-orange.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)

**Repo-Chat**, GitHub üzerindeki herhangi bir kod tabanını indirip analiz eden ve **yerel yapay zeka (Local LLM)** kullanarak kodlarınızla sohbet etmenizi sağlayan bir RAG (Retrieval-Augmented Generation) asistanıdır.

Bu proje, verilerinizi 3. parti sunuculara (OpenAI vb.) göndermeden, tamamen kendi bilgisayarınızda (Offline & Private) çalışır.

---

## 🚀 Özellikler

* **🔒 %100 Gizlilik:** Kodlarınız bilgisayarınızdan dışarı çıkmaz.
* **🧠 Llama 3 Gücü:** Meta'nın en son teknoloji açık kaynak modelini kullanır.
* **⚡ Vektör Arama:** ChromaDB ile kodlar arasında anlamsal arama yapar.
* **💬 Modern Arayüz:** Streamlit ile geliştirilmiş, temiz ve kullanıcı dostu chat ekranı.

---

## 🛠 Kurulum

### 1. Gereksinimler
* **Python 3.9+**
* **Ollama** (Llama 3 modelini çalıştırmak için)

### 2. Kurulum Adımları

```bash
# 1. Repoyu klonlayın
git clone [https://github.com/KULLANICI_ADIN/repo-chat.git](https://github.com/KULLANICI_ADIN/repo-chat.git)
cd repo-chat

# 2. Sanal ortamı kurun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Kütüphaneleri yükleyin
pip install -r requirements.txt



Harika bir fikir! 🎨 Çalışan bir sistemi "Satılabilir bir Ürüne" dönüştürmenin yolu, Kullanıcı Deneyimi (UI/UX) ve Sunumdan (README) geçer.

Şu anki arayüz biraz "ham". Onu modern, ferah (beyaz tema) ve profesyonel bir Chatbot görünümüne kavuşturacağız. Ayrıca GitHub vitrinini de süsleyeceğiz.

Hadi projeye son makyajı yapalım.

🎨 ADIM 1: Modern ve Beyaz Tema Ayarı
Streamlit varsayılan olarak sistem temasını (karanlık/aydınlık) kullanır. Biz bunu zorla Beyaz/Aydınlık yapacağız ve renkleri güzelleştireceğiz.

Proje klasörünün içinde .streamlit adında (başında nokta var) yeni bir klasör oluştur.

O klasörün içine config.toml adında bir dosya oluştur.

İçine şu ayarları yapıştır:

Ini, TOML

[theme]
base = "light"
primaryColor = "#2563EB" # Profesyonel Mavi
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#1F2937"
font = "sans serif"

[server]
headless = true
(Bu ayar, sitenin her zaman bembeyaz, temiz ve kurumsal görünmesini sağlar).

💅 ADIM 2: app.py Makyajı (Profesyonel UI)
Mevcut app.py dosyanı aç ve tamamen sil. Yerine aşağıdaki geliştirilmiş kodu yapıştır.

Yenilikler:

Sidebar (Yan Panel): Ayarlar ve "Sohbeti Temizle" butonu eklendi.

Özel CSS: Mesaj balonları (WhatsApp tarzı) eklendi.

Avatar: Kullanıcı ve AI için ikonlar.

Temiz Düzen: Gereksiz yazılar kaldırıldı.

Python

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
📝 ADIM 3: requirements.txt Oluşturma
Artık proje bittiğine göre, başkalarının da çalıştırabilmesi için kütüphane listesini çıkaralım.

Terminalde:

Bash

pip freeze > requirements.txt
📄 ADIM 4: README.md (Vitrin Düzenleme)
Projenin ana dizininde README.md adında bir dosya oluştur ve aşağıdaki Profesyonel Tanıtımı yapıştır.

Markdown

# 🧠 Repo-Chat: Local RAG with Llama 3

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green.svg)
![Ollama](https://img.shields.io/badge/Model-Llama3-orange.svg)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red.svg)

**Repo-Chat**, GitHub üzerindeki herhangi bir kod tabanını indirip analiz eden ve **yerel yapay zeka (Local LLM)** kullanarak kodlarınızla sohbet etmenizi sağlayan bir RAG (Retrieval-Augmented Generation) asistanıdır.

Bu proje, verilerinizi 3. parti sunuculara (OpenAI vb.) göndermeden, tamamen kendi bilgisayarınızda (Offline & Private) çalışır.

---

## 🚀 Özellikler

* **🔒 %100 Gizlilik:** Kodlarınız bilgisayarınızdan dışarı çıkmaz.
* **🧠 Llama 3 Gücü:** Meta'nın en son teknoloji açık kaynak modelini kullanır.
* **⚡ Vektör Arama:** ChromaDB ile kodlar arasında anlamsal arama yapar.
* **💬 Modern Arayüz:** Streamlit ile geliştirilmiş, temiz ve kullanıcı dostu chat ekranı.

---

## 🛠 Kurulum

### 1. Gereksinimler
* **Python 3.9+**
* **Ollama** (Llama 3 modelini çalıştırmak için)

### 2. Kurulum Adımları

```bash
# 1. Repoyu klonlayın
git clone [https://github.com/KULLANICI_ADIN/repo-chat.git](https://github.com/KULLANICI_ADIN/repo-chat.git)
cd repo-chat

# 2. Sanal ortamı kurun
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Kütüphaneleri yükleyin
pip install -r requirements.txt
3. Modelin Hazırlanması (Ollama)
Bilgisayarınızda Ollama'nın kurulu olduğundan emin olun ve terminalden modeli çekin:

Bash

ollama run llama3
🏃‍♂️ Kullanım
Adım 1: Kodları Hafızaya At (Ingestion)
Analiz etmek istediğiniz GitHub reposunu ingest.py içindeki REPO_URL kısmına yazın ve çalıştırın:

Bash

python ingest.py
(Bu işlem kodları indirir, parçalar ve ChromaDB veritabanına kaydeder).

Adım 2: Asistanı Başlat
Bash

streamlit run app.py
Tarayıcınızda açılan ekrandan kodlarınızla konuşmaya başlayabilirsiniz! 🎉

🏗 Mimari
Ingestion: gitpython ile repo indirilir.

Splitting: RecursiveCharacterTextSplitter ile kodlar parçalanır.

Embedding: HuggingFaceEmbeddings ile vektöre çevrilir.

Vector Store: ChromaDB üzerinde saklanır.

Retrieval & Chat: Kullanıcı sorusu LangChain aracılığıyla Llama 3'e iletilir ve en alakalı kod parçalarıyla birlikte cevaplanır.