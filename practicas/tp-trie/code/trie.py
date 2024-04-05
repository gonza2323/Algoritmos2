
class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


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


def search(T, element):
    return None


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
