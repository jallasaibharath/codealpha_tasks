# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hi! I'm your simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there! How can I help you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot!")
        
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        elif "weather" in user_input:
            print("Chatbot: I can’t check the weather yet, but I bet it's nice outside!")
        
        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()
