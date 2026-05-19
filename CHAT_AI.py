import os
import webbrowser
import time

while True: #runs loop forever till the session expires

    message = input("You: ").lower()  # this where your message is stored

    if "hello" in message:  # reads hello
        print("Bot: Hi!")
    
    elif "youtube" in message: # opens youtube
         print("Bot: Opening YouTube...")
         webbrowser.open("https://youtube.com")

    elif "google" in message: # opens google
         print("Bot: Opening Google...")
         webbrowser.open("https://www.google.com")

    elif "chatgpt" in message: # opens chatgpt
         print("Bot: Opening ChatGPT...")
         webbrowser.open("https://chatgpt.com")
         
    elif "calc" in message: # opens calculator
        print("opening calculator...")
        os.system("start calc")

    elif "notepad" in message: # opens notepad
        print("Bot: Opening Notepad...")
        os.system("start notepad")
 
    elif "paint" in message: # opens mspaint

        print("Bot: Opening Paint...")

        os.system("start mspaint")

    elif "vs code" in message: # opens visual studio code

        print("Bot: Opening VS Code...")

        os.system("code")

    elif "weather" in message: # gives the weather report by taking city input

        city = input("Enter city name: ")

        webbrowser.open(
        f"https://www.google.com/search?q=weather+{city}"
        )

        print(f"Bot: Showing weather for {city}")

    elif "search" in message: # search a query in google

        query = message.replace("search", "")

        webbrowser.open(
        f"https://www.google.com/search?q={query}"
        )

        print("Bot: Searching on Google...")

    elif "time" in message: # gives the current time and date
        print("the time is:",time.ctime())
    
    elif "ai" in message:  # speaks on ai
        print("Bot: AI means Artificial Intelligence.")

    elif "python" in message: # speaks on python
        print("Bot: Python is a programming language.")

    elif "bye" in message: # goodbye message this is where it breaks out of the loop
        print("Bot: Goodbye!")
        break

    else: # execuites this statement when nothing matches
        print("Bot: I don't understand.")