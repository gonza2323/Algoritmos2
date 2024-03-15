
class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


def _insertNode(currentNode, newNode):    
    newNode.parent = currentNode
    if newNode.key < currentNode.key:
        if currentNode.leftnode is None:
            currentNode.leftnode = newNode
            return newNode.key
        else:
            return _insertNode(currentNode.leftnode, newNode)
    elif newNode.key > currentNode.key:
        if currentNode.rightnode is None:
            currentNode.rightnode = newNode
            return newNode.key
        else:
            return _insertNode(currentNode.rightnode, newNode)
    else:
        print("Error! Ya existe un elemento para la key indicada!")
        return None


def insert(t, element, key):
    if not t:
        return None
    
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    newNode.bf = 0

    if t.root is None:
        t.root = newNode
        return key
    
    return _insertNode(t.root, newNode);
