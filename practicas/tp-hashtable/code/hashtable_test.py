from hashtable import *


def test_insert():
    pairs = [
        (0, "Gonza"),
        (5, "Roberto"),
        (10, "Banana"),
        (4, "Chocolate"),
        (9, "Frutilla"),
        (3, "Pedro")
    ]
    d = [None] * 5
    
    for (k, v) in pairs:
        insert(d, k, v)
    
    for (k, v) in pairs:
        assert search(d, k) == v


def test_update():
    pairs = [
        (0, "Gonza"),
        (5, "Roberto"),
        (10, "Banana"),
        (4, "Chocolate"),
        (9, "Frutilla"),
        (3, "Pedro")
    ]
    d = [None] * 5
    
    for (k, v) in pairs:
        insert(d, k, v)
    
    updates = [
        (0, "Agustín"),
        (3, "Diego"),
        (9, "Sandía")
    ]
    
    for (k, v) in updates:
        insert(d, k, v)

    for (k, v) in updates:
        assert search(d, k) == v


def test_delete():
    keysToAdd = [0, 1, 2, 3, 4, 5]
    d = [None] * 5
    
    for k in keysToAdd:
        insert(d, k, k)
    
    keysToDelete = [0, 2, 3, 5, 10]

    for k in keysToDelete:
        delete(d, k)
    
    for k in keysToDelete:
        assert search(d, k) == None
    
    for k in [key for key in keysToAdd if key not in keysToDelete]:
        assert search(d, k) == k


def test_isPermutation():
    assert isPermutation("igual", "igual") == True
    assert isPermutation("hola", "loha") == True
    assert isPermutation("Hola", "loha") == True
    assert isPermutation("gonzalo", "lozagon") == True
    assert isPermutation("gonzalo", "lozAgOn") == True
    assert isPermutation("asdf", "asdg") == False
    assert isPermutation("aaa", "aba") == False
    assert isPermutation("asdf", "asdff") == False
    assert isPermutation("asdff", "asdf") == False
    
    assert isPermutation(None, "hola") == False
    assert isPermutation("hola", None) == False
    assert isPermutation(None, None) == False
    assert isPermutation("", "") == False


def test_noRepeatedElements():
    assert noRepeatedElements(None) == False
    assert noRepeatedElements([]) == True
    assert noRepeatedElements([1,1,2,3,4]) == False
    assert noRepeatedElements([1,0,2,3,4]) == True
    assert noRepeatedElements([1,0,2,4,"4"]) == True
