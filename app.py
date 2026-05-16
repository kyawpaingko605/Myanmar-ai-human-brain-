import gradio as gr
import json
import os
import requests
from difflib import get_close_matches

# 🌐 GitHub RAW KB (CHANGE THIS)
KB_URL = "https://raw.githubusercontent.com/YOURNAME/Myanmar-ai-human-brain/main/kb.json"

MEM_FILE = "memory.json"

# ---------------- LOAD ONLINE KB ----------------
def load_online_kb():
    try:
        return requests.get(KB_URL, timeout=5).json()
    except:
        return []

# ---------------- LOAD LOCAL MEMORY ----------------
def load_memory():
    if os.path.exists(MEM_FILE):
        try:
            with open(MEM_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

# ---------------- SAVE MEMORY ----------------
def save_memory(data):
    with open(MEM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# ---------------- SMART SEARCH ----------------
def search(msg, kb):
    if not kb:
        return None

    questions = [i["q"] for i in kb]

    match = get_close_matches(msg, questions, n=1, cutoff=0.5)

    if match:
        for i in kb:
            if i["q"] == match[0]:
                return i["a"]

    return None

# ---------------- BRAIN CORE ----------------
def brain(message):

    local = load_memory()
    online = load_online_kb()

    # 1. local memory first
    ans = search(message, local)
    if ans:
        return "🧠 Memory: " + ans

    # 2. online KB second
    ans2 = search(message, online)
    if ans2:
        return "🌐 Online: " + ans2

    # 3. unknown
    return "❓ မသိသေးပါ။ သင်: မေးခွန်း => အဖြေ လို့သင်ပေးပါ"

# ---------------- LEARN SYSTEM ----------------
def learn(text):

    if text.startswith("သင်:"):
        try:
            q, a = text.replace("သင်:", "").split("=>")

            data = load_memory()
            data.append({"q": q.strip(), "a": a.strip()})

            save_memory(data)

            return "✅ မှတ်ပြီး: " + q

        except:
            pass

    return "Format 👉 သင်: က => က - အက္ခရာ"

# ---------------- CHAT FUNCTION ----------------
def chat(message, history):

    reply = brain(message)

    # IMPORTANT: messages format (no crash)
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})

    return "", history

# ---------------- UI ----------------
with gr.Blocks() as app:

    gr.Markdown("# 🧠 Myanmar AI Human Brain (GitHub + HF Ready)")

    chatbot = gr.Chatbot(type="messages")

    msg = gr.Textbox(placeholder="မြန်မာစာရေးပါ...")

    send = gr.Button("Send")

    msg.submit(chat, [msg, chatbot], [msg, chatbot])
    send.click(chat, [msg, chatbot], [msg, chatbot])

    gr.Markdown("## 📚 Teach AI")

    learn_box = gr.Textbox(placeholder="သင်: က => က - အက္ခရာ")

    learn_box.submit(learn, learn_box, learn_box)

app.launch()
