
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
    if newNode.key < currentNode.key:
        if currentNode.leftnode is None:
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else:
            return _insertNode(currentNode.leftnode, newNode)
    elif newNode.key > currentNode.key:
        if currentNode.rightnode is None:
            currentNode.rightnode = newNode
            newNode.parent = currentNode
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


def _findNodeByValue(node, value):    
    if node is None:
        return None
    
    if node.value == value:
        return node
    
    return _findNodeByValue(node.leftnode, value) or _findNodeByValue(node.rightnode, value)


def _findNodeByKey(node, key):    
    if node is None:
        return None
    
    if node.key == key:
        return node
    elif key < node.key:
        return _findNodeByKey(node.leftnode, key)
    else:
        return _findNodeByKey(node.rightnode, key)


def search(B, element):
    node = _findNodeByValue(B.root, element)
    return node.key if node is not None else None


def _findSmallest(node):
    if node is None:
        return None
    
    if node.leftnode is None:
        return node
    
    return _findSmallest(node.leftnode)


def _findLargest(node):
    if node is None:
        return None
    
    if node.rightnode is None:
        return node
    
    return _findLargest(node.rightnode)


def _deleteNode(B, node):
    if node is None:
        return None
    
    newNode = _deleteNode(B, _findSmallest(node.rightnode) or _findLargest(node.leftnode))

    if newNode is not None:
        newNode.leftnode = node.leftnode
        newNode.rightnode = node.rightnode
        if newNode.leftnode is not None:
            newNode.leftnode.parent = newNode
        if newNode.rightnode is not None:
            newNode.rightnode.parent = newNode
        newNode.parent = node.parent
    
    if node.parent is None:
        B.root = newNode
    elif node.parent.leftnode == node:
        node.parent.leftnode = newNode
    else:
        node.parent.rightnode = newNode

    return node


def delete(B, element):
    node = _deleteNode(B, _findNodeByValue(B.root, element))
    return node.key if node is not None else None


def deleteKey(B, key):
    node = _deleteNode(B, _findNodeByKey(B.root, key))
    return node.key if node is not None else None


def rotateLeft(t, node):
    # (raíz) A -> B -> C

    # Caso especial:
    if node.rightnode.bf > 0:
        rotateRight(t, node.rightnode)

    a = node
    b = node.rightnode

    # Nodo B es la nueva raíz
    a.rightnode = None
    b.parent = a.parent
    if b.parent:
        if b.key > b.parent.key:
            b.parent.rightnode = b
        else:
            b.parent.leftnode = b
    else:
        t.root = b
    
    # Si B tenía hijo izquierdo, pasa a ser el
    # hijo derecho de A
    if b.leftnode:
        a.rightnode = b.leftnode
        b.leftnode.parent = a
        b.leftnode = None

    # Nodo A es el hijo izquierdo de B
    b.leftnode = a
    a.parent = b

    return b


def rotateRight(t, node):
    # C <- B <- A (raiz)
    
    # Caso especial:
    if node.leftnode.bf < 0:
        rotateLeft(t, node.leftnode)

    a = node
    b = node.leftnode

    # Nodo B es la nueva raíz
    a.leftnode = None
    b.parent = a.parent
    if b.parent:
        if b.key > b.parent.key:
            b.parent.rightnode = b
        else:
            b.parent.leftnode = b
    else:
        t.root = b
    
    # Si B tenía hijo derecho, pasa a ser el
    # hijo izquierdo de A
    
    if b.rightnode:
        a.leftnode = b.rightnode
        b.rightnode.parent = a
        b.rightnode = None
    
    # Nodo A es el hijo derecho de B
    b.rightnode = a
    a.parent = b

    return b


def calculateNodeBalance(node):
    if not node:
        return 0
    
    leftHeight = calculateNodeBalance(node.leftnode)
    rightHeight = calculateNodeBalance(node.rightnode)
    node.bf = leftHeight - rightHeight
    return max(leftHeight, rightHeight) + 1
    

def calculateBalance(AVLTree):
    if not AVLTree:
        return None
    
    calculateNodeBalance(AVLTree.root)
    return AVLTree


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
