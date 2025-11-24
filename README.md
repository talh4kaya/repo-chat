# Repo-Chat 🚀  
### Privacy-First Local RAG Assistant for Your Code Repositories

**Repo-Chat**, GitHub üzerindeki herhangi bir kod deposunu indirip analiz eden, ardından yerel bir LLM (Large Language Model) ile bu kodlar üzerinde sohbet etmeni sağlayan bir **lokal RAG sistemi**dir.  
Tüm işlemler cihazında yapılır — **kodların asla bulut sunucularına gönderilmez**.

---

## 🌟 Özellikler

- 🔒 **%100 Gizlilik** — Kodlar hiçbir zaman cihazdan dışarı çıkmaz  
- 🤖 **LLM Desteği** — Llama 3 gibi güçlü açık kaynak modellerle çalışma  
- 🧠 **Anlamsal Arama** — HuggingFace Embeddings + ChromaDB ile vektör tabanlı kod araması  
- 💬 **Modern Arayüz** — Streamlit tabanlı şık chat arayüzü  
- ⚡ **Hızlı & Hafif** — Küçük kod tabanlarında anında, büyük kod tabanlarında optimize edilmiş işleme

---

## 📁 Proje Yapısı

```
repo-chat/
├── chroma_db/              # Vektör veritabanı (git-ignore’da)
├── downloaded_repo/        # Analiz edilen repo (git-ignore’da)
├── .streamlit/
│   └── config.toml         # Tema ayarları
├── app.py                  # Ana Streamlit sohbet arayüzü
├── ingest.py               # Kod indirme + işleme + embedding oluşturma
├── requirements.txt        # Bağımlılıklar
└── README.md               # Dokümantasyon
```

---

## 🛠️ Kurulum

### 1️⃣ Gereksinimler  
- Python 3.9+  
- Git  
- [Ollama](https://ollama.com/) (Llama 3 veya benzeri modeller için)

### 2️⃣ Projeyi Klonla

```bash
git clone https://github.com/talh4kaya/repo-chat.git
cd repo-chat
```

### 3️⃣ Sanal ortam oluştur ve bağımlılıkları yükle

```bash
python -m venv venv

# Windows
.env\Scriptsctivate  

# Mac/Linux
source venv/bin/activate  

pip install -r requirements.txt
```

### 4️⃣ Ollama modelini çalıştır

```bash
ollama run llama3
```

---

## 💬 Kullanım

### 1️⃣ Analiz etmek istediğin repo’yu içe aktar

`ingest.py` içindeki `REPO_URL` değişkenini düzenle:

```python
REPO_URL = "https://github.com/kullanici/proje-adi"
```

Ardından çalıştır:

```bash
python ingest.py
```

Bu işlem:

- Repo’yu indirir  
- Kodları parçalar  
- Embedding’leri oluşturur  
- ChromaDB’ye kaydeder  

### 2️⃣ Chat arayüzünü başlat

```bash
streamlit run app.py
```

Tarayıcı açıldığında kodlarla sohbet etmeye başlayabilirsin.

---

## 🧠 Mimari

- **Model:** Llama 3 (Ollama üzerinden)  
- **Embedding:** HuggingFace  
- **Vektör DB:** ChromaDB  
- **Arayüz:** Streamlit  
- **Pipeline:**  
  1. Repo indir  
  2. Kod parçala  
  3. Embedding üret  
  4. Sorgu → en yakın chunk → LLM’e gönder → yanıt üret  

---

## 🔭 Roadmap

- Çoklu model desteği (Gemma, Phi-3, Mistral vb.)
- Daha gelişmiş UI
- Token optimizasyonu
- Kod üzerinde özetleme ve refaktör önerileri
- Çoklu repo desteği

---

## 🤝 Katkıda Bulunma

1. Issue açabilir  
2. Fork → Branch → PR sürecini takip edebilirsin  
3. Ek özellikler ve hata düzeltmeleri memnuniyetle karşılanır

---

## 📜 Lisans

Bu proje MIT Lisansı ile sunulmaktadır.

---

## 👤 İletişim

**Geliştirici:** Talha Kaya  
GitHub: https://github.com/talh4kaya  

---

Teşekkürler! Repo-Chat’i geliştirmeye devam ediyorum.  
Her türlü katkı ve öneriye açığım. 🚀
