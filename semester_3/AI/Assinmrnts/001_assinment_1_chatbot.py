def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help?"
    elif "your name" in user_input:
        return "I am a rule-based chatbot!"
    elif "how are you" in user_input:
        return "Just a program, thanks for asking!"
    elif "thank" in user_input:
        return "You are welcome!"
    # Assingment to add 5 more rules
    elif "help" in user_input:
        return "i can answer simple question based on rules."
    elif "python" in user_input:
        return "Python is a computer language"
    elif "thanks" in user_input:
        return "Your welcome"
    elif "creater" in user_input:
        return "Noman Jatala"
    elif "bye" in user_input:
        return "Good bye"
    else:
        return "Sorry, I did not understand."
print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Bye!")
        break
    print("Chatbot:", chatbot_response(user_input))