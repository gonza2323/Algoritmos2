from binarytree import *

t = AVLTree()

for i in range(0, 10):
    insert(t, i, i)

rotateLeft(t, t.root)
rotateLeft(t, t.root)
rotateLeft(t, t.root)
rotateRight(t, t.root)
rotateRight(t, t.root)
rotateRight(t, t.root)

print("Hello")
