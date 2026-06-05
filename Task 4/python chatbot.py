#   ChatBot - Hindi & English Rule-Based Chatbot
#   Concepts: Functions, if-elif-else, while loop, Input/Output
# List of Hindi words to detect language
HINDI_WORDS = [
    'kya', 'hai', 'ho', 'hain', 'mein', 'se', 'ka', 'ki', 'ke', 'aur',
    'nahi', 'karo', 'kuch', 'yaar', 'bhai', 'dost', 'tera', 'mera',
    'tumhara', 'aapka', 'namaste', 'sunao', 'bolo', 'arre', 'lagta',
    'accha', 'theek', 'shukriya', 'dhanyawad', 'neend', 'bhook',
    'khaana', 'subah', 'raat', 'din', 'bahut', 'bilkul', 'haan',
    'phir', 'milenge', 'alvida', 'chalti', 'chalta', 'hun',
    'tum', 'aap', 'main', 'kaisa', 'kaisi', 'kaise'
]

#   STEP 1: Detect if user typed Hindi or English

def detect_language(user_input):
    """
    Returns 'hi' if Hindi words are found, else 'en' for English.
    """
    words = user_input.lower().split()
    for word in words:
        if word in HINDI_WORDS:
            return 'hi'
    return 'en'

#   STEP 2: Match input to a rule and return reply

def chatbot_response(user_input):
    """
    Matches user input to predefined rules.
    Replies in the same language the user typed in.
    """

    text = user_input.lower().strip()
    lang = detect_language(text)

    # --- Greetings ---
    if any(k in text for k in ['hello', 'hi', 'hey', 'hii']):
        if lang == 'hi':
            return "Hello dost! Kaise ho? 😊"
        else:
            return "Hello! How are you doing? 😊"

    elif any(k in text for k in ['namaste', 'namaskar', 'namste']):
        if lang == 'hi':
            return "Namaste! Swaagat hai aapka. Kya haal hai? 🙏"
        else:
            return "Namaste! Welcome. How can I help you? 🙏"

    # --- How are you ---
    elif any(k in text for k in ['how are you', 'how r u', 'how are u']):
        return "I'm doing great, thanks for asking! And you? 😊"

    elif any(k in text for k in ['kya hal hai', 'kya haal hai', 'kaise ho', 'kya chal raha']):
        return "Main bilkul mast hun! Shukriya poochne ke liye. Aur aap? 😄"

    # --- Name ---
    elif any(k in text for k in ['what is your name', 'whats your name', 'your name', 'who are you']):
        return "I'm ChatBot — a smart chatbot that understands both Hindi and English! 🤖"

    elif any(k in text for k in ['tumhara naam', 'tera naam', 'aapka naam', 'tum kaun ho']):
        return "Mera naam ChatBot hai! Tumhara Hindi-English dost chatbot. 🤖"

    # --- Jokes ---
    elif any(k in text for k in ['tell me a joke', 'joke please', 'funny', 'make me laugh']):
        return "Why don't scientists trust atoms? Because they make up everything! 😂"

    elif any(k in text for k in ['joke sunao', 'koi joke', 'hasa do', 'hasao']):
        return "Suno: Teacher ne pucha — 'Ek aur ek kitna?'\nStudent: 'Maths mein 2, English mein eleven!' 😂"

    # --- Python ---
    elif any(k in text for k in ['what is python', 'tell me about python', 'python language']):
        return "Python is an amazing programming language — simple syntax, powerful features, perfect for beginners! 🐍💻"

    elif 'python kya hai' in text:
        return "Python ek bahut achhi programming language hai — simple aur powerful, beginners ke liye best! 🐍💻"

    # --- Help ---
    elif any(k in text for k in ['help', 'what can you do']):
        return "I can chat in both Hindi and English! Ask me anything — jokes, questions, or just talk. 😊"

    elif any(k in text for k in ['help karo', 'kya kar sakte', 'kya jaante ho']):
        return "Main Hindi aur English dono mein baat kar sakta hun! Jokes bhi, sawaal bhi. 😊"

    # --- Thanks ---
    elif any(k in text for k in ['thanks', 'thank you', 'thank u', 'thankyou']):
        return "You're welcome! Always here to help. 😊"

    elif any(k in text for k in ['shukriya', 'dhanyawad', 'thanks yaar']):
        return "Koi baat nahi dost! Hamesha haazir hun. 😊"

    # --- Tired / Bored ---
    elif any(k in text for k in ['neend', 'thak gaya', 'thak gayi', 'bore ho raha']):
        return "Aw! Thoda rest lo, chai piyo. Main yahan hun! ☕"

    elif any(k in text for k in ['i am tired', 'i am bored', 'sleepy', 'bored']):
        return "Sounds like you need rest! Take a break and have some tea. ☕"

    # --- Food ---
    elif any(k in text for k in ['khana', 'khaana', 'bhook', 'bhukh']):
        return "Arre jao khaana khao! Main bot hun, mujhe bhook nahi lagti. 😄"

    elif any(k in text for k in ['hungry', 'food', 'what should i eat']):
        return "Go grab something to eat! You deserve it. 🍕😄"

    # --- Greetings (time-based) ---
    elif any(k in text for k in ['good morning', 'morning', 'gm']):
        return "Good morning! Hope you have a wonderful day. ☀️"

    elif any(k in text for k in ['good night', 'goodnight', 'gn']):
        return "Good night! Sweet dreams. 🌙"

    elif any(k in text for k in ['subah', 'suprabhat']):
        return "Suprabhat! Aaj ka din shandar ho. ☀️"

    # --- Love ---
    elif any(k in text for k in ['i love you', 'love you', 'i like you']):
        return "Aww! I like chatting with you too! 💙"

    # --- Okay / Yes / No ---
    elif any(k in text for k in ['okay', 'ok', 'alright', 'sure', 'got it']):
        return "Great! Anything else I can help with? 😊"

    elif any(k in text for k in ['accha', 'theek hai', 'haan', 'bilkul']):
        return "Bilkul! Aur kuch jaanna chahte ho? 😊"

    # --- Bye ---
    elif any(k in text for k in ['bye', 'goodbye', 'good bye', 'see you']):
        return "Goodbye! Take care and see you soon! 👋😊"

    elif any(k in text for k in ['alvida', 'phir milenge', 'chalta hun', 'chalti hun']):
        return "Alvida dost! Phir milenge, apna khayal rakhna! 👋😊"

    # --- Default fallback ---
    else:
        if lang == 'hi':
            return "Samajh gaya! Lekin is sawaal ka jawab abhi mere paas nahi hai. Kuch aur poochho? 😊"
        else:
            return "I got you! But I don't have an answer for that yet. Try asking something else? 😊"


#   STEP 3: Main loop — keep chatting until user says bye
def main():
    """
    Runs the chatbot in a loop until the user types bye/alvida.
    """
    print("=" * 50)
    print("   Welcome to ChatBot!")
    print("   Hindi mein bolo ya English mein — dono chalega!")
    print("   Type 'bye' or 'alvida' to exit.")
    print("=" * 50)

    # Keep running until user says bye
    while True:

        # Take input from user
        user_input = input("\nYou: ").strip()

        # Skip empty input
        if not user_input:
            continue

        # Get chatbot reply
        response = chatbot_response(user_input)

        # Print the reply
        print(f"ChatBot: {response}")

        # Stop if user says bye
        text = user_input.lower()
        if any(k in text for k in ['bye', 'goodbye', 'alvida', 'phir milenge']):
            break


# Run the program
if __name__ == "__main__":
    main()
