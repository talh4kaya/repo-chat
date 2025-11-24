from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
import time

# 1. MODELİ BAĞLA
print("🔌 Ollama'ya bağlanılıyor...")
# 'llama3' modelini kullanacağız. Sıcaklığı (temperature) 0.7 yaptık ki biraz yaratıcı olsun.
llm = ChatOllama(model="llama3", temperature=0.7)

# 2. SORUYU HAZIRLA
soru = "Yazılım mühendisliğinde 'Bug' (Böcek) teriminin tarihçesini 2 cümleyle anlat."
messages = [HumanMessage(content=soru)]

print(f"🤖 Soru Soruluyor: {soru}")
print("⏳ Düşünüyor (Local GPU)...")

# 3. CEVABI AL
start_time = time.time()
response = llm.invoke(messages)
end_time = time.time()

# 4. SONUCU YAZDIR
print("-" * 50)
print(f"💬 CEVAP:\n{response.content}")
print("-" * 50)
print(f"⚡ Süre: {end_time - start_time:.2f} saniye")