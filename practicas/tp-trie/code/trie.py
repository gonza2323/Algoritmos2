
class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


# --- Ejercicio 1a
def insert(T, element):
    if not element or not T:
        return None
    
    if not T.root:
        T.root = TrieNode()
        T.root.children = [None] * 27

    node = T.root
    element = element.lower()
    for i, char in enumerate(element):
        indexChild = ord(char) - 97
        nextNode = node.children[indexChild]
        if not nextNode:
            node.children[indexChild] = TrieNode()
            nextNode = node.children[indexChild]
            nextNode.children = [None] * 27
            nextNode.key = char
            nextNode.parent = node
        if i == len(element) - 1:
            nextNode.isEndOfWord = True
        node = nextNode

    return None
# --- end


# --- Ejercicio 1b
def search(T, element):
    return True if _findLastNodeOfWord(T, element) else False


def _findLastNodeOfWord(T, element):    
    if not T or not T.root or not element:
        return False
    
    node = T.root
    element = element.lower()
    for i, char in enumerate(element):
        node = node.children[ord(char) - 97]
        if (not node or
            node.key != char or
            (i == len(element) - 1 and not node.isEndOfWord)):
            return False

    return node
# --- end


# --- Ejercicio 3
def delete(T, element):
    if not T or not T.root or not element:
        return False
    
    node = _findLastNodeOfWord(T, element) # final de palabra, si existe

    if not node:
        return False # Si no existe, no hacemos nada
    
    node.isEndOfWord = False

    # Mientras no tenga hijos ni sea fin de otra palabra, borramos nodo:
    while (not any(child for child in node.children) and not node.isEndOfWord):
        node.parent.children[ord(node.key)-97] = None # borramos el nodo
        node = node.parent # pasamos a su padre

    return True
# --- end


# --- Ejercicio 4
def printWordsWithPrefixAndLength(t, prefix, length):
    if not t or not t.root or not prefix or not length:
        return
    
    # Si el prefijo es mayor al largo de
    # palabra, retornamos
    if length < len(prefix):
        return
    
    # Encontrar node final del prefijo
    node = t.root
    prefix = prefix.lower()
    for c in prefix:
        node = node.children[ord(c) - 97]
        if not node or node.key != c:
            return
    
    # Imprime palabras a partir de un nodo,
    # que tengan el largo indicado
    def printWordsFromNodeWithLength(node, word):
        if not node:
            return
        
        # Si llegamos al largo indicado,
        # imprimimos si es final de palabra
        # Si no, cortamos
        if len(word) == length:
            if node.isEndOfWord:
                print(word)
            return
        
        # Si todavía no llegamos al largo indicado
        # recorremos cada hijo del nodo
        for child in node.children:
            if child:
                printWordsFromNodeWithLength(child, word + child.key)

    # Imprimimos palabras del largo indicado
    # partiendo desde el final del prefijo
    printWordsFromNodeWithLength(node, prefix)
# --- end


def getWords(T):
    if not T:
        return None
    
    words = []

    def getWordsNode(word, node):
        if node.key:
            word = word + node.key
        
        if node.isEndOfWord:
            words.append(word)
        
        for child in node.children:
            if child:
                getWordsNode(word, child)
    
    if T.root:
        getWordsNode("", T.root)
    return words
