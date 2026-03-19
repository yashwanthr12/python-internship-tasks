print("Simple Chatbot")
print("Type 'exit' to end the conversation")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you for asking.")

    elif user_input == "your name":
        print("Bot: I am a simple Python chatbot.")

    elif user_input == "help":
        print("Bot: You can ask me simple questions like hello, how are you, or my name.")

    elif user_input == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")