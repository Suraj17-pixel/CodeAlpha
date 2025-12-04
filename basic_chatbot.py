def simple_chatbot():
    """A simple rule-based chatbot"""
    
    # Predefined responses
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! Nice to meet you!",
        "how are you": "I'm doing great, thanks for asking! How about you?",
        "what is your name": "I'm ChatBot, your virtual assistant!",
        "bye": "Goodbye! Have a wonderful day!",
        "thank you": "You're welcome! 😊",
        "what can you do": "I can chat with you! Try asking about my name or saying hello.",
        "good morning": "Good morning! Hope you have a great day ahead!",
        "good night": "Good night! Sleep well!",
        "help": "I'm here to chat with you. You can say hello, ask how I am, or just talk!"
    }
    
    print("🤖 Welcome to Simple ChatBot!")
    print("Type 'bye' to exit the chat.\n")
    print("ChatBot: Hello! I'm your friendly chatbot. How can I assist you today?")
    
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()
        
        # Check for exit condition
        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            print("ChatBot: Goodbye! Thanks for chatting with me!")
            break
        
        # Check for exact matches first
        if user_input in responses:
            print(f"ChatBot: {responses[user_input]}")
        else:
            # Check for partial matches
            found_response = False
            for key in responses:
                if key in user_input:
                    print(f"ChatBot: {responses[key]}")
                    found_response = True
                    break
            
            # Default response if no match found
            if not found_response:
                print("ChatBot: I'm not sure how to respond to that. Try saying hello or asking what I can do!")
        
        print()  # Empty line for readability

def enhanced_chatbot():
    """Enhanced version with more features"""
    
    responses = {
        "greetings": ["Hello!", "Hi!", "Hey there!", "Greetings!"],
        "how_are_you": ["I'm great, thanks!", "Doing well! How about you?", "All systems operational!"],
        "farewell": ["Goodbye!", "See you later!", "Bye! Take care!"],
        "default": ["Interesting...", "Tell me more!", "I see.", "That's nice!"]
    }
    
    print("🤖 Enhanced ChatBot Activated!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if any(word in user_input for word in ['bye', 'exit', 'quit']):
            print(f"ChatBot: {random.choice(responses['farewell'])}")
            break
        elif any(word in user_input for word in ['hello', 'hi', 'hey']):
            print(f"ChatBot: {random.choice(responses['greetings'])}")
        elif 'how are' in user_input:
            print(f"ChatBot: {random.choice(responses['how_are_you'])}")
        elif 'name' in user_input:
            print("ChatBot: I'm ChatBot 2.0!")
        elif 'time' in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M")
            print(f"ChatBot: The current time is {current_time}")
        elif 'date' in user_input:
            from datetime import datetime
            current_date = datetime.now().strftime("%B %d, %Y")
            print(f"ChatBot: Today is {current_date}")
        else:
            print(f"ChatBot: {random.choice(responses['default'])}")

if __name__ == "__main__":
    # Run the simple chatbot
    simple_chatbot()
    
    # Uncomment to run the enhanced version instead
    # import random
    # enhanced_chatbot()