# Extended_Chatbot README
==========================

Prerequisite in order for the code to run properly:
- Python version 12.9 or lower with nltk installed
- To install nltk: input 'pip install nltk'

**This is the failed version chatbot report:

As for this version, I did my research on how I could improve from the Codehs one and referenced some parts of the code from the internet (https://datasciencedojo.com/blog/rule-based-chatbot-in-python/). I decided to focus on developing interaction ability, so I took out the options of questions users could choose and let them type their questions instead. 

I figured there are several limitations to improving a rule-based chatbot when it comes to keywords; I tried to expand the scope of keywords the chatbot can recognize in order to effectively find the user’s intent in their questions. To do this, I use a built-in library called Natural Language Toolkit(NLTK). I’ve encountered many issues while trying to import it, I figured it only runs in Python 12.9 or lower. I intended to use its subset called wordnet which acts as a synonym list or words database. But I then realized that it is unable to answer a simple question like “what is it?” since words like ‘what’ can’t be fixed to one question. Moreover, it is hard to manipulate the synonyms from wordnet due to my own lack of complete understanding on how it works.  After many attempts, I simply think it’s better to manually build a list of keywords, compared to a list with irrelevant ones that users are very unlikely to use like from wordnet.
