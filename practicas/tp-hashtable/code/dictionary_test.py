from dictionary import *


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


def test_compress_string():
    assert compress_string(None) == None
    assert compress_string("") == ""
    assert compress_string("aaaabcccddaaa") == "a4b1c3d2a3"
    assert compress_string("aaaabcccddaaab") == "a4b1c3d2a3b1"
    assert compress_string("aaabcccddaaabc") == "aaabcccddaaabc"
    assert compress_string("aaaabcccddaaabc") == "a4b1c3d2a3b1c1"
    assert compress_string("aaaabcccddaadbc") == "aaaabcccddaadbc"
    assert compress_string("abcd") == "abcd"


def test_is_subset():
    assert is_subset([5,8,2], [0,-5,5,12,8,2,42]) == True


def test_find_index():
    assert find_index("cada", "abracadabra") == 4
    assert find_index("abra", "abracadabra") == 0
    assert find_index("dabra", "abracadabra") == 6
    assert find_index("asdf", "abracadabra") == None
    assert find_index("a", "abracadabra") == 0
    assert find_index("f", "abracadabrf") == 10
    assert find_index("s", "abracsdabra") == 5
    assert find_index("abracadabra", "abracadabra") == 0
    assert find_index("abracaaabra", "abracadabra") == None
    assert find_index("abracadabra", "abra") == None
    assert find_index("abracadabra", "") == None
    assert find_index("", "abracadabra") == None
    assert find_index("es ", "Esto es una prueba mas compleja y es mas dificil") == 5
    assert find_index("prueba", "Esto es una prueba mas compleja y es mas dificil") == 12
    assert find_index("dificil", "Esto es una prueba mas compleja y es mas dificil") == 41
    assert find_index("E", "Esto es una prueba mas compleja y es mas dificil") == 0
    assert find_index("j", "Esto es una prueba mas compleja y es mas dificil") == 29
    assert find_index("l", "Esto es una prueba mas dificil") == 29
    assert find_index(" es una", "Esto es una prueba mas dificil") == 4
