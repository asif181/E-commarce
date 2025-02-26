
import random

# List of sweet messages or compliments
messages = [
    "You are the light of my life.",
    "I am so grateful to have you in my life.",
    "You make every moment special.",
    "You are amazing, just the way you are!",
    "Your smile brightens up my day.",
    "You make the world a better place.",
    "I appreciate you more than you know.",
    "You are loved more than words can express.",
    "Thank you for being you!",
    "Every moment with you is a gift."
]

# Function to choose and print a random sweet message
def send_love_message():
    message = random.choice(messages)
    print(f"Here's a message for you: \n'{message}'")

# Call the function to display a sweet message
send_love_message()
