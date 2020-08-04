#Basic Chatbot responding to Hello from the user !!

from nltk.chat.util import Chat,reflections

pairs = [
    ['my name is (.*)',['Hi %1']],
    ['(hi|hello|hey there|hola|hey)',['hey there','hello','hola']],
    ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],


]




chat = Chat(pairs,reflections)
# chat._substitute('go hello')
chat.converse()
