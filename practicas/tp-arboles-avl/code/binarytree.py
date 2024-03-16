
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
