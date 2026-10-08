import re

def get_bot_response(user_input):
    # Text Normalization: Convert input to lowercase to make matching easier
    user_input = user_input.lower()
    
    # Pattern Matching using if-else statements
    if re.search(r'\b(hi|hello|hey|greetings)\b', user_input):
        return "Hello there! How can I help you today?"
    
    elif "how are you" in user_input:
        return "I'm just a collection of if-else statements, but I'm doing great! How are you?"
    
    elif re.search(r'\b(name|who are you)\b', user_input):
        return "I am RuleBot, a simple conversational assistant."
    
    elif "weather" in user_input:
        return "I can't check the live weather yet, but I hope it's nice outside!"
    
    elif "help" in user_input:
        return "You can say 'hello', ask my name, ask about the weather, or say 'bye' to leave."
    
    elif re.search(r'\b(bye|exit|quit)\b', user_input):
        return "Goodbye! Have a fantastic day!"
    
    else:
        # Fallback response for unrecognized inputs
        return "I'm not sure I understand. Type 'help' to see what we can talk about."

def chat():
    print("RuleBot: Hi! I'm online. (Type 'bye' to exit)")
    print("-" * 40)
    
    # Conversation Flow: A continuous loop that waits for user input
    while True:
        user_input = input("You: ")
        
        # Get the predefined response
        response = get_bot_response(user_input)
        print(f"RuleBot: {response}")
        
        # Break the loop if the user wants to exit
        if "bye" in user_input.lower() or "exit" in user_input.lower():
            break

# Run the chatbot
if __name__ == "__main__":
    chat()