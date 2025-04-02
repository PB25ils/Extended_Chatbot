# Importing modules
import re
from nltk.corpus import wordnet 


# Building a list of Keywords
list_words=['hello','define', 'differences', 'how']
list_syn={}
for word in list_words:
    synonyms=[]
    for syn in wordnet.synsets(word):
        for lem in syn.lemmas():
            # Remove any special characters from synonym strings
            lem_name = re.sub(r'[^a-zA-Z0-9 \n.]', ' ', lem.name())
            synonyms.append(lem_name)
    list_syn[word]=set(synonyms)
print (list_syn)


# Building a dictionary of responses
responses={
    'hello':'Hello! How can I help you?',
    'grid_method_definition':"""
    
Basically, Grid-drawing method is one of the most well-known 
drawing techniques where you apply the same grid to both your canvas
and the reference. This way, you can copy the instance of the 
proportion and details from the photo reference accurately.

It is particularly useful for solving scaling issues and also helps
you improve your observational skill.

*********************************************************************
    
""",

'differences' : """

The outcomes are very different. As mentioned before, it is a
DRAWING TECHNIQUE which was created to help you draw easier
and more efficiently. Drawing by just looking at the reference with our 
eyes has very limited ablilty to capture every detail and how it should 
be proportioned.

Grid-drawing method helps you fix that by letting you focus on just small 
boxes of the grid. You might be wondering how it make that much of a difference.
And yes, it does, especially when you draw in a different scale as your 
reference might be bigger or smaller.

**********************************************************************
    
""",

'how_to' : """

Like its name; you apply the same grid on your canvas or paper as your reference.
Then, you should start by observing each box and OUTLINING the bigger shapes.
Remember that you should not put a lot of pressure on your pencil while outlining
or it'll be difficult to erase if you make a mistake.

Same with the grid; while the reference should show clear grid lines, your drawing 
paper/canvas should be lightly grided.

***********************************************************************

    """
}



#Introduction & greeting

print("""
Have you ever felt so frustrasted on how your 
drawing turned out, that you wanted to throw
all your supplies out of the window??

Exactly, and I'm here to help you no to do the exact 
you're wanting to do!!

Hi! you can consider me as your art teacher,
my name is Grido and I'll be guiding you through the 
process of accurately draw from your reference 
WITHOUT having to trace it ^^

**********************************************

I introduce you a secret(not really) technique>>>
GRID DRAWING METHOD!!!
      
What would you like to know about grid-drawing method?
      
********************************************
      

If you're done, type 'done'

""")
done = False

while done == False:
    user_input = input("You: ").lower()
    user_input_list = user_input.split()  
    
    
    for word in user_input_list:
        # Checking if the user's input is in the list of keywords
        if word in list_syn["hello"]:
        # If the user's input is in the list of keywords, print a response from the dictionary
            print(responses["hello"])
            break

        elif word in list_syn["define"]:
            print(responses["grid_method_definition"])
            break

        elif word in list_syn["differences"]:
            print(responses["differences"])
            break

        elif word in list_syn["how"]:
            print(responses["how_to"])
            break

        elif word == "done":
            print("Have fun drawing!")
            done = True
            break
        else:
            print("Sorry, I didn't understand that. Please try again.")

