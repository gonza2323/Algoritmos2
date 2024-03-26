
class AVLTree:
    root = None


class AVLNode:
    parent = None
    leftnode = None
    rightnode = None
    key = None
    value = None
    bf = None


# --- Ejercicio 4
def _insertNode(currentNode, newNode):    
    if newNode.key < currentNode.key: # Insertamos a la izquierda
        if not currentNode.leftnode: # Si no hay hijo, pasa a ser el nuevo hijo
            currentNode.leftnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else: # Si lo hay, llamamos a la recursión
            return _insertNode(currentNode.leftnode, newNode)
    elif newNode.key > currentNode.key: # Insertamos a la derecha
        if not currentNode.rightnode: # Si no hay hijo, pasa a ser el nuevo hijo
            currentNode.rightnode = newNode
            newNode.parent = currentNode
            return newNode.key
        else: # Si lo hay, llamamos a la recursión
            return _insertNode(currentNode.rightnode, newNode)
    else:
        print("Error! Ya existe un elemento para la key indicada!")
        return None # Si ya existe la key en el árbol, devolvemos None


def insert(t, element, key):
    if not t:
        return None
    
    # Creamos el nuevo nodo
    newNode = AVLNode()
    newNode.key = key
    newNode.value = element
    newNode.bf = 0

    # Si no hay raíz, pasa a ser la raíz
    if not t.root:
        t.root = newNode
        return key
    
    key = _insertNode(t.root, newNode) # Si no, insertamos
    reBalance(t) # Rebalanceamos
    return key # Retornamos la key si fue exitoso (puede ser None)
# --- end


def _findNodeByValue(node, value):    
    if not node:
        return None
    
    if node.value == value:
        return node
    
    return _findNodeByValue(node.leftnode, value) or _findNodeByValue(node.rightnode, value)


def _findNodeByKey(node, key):    
    if not node:
        return None
    
    if node.key == key:
        return node
    elif key < node.key:
        return _findNodeByKey(node.leftnode, key)
    else:
        return _findNodeByKey(node.rightnode, key)


def search(B, element):
    node = _findNodeByValue(B.root, element)
    return node.key if node else None


def _findSmallest(node):
    if not node:
        return None
    
    if not node.leftnode:
        return node
    
    return _findSmallest(node.leftnode)


def _findLargest(node):
    if not node:
        return None
    
    if not node.rightnode:
        return node
    
    return _findLargest(node.rightnode)


# --- Ejercicio 5
def _deleteNode(B, node):
    if not node:
        return None
    
    # El nodo a eliminar es reemplazado por el más pequeño de su subárbol derecho
    # o el más grande de su subárbol izquierdo para mantener el orden
    # _delteNode lo elimina de su posición y nos lo devuelve
    newNode = _deleteNode(B, _findSmallest(node.rightnode) or _findLargest(node.leftnode))

    # Si existe un reemplazo, reemplazamos
    if newNode:
        newNode.leftnode = node.leftnode
        newNode.rightnode = node.rightnode
        if newNode.leftnode:
            newNode.leftnode.parent = newNode
        if newNode.rightnode:
            newNode.rightnode.parent = newNode
        newNode.parent = node.parent
    
    # Apuntamos el padre al nuevo nodo
    if not node.parent:
        B.root = newNode
    elif node.parent.leftnode == node:
        node.parent.leftnode = newNode
    else:
        node.parent.rightnode = newNode

    return node # Retornamos el nodo eliminado


def delete(B, element):
    node = _deleteNode(B, _findNodeByValue(B.root, element)) # Buscamos el nodo y lo eliminamos
    reBalance(B) # Rebalanceamos el árbol
    return node.key if node else None # Retornamos la key
# --- end


def deleteKey(B, key):
    node = _deleteNode(B, _findNodeByKey(B.root, key))
    reBalance(B)
    return node.key if node else None


def access(B, key):
    node = _findNodeByKey(B.root, key)
    return node.value if node else None


def update(B, element, key):
    node = _findNodeByKey(B.root, key)
    if node:
        node.value = element
        return key
    else:
        return None


# --- Ejercicio 1
def rotateLeft(t, node):
    # Caso especial donde debe realizarse una rotación previa
    if node.rightnode.bf > 0:
        rotateRight(t, node.rightnode)

    a = node # raíz actual
    b = node.rightnode # nueva raíz

    # Convertir a 'b' en la nueva raíz
    a.rightnode = None
    b.parent = a.parent
    if b.parent:
        if b.key > b.parent.key:
            b.parent.rightnode = b
        else:
            b.parent.leftnode = b
    else:
        t.root = b
    
    # Si 'b' tenía hijo izquierdo, pasa a ser el
    # hijo derecho de 'a'
    if b.leftnode:
        a.rightnode = b.leftnode
        b.leftnode.parent = a
        b.leftnode = None

    # Nodo 'a' para a ser hijo izquierdo de 'b'
    b.leftnode = a
    a.parent = b

    return b # Retornamos la nueva raíz
# --- end


def rotateRight(t, node):
    # Caso especial donde debe realizarse una rotación previa
    if node.leftnode.bf < 0:
        rotateLeft(t, node.leftnode)

    a = node # raíz actual
    b = node.leftnode # nueva raíz

    # Nodo 'b' es la nueva raíz
    a.leftnode = None
    b.parent = a.parent
    if b.parent:
        if b.key > b.parent.key:
            b.parent.rightnode = b
        else:
            b.parent.leftnode = b
    else:
        t.root = b
    
    # Si 'b' tenía hijo derecho, pasa a ser el
    # hijo izquierdo de 'a'
    if b.rightnode:
        a.leftnode = b.rightnode
        b.rightnode.parent = a
        b.rightnode = None
    
    # Nodo 'a' para a ser hijo derecho de 'b'
    b.rightnode = a
    a.parent = b

    return b # Retornamos la nueva raíz
    

# --- Ejercicio 2
def calculateBalance(AVLTree):
    if not AVLTree:
        return None
    
    # Calcula el balance factor de cada nodo, calculando
    # previamente la altura de cada sub árbol. Orden O(n)
    def calculateNodeBalance(node):
        if not node:
            return 0
        
        leftHeight = calculateNodeBalance(node.leftnode)
        rightHeight = calculateNodeBalance(node.rightnode)
        node.bf = leftHeight - rightHeight
        return max(leftHeight, rightHeight) + 1
    
    calculateNodeBalance(AVLTree.root)
    return AVLTree # Retornamos el árbol
# --- end


# --- Ejercicio 3
# Balancea un nodo y sus hijos
# Retorna True si ocurrió un balanceo de forma exitosa
# Si no ocurrieron, o fallaron, retorna False
def reBalanceNode(t, node):
    if not node:
        return False
    
    # Balanceamos los subárboles del nodo
    # Si un nodo inferior fue balanceado, por propiedades
    # de los AVL ya no es necesario balancear este nodo
    wasReBalanced = reBalanceNode(t, node.leftnode) or reBalanceNode(t, node.rightnode)

    if wasReBalanced:
        return True
    
    if abs(node.bf) < 2: # Nodo balanceado
        return False

    if node.bf == 2:
        return rotateRight(t, node) # Balanceamos
    elif node.bf == -2:
        return rotateLeft(t, node) # Balanceamos
    elif abs(node.bf) > 2:
        print(f'Node con key = {node.key} tiene un balance factor = {node.bg} incorregible!')
        return False # Algo salió muy mal


def reBalance(t):
    if not t:
        return None
    
    calculateBalance(t) # Calculamos los balances por si no existen o están desactualizados
    reBalanceNode(t, t.root) # Balanceamos
    calculateBalance(t) # Recalculamos los balances
    return t
# --- end


# --- Ejercicio opcional1
def height(t):
    if t is None:
        return None
    
    def nodeHeight(node):
        if node is None:
            return 0
        
        # Utilizando el balance factor, elegimos el subárbol
        # de mayor altura y seguimos la recursión por ahí.
        longest = node.rightnode if node.bf < 0 else node.leftnode
        
        # Retornamos la altura del subárbol más alto + 1
        return nodeHeight(longest) + 1
    
    return nodeHeight(t.root) - 1 if t.root else 0
# --- end


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
