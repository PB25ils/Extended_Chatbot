import re
from nltk.corpus import wordnet

# Function to get synonyms from WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            lem_name = re.sub(r'[^a-zA-Z0-9 ]', ' ', lem.name())  # Clean up special characters
            synonyms.add(lem_name.lower())
    return synonyms

# Base keywords related to grid-drawing (Expanding with synonyms)
base_keywords = {
    "greet": ["hello", "hi", "hey"],
    "steps": ["steps", "process", "instructions", "how to", "method"],
    "materials": ["materials", "tools", "supplies", "needed", "equipment"],
    "accuracy": ["accuracy", "precision", "alignment", "correctness"],
    "benefits": ["benefits", "advantages", "why use", "purpose", "helpful"],
    "mistakes": ["mistakes", "errors", "problems", "wrong", "issues", "fix"],
    "goodbye": ["bye", "goodbye", "see you", "farewell"]
}

# Expand keywords with synonyms
expanded_keywords = {intent: set() for intent in base_keywords}
for intent, words in base_keywords.items():
    for word in words:
        expanded_keywords[intent].update(get_synonyms(word))  # Add synonyms dynamically

# Convert keyword sets to regex patterns for efficient matching
keywords_dict = {intent: re.compile(r'\b(?:' + '|'.join(map(re.escape, words)) + r')\b', re.IGNORECASE) 
                 for intent, words in expanded_keywords.items()}

# Responses for different intents
responses = {
    "greet": "Hello! Ask me anything about the grid-drawing method.",
    "steps": "To use the grid-drawing method, first draw a grid over your reference image and another on your drawing paper. Then, copy each square one by one to maintain proportions.",
    "materials": "You'll need a ruler, pencil, eraser, and a reference image. A fine-tipped pen may help for more precise grid lines.",
    "accuracy": "Make sure to keep the grid lines straight and use light pencil strokes. Checking alignment regularly helps maintain accuracy.",
    "benefits": "The grid method helps artists maintain proportions and improve accuracy, making it especially useful for enlarging or reducing images.",
    "mistakes": "Common mistakes include misaligned grids, incorrect scaling, or pressing too hard on the paper. Always double-check your measurements!",
    "goodbye": "Happy drawing! Let me know if you have more questions.",
    "fallback": "I don't quite understand. Could you clarify your question about the grid-drawing method?"
}

# Start chatbot
print("Welcome! I can help you with the grid-drawing method. Ask me anything!")

while True:
    user_input = input().strip().lower()  # Remove spaces and standardize input
    
    if not user_input:  # Handle empty input
        print(responses["fallback"])
        continue

    if user_input in ["quit", "exit"]:
        print("Happy drawing! See you next time!")
        break

    matched_intent = None
    for intent, pattern in keywords_dict.items():
        if pattern.search(user_input):  # Check if input matches any keyword pattern
            matched_intent = intent
            break

    response = responses.get(matched_intent, responses["fallback"])
    print(response)
