from avltree import *

t = AVLTree()

# a = 8
# h = 3
# for i in range(h):
#     for j in range(2**i):
#         v = (a / 2**i) * (1 + j*2)
#         insert(t, v, v)

for i in range(15):
    insert(t, 0, i)
    print(toString(t))
