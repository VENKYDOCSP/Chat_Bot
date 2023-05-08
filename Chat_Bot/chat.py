import random

greetings = ["hello", "hi", "hey", "greetings", "yo"]
responses = ["How are you?", "What can I do for you?", "Nice to meet you!"]

while True:
    message = input("You: ")
    if message.lower() in greetings:
        print("Bot: " + random.choice(responses))
    elif message.lower() == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I'm sorry, I don't understand what you're saying.")
