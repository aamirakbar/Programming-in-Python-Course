# Define a dictionary of predefined responses
responses = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm here to help!",
    "bye": "Goodbye! Have a great day!",
    "tell me a joke": "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!",
    "tell me a fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "what is your favorite color": "I'm just a bunch of code, so I don't have a favorite color, but I think rainbow colors are pretty cool!",
}

# Main chat loop
print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    
    input_text = user_input.lower()  # Convert input to lowercase for case insensitivity
    
    if input_text in responses:
        response = responses[input_text]
    else:
        response = "I'm sorry, I don't understand that."
        
    print("Chatbot:", response)
