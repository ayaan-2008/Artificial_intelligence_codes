# 🤖 Advanced AI Desktop Assistant

An intelligent AI-powered desktop assistant built with Python that can:

- Open desktop applications
- Perform smart web searches
- Take screenshots
- Write automatically in Notepad
- Interact conversationally using AI
- Execute system commands
- Search YouTube
- Detect fuzzy command matches
- Maintain short-term conversation memory

---

# 🚀 Features

## 🧠 AI Conversation
Uses the Groq API with LLaMA models for:
- Natural conversation
- Question answering
- Smart responses
- Context memory

---

## 💻 Desktop Automation

The assistant can:

- Open Chrome
- Open Notepad
- Open Calculator
- Open Camera
- Open File Explorer
- Open Task Manager
- Open Settings
- Lock Screen
- Shutdown PC
- Restart PC

---

## 📸 Screenshot Support

Take screenshots instantly using voice/text-like commands.

Example:
```bash
take screenshot
```

---

## ✍️ Automatic Typing in Notepad

Example:
```bash
write hello world in notepad
```

The assistant automatically opens Notepad and types the text.

---

## 🔎 Smart Search System

- AI answers first
- Then web search opens automatically
- Uses DuckDuckGo API + Google Search

Example:
```bash
search latest AI news
```

---

## 🎬 YouTube Search

Example:
```bash
play interstellar trailer
```

Automatically opens YouTube search results.

---

## 🎯 Fuzzy Command Recognition

Even typo commands work.

Examples:
```bash
helo
opn chrom
calcultor
```

Uses RapidFuzz for intelligent matching.

---

# 🛠️ Technologies Used

- Python
- Groq API
- LLaMA 3.3 70B
- RapidFuzz
- PyAutoGUI
- Requests

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

---

## 2️⃣ Navigate Into Folder

```bash
cd YOUR_REPO
```

---

## 3️⃣ Create Virtual Environment

### Windows
```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

OR manually:

```bash
pip install groq rapidfuzz pyautogui requests
```

---

# 🔑 Groq API Setup

This project requires a Groq API key.

⚠️ IMPORTANT:
The API key is NOT included in this project.

Each user must create their own API key.

Get your API key from:

https://console.groq.com/keys

Then replace this line:

```python
GROQ_API_KEY = "YOUR_API_KEY_HERE"
```

with:

```python
GROQ_API_KEY = "your_actual_api_key"
```

---

# ▶️ Run The Assistant

```bash
python main.py
```

---

# 💬 Example Commands

## Open Applications

```bash
open chrome
open notepad
calculator
camera
```

---

## AI Conversation

```bash
how are you
what can you do
tell me about AI
```

---

## Web Search

```bash
search quantum computing
google latest space news
```

---

## YouTube Search

```bash
play lo-fi music
youtube python tutorial
```

---

## Screenshot

```bash
take screenshot
```

---

## Notepad Automation

```bash
write hello world in notepad
```

---

# 📁 Project Structure

```bash
project/
│
├── main.py
├── search_engine.py
├── requirements.txt
└── README.md
```

---

# ⚡ Future Improvements

- Voice Recognition
- Speech Output
- AI Vision
- Local LLM Support
- Smart File Handling
- Task Scheduling
- System Monitoring
- GUI Interface

---

# 🧠 AI Model Used

Model:
```bash
llama-3.3-70b-versatile
```

Provided by:
Groq API

---

# ⚠️ Disclaimer

This project performs desktop automation commands on your system.

Use responsibly.

---

# 👨‍💻 Author

Developed by Abdul Ayaan

---

# ⭐ Support

If you like this project:
- Star the repository
- Fork the project
- Improve and contribute

---