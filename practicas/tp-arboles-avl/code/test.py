from binarytree import *

t = AVLTree()

for i in range(0, 10):
    insert(t, i, i)

# rotateLeft(t, t.root)
# rotateLeft(t, t.root)
# rotateLeft(t, t.root)
calculateBalance(t)

print("Hello")
