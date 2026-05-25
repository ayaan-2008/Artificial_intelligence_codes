import spacy
import subprocess
import webbrowser
import requests

# =========================================
# LOAD NLP MODEL
# =========================================

nlp = spacy.load("en_core_web_sm")

# =========================================
# DESKTOP APPS
# =========================================

APPS = {

    "calculator": "calc.exe",
    "calc": "calc.exe",
    "camera": "microsoft.windows.camera",
    "notepad": "notepad.exe",

    "paint": "mspaint.exe",
    "mspaint": "mspaint.exe",

    "vs code": r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe",

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe"
}

# =========================================
# WEBSITES
# =========================================

WEBSITES = {

    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "github": "https://github.com",
    "spotify": "https://spotify.com",
    "chatgpt": "https://chat.openai.com"
}

# =========================================
# INTENTS
# =========================================

INTENTS = {

    "open": [
        "open",
        "launch",
        "start",
        "run"
    ],

    "search": [
        "search",
        "find",
        "look for"
    ],

    "weather": [
        "weather",
        "temperature",
        "forecast",
        "climate"
    ],

    "describe": [

        "describe",

        "what is",
        "who is",

        "tell me about",

        "information about",

        "explain"
    ],
    "greeting": [

    "hello",
    "hi",
    "hey",

    "good morning",
    "good afternoon",
    "good evening",

    "how are you"
],
}

# =========================================
# SMART INTENT DETECTION
# =========================================

def detect_intent(text):

    text = text.lower()

    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            # phrase matching
            if keyword in text:

                return intent

    return "unknown"

# =========================================
# SPLIT MULTIPLE COMMANDS
# =========================================

def split_commands(text):

    separators = [
        " and then ",
        " then ",
        " and "
    ]

    commands = [text]

    for sep in separators:

        temp = []

        for cmd in commands:

            parts = cmd.split(sep)

            temp.extend(parts)

        commands = temp

    return [cmd.strip() for cmd in commands if cmd.strip()]

# =========================================
# EXTRACT TARGET
# =========================================

def extract_target(text):

    text = text.lower()

    filler_words = [

        "open",
        "launch",
        "start",
        "run",
        "please",
        "can",
        "you",
        "the",
        "app",
        "website"
    ]

    words = text.split()

    filtered = []

    for word in words:

        if word not in filler_words:

            filtered.append(word)

    return " ".join(filtered)

# =========================================
# EXTRACT CITY
# =========================================

def extract_city(text):

    doc = nlp(text)

    # Use Named Entity Recognition
    for ent in doc.ents:

        if ent.label_ == "GPE":

            return ent.text

    # Backup manual detection
    words = text.lower().split()

    if "in" in words:

        index = words.index("in")

        if index + 1 < len(words):

            return words[index + 1]

    return None
# =========================================
# KNOWLEDGE ENGINE
# =========================================
import wikipediaapi

wiki = wikipediaapi.Wikipedia(

    language='en',
    user_agent='AIAssistantBot/1.0'
)
def describe_topic(text):

    try:

        query = text.lower()

        remove_phrases = [

            "describe",
            "what is",
            "who is",

            "tell me about",

            "information about",

            "explain"
        ]

        for phrase in remove_phrases:

            query = query.replace(phrase, "")

        query = query.strip()

        query = query.title()

        print(f"\nSearching Wikipedia for: {query}")

        page = wiki.page(query)

        if page.exists():

            summary = page.summary[:700]

            print("\n" + summary)

        else:

            print("\nNo Wikipedia page found.")

    except Exception as e:

        print("\nWikipedia Error:", e)
# =========================================
# GREETING ENGINE
# =========================================

def respond_greeting(text):

    text = text.lower()

    if "how are you" in text:

        print("\nI'm functioning properly and ready to help.")

    elif "morning" in text:

        print("\nGood morning!")

    elif "afternoon" in text:

        print("\nGood afternoon!")

    elif "evening" in text:

        print("\nGood evening!")

    else:

        print("\nHello! How can I help you?")
# =========================================
# OPEN DESKTOP APPS
# =========================================

def open_app(target):

    for app_name, app_path in APPS.items():

        if app_name in target:

            try:

                subprocess.Popen(app_path)

                print(f"Opened app: {app_name}")

                return True

            except Exception as e:

                print("App error:", e)

                return True

    return False

# =========================================
# OPEN WEBSITES
# =========================================

def open_website(target):

    for site_name, site_url in WEBSITES.items():

        if site_name in target:

            webbrowser.open(site_url)

            print(f"Opened website: {site_name}")

            return True

    # Dynamic website opening
    try:

        target = target.replace(" ", "")

        url = f"https://{target}.com"

        webbrowser.open(url)

        print(f"Opened dynamic website: {url}")

        return True

    except:

        return False

# =========================================
# GOOGLE SEARCH
# =========================================

def google_search(query):

    query = query.replace("search", "")
    query = query.replace("find", "")
    query = query.replace("look for", "")

    query = query.strip()

    url = f"https://www.google.com/search?q={query}"

    webbrowser.open(url)

    print(f"Searching Google for: {query}")

# =========================================
# WEATHER SYSTEM
# =========================================

def get_weather(city=None):

    try:

        if city:

            city = city.replace(" ", "+")

            url = f"https://wttr.in/{city}?format=3"

        else:

            url = "https://wttr.in/?format=3"

        response = requests.get(url)

        if response.status_code == 200:

            print("\n" + response.text)

        else:

            print("Could not fetch weather.")

    except Exception as e:

        print("Weather error:", e)

# =========================================
# EXECUTION ENGINE
# =========================================

def execute(command):

    intent = detect_intent(command)

    target = extract_target(command)

    print("\n====================")
    print("COMMAND :", command)
    print("INTENT  :", intent)
    print("TARGET  :", target)
    print("====================")
    

    # -------------------------------------
    # OPEN COMMAND
    # -------------------------------------

    if intent == "open":

        opened = open_app(target)

        if not opened:

            opened = open_website(target)

        if not opened:

            print("Could not open target.")
    
    # -------------------------------------
    # GREETING
    # -------------------------------------

    elif intent == "greeting":

        respond_greeting(command)
    # -------------------------------------
    # SEARCH COMMAND
    # -------------------------------------

    elif intent == "search":

        google_search(command)

    # -------------------------------------
    # WEATHER COMMAND
    # -------------------------------------

    elif intent == "weather":

        city = extract_city(command)

        print("Detected City:", city)

        get_weather(city)
    
        # -------------------------------------
    # DESCRIPTION / KNOWLEDGE
    # -------------------------------------

    elif intent == "describe":

        describe_topic(command)

    # -------------------------------------
    # UNKNOWN COMMAND
    # -------------------------------------

    else:

        print("Command not understood.")

# =========================================
# MAIN LOOP
# =========================================

print("\nAI Assistant Started")
print("Type 'exit' to quit")

while True:

    user = input("\nYou: ")

    if user.lower() == "exit":

        print("Goodbye!")

        break

    commands = split_commands(user)

    print("\nDetected Commands:")

    for i, cmd in enumerate(commands, 1):

        print(f"{i}. {cmd}")

    for cmd in commands:

        execute(cmd)