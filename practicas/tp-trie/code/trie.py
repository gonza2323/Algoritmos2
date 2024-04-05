
class Trie:
    root = None


class TrieNode:
    parent = None
    children = None
    key = None
    isEndOfWord = False


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
