# ==========================================
# AI DESKTOP ASSISTANT — MAIN FILE
# ==========================================

import os
import time
import subprocess
import webbrowser
import requests
import pyautogui

from groq import Groq
from search_engine import suggest_commands, normalize

print("=" * 60)
print("         ADVANCED AI DESKTOP ASSISTANT")
print("=" * 60)

# ==========================================
# APPLICATION PATHS
# ==========================================

apps = {
    "chrome":       "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad":      "notepad.exe",
    "calculator":   "calc.exe",
    "vscode":       "C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "spotify":      "C:\\Users\\%USERNAME%\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "discord":      "C:\\Users\\%USERNAME%\\AppData\\Local\\Discord\\Update.exe",
}

# ==========================================
# GROQ CLIENT SETUP
# ==========================================

GROQ_API_KEY = "YOUR_API_KEY_HERE"   # <---paste your api key here from groq 
groq_client   = Groq(api_key=GROQ_API_KEY)

# Stores conversation history for memory across turns
conversation_history = []

# ==========================================
# AI RESPONSE (GROQ)
# ==========================================

def ask_ai(prompt):

    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    # Keep only the last 6 messages (3 exchanges) to stay within limits
    recent_history = conversation_history[-6:]

    try:
        response = groq_client.chat.completions.create(
           model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a smart desktop AI assistant. "
                        "Give short, helpful, and accurate responses."
                    )
                },
                *recent_history
            ]
        )

        reply = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content": reply
        })

        print("\n=== AI RESPONSE ===\n")
        print(reply)

    except Exception as e:
        print("\nAI ERROR:", e)

# ==========================================
# SMART WEB SEARCH (DUCKDUCKGO)
# ==========================================

def smart_search(query):

    try:
        print(f"\nSearching web for: {query}\n")

        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        response = requests.get(url, timeout=5).json()
        answer = response.get("Abstract")

        if answer:
            print("=== RESULT ===\n")
            print(answer)
        else:
            print("No direct answer found. Opening Google...\n")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    except Exception as e:
        print("Search failed:", e)

# ==========================================
# WRITE IN NOTEPAD
# ==========================================

def write_in_notepad(text):

    subprocess.Popen(["notepad.exe"])
    time.sleep(1.5)
    pyautogui.write(text, interval=0.03)

# ==========================================
# TAKE SCREENSHOT
# ==========================================

def take_screenshot():

    screenshot = pyautogui.screenshot()
    path = os.path.join(os.path.expanduser("~"), "Desktop", "screenshot.png")
    screenshot.save(path)
    print(f"\nScreenshot saved to: {path}\n")

# ==========================================
# COMMAND ACTION FUNCTIONS
# ==========================================

def open_chrome():
    print("\nOpening Chrome...\n")
    os.startfile(apps["chrome"])

def open_notepad():
    print("\nOpening Notepad...\n")
    os.system("notepad")

def open_calculator():
    print("\nOpening Calculator...\n")
    os.system("calc")

def open_camera():
    print("\nOpening Camera...\n")
    os.system("start microsoft.windows.camera:")

def open_file_explorer():
    print("\nOpening File Explorer...\n")
    os.system("explorer")

def open_task_manager():
    print("\nOpening Task Manager...\n")
    os.system("taskmgr")

def open_settings():
    print("\nOpening Settings...\n")
    os.system("start ms-settings:")

def lock_screen():
    print("\nLocking Screen...\n")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def shutdown():
    print("\nShutting down in 10 seconds... Type 'cancel' to abort.\n")
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        os.system("shutdown /s /t 10")
    else:
        print("Shutdown cancelled.\n")

def restart():
    print("\nRestarting in 10 seconds...\n")
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        os.system("shutdown /r /t 10")
    else:
        print("Restart cancelled.\n")

def greet():
    print("\nHello! How can I help you today?\n")

# ==========================================
# COMMANDS DATABASE
# ==========================================

COMMANDS = {

    "open chrome": {
        "keywords": ["chrome", "browser", "google chrome", "open browser"],
        "action": open_chrome
    },

    "open notepad": {
        "keywords": ["notepad", "text editor", "notes"],
        "action": open_notepad
    },

    "calculator": {
        "keywords": ["calculator", "calc", "math"],
        "action": open_calculator
    },

    "camera": {
        "keywords": ["camera", "webcam", "photo"],
        "action": open_camera
    },

    "file explorer": {
        "keywords": ["file explorer", "files", "explorer", "my files"],
        "action": open_file_explorer
    },

    "task manager": {
        "keywords": ["task manager", "tasks", "processes"],
        "action": open_task_manager
    },

    "settings": {
        "keywords": ["settings", "preferences", "control panel"],
        "action": open_settings
    },

    "lock screen": {
        "keywords": ["lock", "lock screen", "lock computer"],
        "action": lock_screen
    },

    "shutdown": {
        "keywords": ["shutdown", "shut down", "turn off", "power off"],
        "action": shutdown
    },

    "restart": {
        "keywords": ["restart", "reboot", "reset pc"],
        "action": restart
    },

    "screenshot": {
        "keywords": ["screenshot","take ss", "screen capture", "capture screen"],
        "action": take_screenshot
    },

    "greeting": {
        "keywords": ["hi", "hello", "hey", "helo", "hii"],
        "action": greet
    }
}

# ==========================================
# FUZZY COMMAND MATCHER
# ==========================================

from rapidfuzz import fuzz

def find_best_match(user_input):

    best_score   = 0
    best_command = None

    user_input = normalize(user_input)

    for command_name, data in COMMANDS.items():
        for keyword in data["keywords"]:

            score = max(
                fuzz.partial_ratio(user_input, keyword),
                fuzz.token_sort_ratio(user_input, keyword)
            )

            if score > best_score:
                best_score   = score
                best_command = command_name

    # Only return if BOTH methods agree it's a strong match
    if best_score > 85:
        return best_command, best_score
    
    return None, 0

# ==========================================
# CONVERSATION DETECTOR
# ==========================================

def is_conversation(text):

    conversations = [
        "how are you",
        "what are you doing",
        "who are you",
        "are you okay",
        "good morning",
        "good night",
        "thank you",
        "thanks",
        "bye",
        "what can you do",
        "help me"
    ]

    text = normalize(text)

    for phrase in conversations:
        score = fuzz.ratio(text, phrase)
        if score > 75:
            return True

    return False

# ==========================================
# MAIN COMMAND EXECUTOR
# ==========================================

def execute_command(command):

    command = normalize(command)

    # ----------------------------------------
    # YOUTUBE / VIDEO
    # ----------------------------------------
    if any(word in command for word in ["youtube", "play", "video"]):

        query = command
        for word in ["youtube", "play", "video"]:
            query = query.replace(word, "")
        query = query.strip()

        print(f"\nSearching YouTube for: {query}\n")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return

    # ----------------------------------------
    # SCREENSHOT
    # ----------------------------------------
    if "screenshot" in command or "capture screen" in command:
        take_screenshot()
        return

    # ----------------------------------------
    # WRITE IN NOTEPAD
    # ----------------------------------------
    if "write" in command:

        text = (
            command
            .replace("write", "")
            .replace("in notepad", "")
            .strip()
        )
        write_in_notepad(text)
        return

    # ----------------------------------------
    # GOOGLE SEARCH — AI answers first, then web
    # ----------------------------------------
    if "search" in command or "google" in command:

        query = command.replace("search", "").replace("google", "").strip()

        # Step 1 — AI answers first
        print(f"\nLet me answer that for you...\n")
        ask_ai(query)

        # Step 2 — delay then open web
        time.sleep(2)
        print(f"\nAlso opening Google for more results...\n")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return
    # ----------------------------------------
    # NORMAL CONVERSATION → GROQ AI
    # ----------------------------------------
    if is_conversation(command):
        ask_ai(command)
        return

    # ----------------------------------------
    # FUZZY COMMAND MATCHING
    # ----------------------------------------
    matched_command, score = find_best_match(command)

    if score > 70:
        print(f"\nMatched: {matched_command} (confidence: {score}%)\n")
        COMMANDS[matched_command]["action"]()
        return

    # ----------------------------------------
    # SHORT QUERY → AI first, then DuckDuckGo
    # ----------------------------------------
    if len(command.split()) <= 3:
        print(f"\nLet me answer that for you...\n")
        ask_ai(command)
        time.sleep(3)
        print("\nAlso searching the web...\n")
        smart_search(command)
        return

    # ----------------------------------------
    # FALLBACK → AI answers, then web search
    # ----------------------------------------
    ask_ai(command)
    time.sleep(2)
    print("\nAlso searching the web for more info...\n")
    webbrowser.open(f"https://www.google.com/search?q={command}")
# ==========================================
# MAIN LOOP
# ==========================================

while True:

    user_input = input("\nYou: ").strip()

    # Check exit FIRST before anything else
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("\nGoodbye!\n")
        break

    # Show suggestions
    suggestions = suggest_commands(user_input)
    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print(f"  - {s}")

    # Execute the command
    execute_command(user_input)
