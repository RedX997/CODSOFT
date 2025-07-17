import random

rules = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey!", "Nice to meet you!"]
    },
    "goodbye": {
        "patterns": ["bye", "see you", "goodbye", "take care"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thank you so much"],
        "responses": ["You're welcome!", "Glad to help!", "No problem!"]
    },
    "name": {
        "patterns": ["what is your name", "who are you", "tell me your name"],
        "responses": ["I'm a chatbot created by GPT!", "You can call me RuleBot."]
    },
    "help": {
        "patterns": ["help", "i need help", "can you help me"],
        "responses": ["Of course, how can I assist you?", "Sure, tell me your problem."]
    }
}

def get_response(user_input):
    user_input = user_input.lower()
    
    for intent, data in rules.items():
        for pattern in data["patterns"]:
            if pattern in user_input:
                return random.choice(data["responses"])
    
    return "Sorry, I didn't understand that."

def chat():
    print("RuleBot: Hello! Type 'bye' to exit.")
    
    while True:
        user_input = input(" You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("RuleBot: Goodbye! Have a great day! 👋")
            break
        response = get_response(user_input)
        print("RuleBot:", response)

if __name__ == "__main__":
    chat()
