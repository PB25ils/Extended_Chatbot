# Importing modules
import re
import nltk
from nltk.corpus import wordnet  

# Download wordnet if not already downloaded
nltk.download('wordnet')

# Keywords and responses
keywords = {
    'hello': "Hello! How can I help you?",
    'define': """
    Basically, the Grid-drawing method is one of the most well-known 
    drawing techniques where you apply the same grid to both your canvas
    and the reference. This way, you can copy proportions and details
    from the reference accurately.

    It is particularly useful for solving scaling issues and helps
    improve your observational skills.
    """,
    'differences': """
    The outcomes are very different. As mentioned before, this is a
    DRAWING TECHNIQUE that helps you draw easier and more efficiently.
    Simply looking at a reference with our eyes has limitations in
    capturing details and proportions.

    Grid-drawing fixes that by allowing you to focus on small 
    sections at a time. This makes it especially helpful when 
    drawing in a different scale than the reference.
    """,
    'how': """
    Like its name suggests, you apply the same grid on your canvas or paper
    as your reference. Then, start by observing each box and outlining
    larger shapes. Keep your pencil pressure light to avoid difficulty
    in erasing mistakes.

    While the reference should have clear grid lines, your drawing 
    should be lightly gridded to avoid affecting the final result.
    """,
}

# Generate synonyms for each keyword
list_syn = {word: set() for word in keywords}
for word in keywords:
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            clean_word = re.sub(r'[^a-zA-Z0-9 \n.]', '', lem.name().lower())  # Remove special characters
            list_syn[word].add(clean_word)

# Greeting message
print("""
**********************************************
Welcome to Grido, your virtual art assistant! 🎨✨

Ever felt frustrated with your drawings? 
Don't worry! I'm here to help you master the 
GRID DRAWING METHOD!

Ask me about:
- "hello" ➝ to start a conversation
- "define" ➝ to learn about the grid drawing method
- "differences" ➝ to understand why it makes a difference
- "how" ➝ to learn how to apply the method

**********************************************
Type "done" or "quit" to exit.
""")

while True:
    user_input = input("You: ").lower().strip()
    
    # Exit conditions
    if user_input in ["done", "quit", "exit"]:
        print("Have fun drawing! See you next time!")
        break

    user_input_list = user_input.split()
    
    # Search for a valid keyword
    found_response = None
    for word in user_input_list:
        for key, synonyms in list_syn.items():
            if word in synonyms:
                found_response = keywords[key]
                break
        if found_response:
            break
    
    # Print response or fallback
    print(found_response if found_response else "Sorry, I didn't understand that. Please try again.")
