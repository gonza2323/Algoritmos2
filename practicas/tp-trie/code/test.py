from trie import *

t = Trie()

wordsInTrie = [
    "Ho",
    "Hola",
    "Holanda",
    "Gonzalo",
    "Gonza",
    "Gonzi",
    "Buenas",
    "Mama",
    "Mamadera",
    "Ma",
]

wordsNotInTrie = [
    "H",
    "Gonz",
    "Gon",
    "Mamaderas",
    "Verdura",
]

for word in wordsInTrie:
    insert(t, word)

print("Palabras en el trie:")
print(getWords(t))

print("\nPalabras que debe encontrar:")
for word in wordsInTrie:
    print(word, search(t, word))

print("\nPalabras que no debe encontrar:")
for word in wordsNotInTrie:
    print(word, search(t, word))
