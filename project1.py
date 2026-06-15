responses={"hello":"Hello! How can I assist you today?",
           "hi":"Hello! How can I assist you today?",
           "how are you":"I'm just a program, but I'm functioning as expected! How can I help you?",
           "what is your name":"I am an AI assistant created to help you with your questions." }
userInput = input("You: ").lower().strip()
while userInput not in ["goodbye", "exit", "quit","bye"]:
    print("AI: " + responses.get(userInput, "I'm sorry, I don't understand that. Can you please rephrase?"))
    userInput = input("You: ").lower().strip()
print("AI: " + "Goodbye! Have a great day!")
