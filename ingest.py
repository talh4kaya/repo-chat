import os
import shutil
from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# AYARLAR
REPO_URL = "https://github.com/talh4kaya/guardian-flow" # Senin önceki projen!
REPO_PATH = "./downloaded_repo"
DB_PATH = "./chroma_db"

def ingest_repo():
    # 1. TEMİZLİK: Önceki indirmeleri sil
    if os.path.exists(REPO_PATH):
        shutil.rmtree(REPO_PATH)
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    # 2. CLONE: Repoyu indir
    print(f"📥 Repo indiriliyor: {REPO_URL}...")
    Repo.clone_from(REPO_URL, to_path=REPO_PATH)

    # 3. LOAD: Kod dosyalarını oku
    print("📂 Kodlar okunuyor...")
    loader = GenericLoader.from_filesystem(
        REPO_PATH,
        glob="**/*",
        suffixes=[".py"], # Sadece Python dosyalarını oku (istersen .js, .java ekle)
        parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
    )
    documents = loader.load()
    print(f"   👉 Toplam {len(documents)} adet dosya bulundu.")

    # 4. SPLIT: Kodları küçük parçalara böl (Chunking)
    # AI hepsini tek lokmada yiyemez, parça parça vermeliyiz.
    print("✂️  Kodlar parçalanıyor (Chunking)...")
    text_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, 
        chunk_size=2000, 
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)
    print(f"   👉 {len(texts)} adet kod parçacığı oluşturuldu.")

    # 5. EMBED & STORE: Vektöre çevir ve kaydet
    print("🧠 Vektör veritabanı oluşturuluyor (Bu işlem GPU/CPU kullanır)...")
    
    # Yerel Embedding Modeli (İnternet gerekmez, hızlıdır)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    db = Chroma.from_documents(
        documents=texts, 
        embedding=embeddings, 
        persist_directory=DB_PATH
    )
    
    # Hafızaya kaydet
    # ChromaDB yeni sürümlerde otomatik persist eder ama garanti olsun.
    print(f"✅ Veritabanı başarıyla oluşturuldu: {DB_PATH}")

if __name__ == "__main__":
    ingest_repo()