from trie import *

t = Trie()

words = [
    "Ho",
    "Hola",
    "Holanda",
    "Gonzalo",
    "Gonza",
    "G",
    "Buenas",
    "Mama",
    "Mamadera",
    "Ma",
]

for word in words:
    insert(t, word)

print(getWords(t))