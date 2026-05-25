# ==========================================
# SEARCH ENGINE MODULE
# ==========================================

from rapidfuzz import fuzz

# ==========================================
# SEARCH SUGGESTIONS DATABASE
# ==========================================

SEARCH_SUGGESTIONS = [

    # APPS
    "open chrome",
    "open notepad",
    "open calculator",
    "open camera",
    "open vscode",
    "open spotify",
    "open discord",
    "open whatsapp",
    "open file explorer",
    "open task manager",
    "open settings",
    "open paint",
    "open word",
    "open excel",

    # MEDIA
    "play music",
    "play lofi",
    "play youtube",
    "play netflix",
    "play spotify",

    # SEARCH
    "search python",
    "search ai",
    "search weather",
    "search news",
    "search google",

    # ACTIONS
    "write in notepad",
    "take screenshot",
    "shutdown",
    "restart",
    "lock screen",
    "set volume",
    "open vscode",
]

# ==========================================
# NORMALIZE TEXT
# ==========================================

def normalize(text):

    text = text.lower().strip()

    while "  " in text:
        text = text.replace("  ", " ")

    return text

# ==========================================
# SUGGESTION ENGINE
# ==========================================

def suggest_commands(user_input):

    user_input = normalize(user_input)

    if user_input == "":
        return []

    prefix_matches = []
    fuzzy_matches = []

    for item in SEARCH_SUGGESTIONS:

        # PREFIX MATCH — highest priority
        if item.startswith(user_input):
            prefix_matches.append(item)

        # FUZZY MATCH — use both methods, pick the best score
        else:
            score = max(
                fuzz.partial_ratio(user_input, item),
                fuzz.token_sort_ratio(user_input, item)
            )

            if score > 65:
                fuzzy_matches.append((score, item))

    # Sort fuzzy matches by score descending
    fuzzy_matches.sort(reverse=True)
    ranked_fuzzy = [item for score, item in fuzzy_matches]

    # Prefix matches come first, then fuzzy
    return (prefix_matches + ranked_fuzzy)[:5]
