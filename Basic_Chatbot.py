# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey", "hy"]:
        return "Hi!"
    
    
    elif user_input in ["how are you", "how are you doing", "how r you", "what's up"]:
        return "I'm fine, thanks! How can I help you?"
    
    
    elif user_input in ["what is your name", "who are you", "your name"]:
        return "I am a simple chatbot."
    
    
    elif user_input in ["help", "what can you do", "options"]:
        return "You can say: hello, how are you, bye"
    
    
    elif user_input in ["thanks", "thank you", "thx"]:
        return "You're welcome!"
    
    
    elif user_input in ["bye", "goodbye", "see you", "exit"]:
        return "Goodbye!"
    

    elif user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."


print("Chatbot is running... (type 'bye' to exit)")

while True:
    user = input("You: ")
    reply = chatbot_response(user)
    print("Bot:", reply)

    if user.lower().strip() == "bye":
        break