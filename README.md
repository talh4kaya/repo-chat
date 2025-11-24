# 🧠 Repo-Chat: Privacy-First Local RAG Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-0.3-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Ollama](https://img.shields.io/badge/Model-Llama3-orange?style=for-the-badge&logo=meta&logoColor=white)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?style=for-the-badge&logo=streamlit&logoColor=white)
![ChromaDB](https://img.shields.io/badge/VectorDB-Chroma-purple?style=for-the-badge)

<br>

**Kendi bilgisayarınızda çalışan, internet gerektirmeyen ve kodlarınızı analiz eden kişisel Yapay Zeka Asistanınız.**

[Kurulum](#-kurulum) • [Kullanım](#-kullanım) • [Mimari](#-mimari-ve-çalışma-mantığı) • [Katkıda Bulunma](#-katkıda-bulunma)

</div>

---

## 📖 Proje Hakkında

**Repo-Chat**, GitHub üzerindeki herhangi bir kod tabanını (repository) indirip analiz eden ve **Yerel Yapay Zeka (Local LLM)** kullanarak bu kodlarla sohbet etmenizi sağlayan bir **RAG (Retrieval-Augmented Generation)** uygulamasıdır.

Bu proje, **veri gizliliğini** en üst düzeyde tutar. Kodlarınız 3. parti sunuculara (OpenAI, Claude vb.) gönderilmez; her şey kendi bilgisayarınızda, **RTX GPU gücüyle** işlenir.

### ✨ Temel Özellikler

* 🔒 **%100 Gizlilik:** Verileriniz ve kodlarınız lokal makinenizi asla terk etmez.
* 🧠 **Llama 3 Gücü:** Meta'nın en gelişmiş açık kaynak modeli ile zeki ve bağlamı anlayan cevaplar.
* ⚡ **Vektör Arama:** **ChromaDB** ve **HuggingFace Embeddings** ile kodlar arasında anlamsal arama.
* 🎨 **Modern UI:** **Streamlit** ile geliştirilmiş, özelleştirilebilir ve kullanıcı dostu arayüz.

---

## 📂 Proje Yapısı

```bash
repo-chat/
├── 📂 chroma_db/          # Vektör veritabanı (Git-ignored)
├── 📂 downloaded_repo/    # Analiz edilen repo (Git-ignored)
├── 📂 .streamlit/         # Arayüz tema ayarları
│   └── config.toml
├── app.py                 # Ana Streamlit uygulaması (Chat Arayüzü)
├── ingest.py              # Veri işleme ve veritabanı oluşturma scripti
├── requirements.txt       # Proje bağımlılıkları
└── README.md              # Dokümantasyon





🛠 Kurulum
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin.

1. Gereksinimler
Python 3.9 veya üzeri

Git

Ollama (Modeli çalıştırmak için gereklidir. İndir)

2. Kurulum Adımları
Bash

# 1. Repoyu klonlayın
git clone [https://github.com/talh4kaya/repo-chat.git](https://github.com/talh4kaya/repo-chat.git)
cd repo-chat

# 2. Sanal ortam oluşturun
python -m venv venv

# 3. Sanal ortamı aktif edin
# Windows için:
.\venv\Scripts\activate
# Mac/Linux için:
# source venv/bin/activate

# 4. Kütüphaneleri yükleyin
pip install -r requirements.txt
3. Modelin Hazırlanması
Terminalde aşağıdaki komutu çalıştırarak Llama 3 modelini indirin:

Bash

ollama run llama3
🚀 Kullanım
Adım 1: Kodları Hafızaya At (Ingestion)
Analiz etmek istediğiniz GitHub reposunu ingest.py dosyası içindeki REPO_URL değişkenine yazın ve çalıştırın:

Bash

python ingest.py
(Bu işlem kodları indirir, parçalar, vektörlere çevirir ve ChromaDB veritabanına kaydeder).

Adım 2: Asistanı Başlat
Veritabanı oluştuktan sonra arayüzü başlatın:

Bash

streamlit run app.py
Tarayıcınızda açılan ekrandan kodlarınızla konuşmaya başlayabilirsiniz! 🎉

🏗 Mimari ve Çalışma Mantığı
Bu proje RAG (Retrieval-Augmented Generation) mimarisini kullanır. Veri akışı aşağıdaki gibidir:

Ingestion (Yutma): gitpython ile repo indirilir.

Splitting (Parçalama): Kod dosyaları RecursiveCharacterTextSplitter ile anlamlı parçalara bölünür.

Embedding (Gömme): Her parça HuggingFaceEmbeddings ile sayısal vektörlere dönüştürülür.

Vector Store (Hafıza): Vektörler ChromaDB içinde saklanır.

Retrieval & Chat: Kullanıcı sorusu ile en alakalı kod parçaları bulunur ve Llama 3 modeline gönderilir.

📊 Akış Şeması

graph TD;
    A[GitHub Repo] -->|Clone| B(Kod Dosyaları);
    B -->|Split| C(Kod Parçacıkları);
    C -->|Embedding| D[(ChromaDB Vektör Veritabanı)];
    E[Kullanıcı Sorusu] -->|Search| D;
    D -->|Alakalı Kodlar| F[Llama 3 LLM];
    F -->|Cevap| G[Streamlit Arayüz];
    style D fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#bbf,stroke:#333,stroke-width:2px


🤝 Katkıda Bulunma
Bu proje açık kaynaklıdır. Önerilerinizi ve hata bildirimlerinizi Issue açarak veya Pull Request göndererek iletebilirsiniz.

📜 Lisans
Bu proje MIT License altında lisanslanmıştır.

<p align="center"> Developed with ❤️ by <strong>Talha Kaya</strong> </p>