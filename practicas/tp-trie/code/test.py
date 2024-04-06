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

print(search(t, "M"))
print(search(t, "Ma"))
print(search(t, "G"))
print(search(t, "Gonzal"))
print(search(t, "Gonzalo"))
print(search(t, "Gonzalos"))
