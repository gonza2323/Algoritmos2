from hashtable import *

m = 5
myDict = [None] * m

words = [
    "gonzalo",
    "agustin",
    "tomas",
    "clara",
    "matias",
    "roberto",
    "diego",
    "julia",
]

for i, w in enumerate(words):
    insert(myDict, i, w)


for i, w in enumerate(words):
    if search(myDict, i) != w:
        print(False)
        exit()

print(True)
print(myDict)

delete(myDict, 0)
delete(myDict, 5)
delete(myDict, 6)
delete(myDict, 1)
delete(myDict, 2)
print(myDict)
