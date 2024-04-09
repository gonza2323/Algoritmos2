
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


# Version para árboles binarios, no funciona en trie
def toString(t):
    if not t:
        return None
    
    def nodeToString(node, length):
        if not node:
            return ""
        
        centerString = f"({node.key}, {node.bf})"

        if node.parent:
            if node == node.parent.rightnode:
                centerString = "┌" + centerString
            else:
                centerString = "└" + centerString
        
        if node.rightnode and node.leftnode:
            centerString += "┤"
        elif node.rightnode and not node.leftnode:
            centerString += "┘"
        elif not node.rightnode and node.leftnode:
            centerString += "┐"
        
        centerString = (length - 2) * " " + centerString + "\n"
        
        rightString = nodeToString(node.rightnode, len(centerString))
        leftString = nodeToString(node.leftnode, len(centerString))

        return rightString + centerString + leftString

    return nodeToString(t.root, 0)
