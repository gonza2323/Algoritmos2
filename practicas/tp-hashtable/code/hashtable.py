
def hash(k, m):
    return k % m


# --- Ejercicio 1a
def insert(d, key, value):
    tableIndex = hash(key, len(d))
    lista = d[tableIndex]

    if not lista:
        d[tableIndex] = [(key, value)]
        return d
    
    for i, (k, v) in enumerate(lista):
        if k == key:
            lista[i] = (key, value)
            return d
    
    lista.append((key, value))
    return d
# --- end


# --- Ejercicio 1b
def search(d, key):
    tableIndex = hash(key, len(d))
    lista = d[tableIndex]

    if not lista:
        return None
    
    for i, (k, v) in enumerate(lista):
        if k == key:
            return v
    
    return None
# --- end


# --- Ejercicio 1c
def delete(d, key):
    tableIndex = hash(key, len(d))
    lista = d[tableIndex]
    
    if not lista:
        return d
    
    for i, (k, v) in enumerate(lista):
        if k == key:
            lista.pop(i)
            if len(lista) == 0:
                d[tableIndex] = None
            break
    
    return d
# --- end


# --- Ejercicio 4
def isPermutation(stringS, stringP):
    if not stringS or not stringP:
        return False

    # Si son de distinto largo, no es permutación
    if len(stringS) != len(stringP):
        return False
    
    stringS = stringS.lower()
    stringP = stringP.lower()
    
    # Contamos los caracteres de cada palabra
    charsCountsS = dict()
    charsCountsP = dict()
    for i in range(len(stringS)):
        if stringS[i] in charsCountsS:
            charsCountsS[stringS[i]] += 1
        else:
            charsCountsS[stringS[i]] = 1
        if stringP[i] in charsCountsP:
            charsCountsP[stringP[i]] += 1
        else:
            charsCountsP[stringP[i]] = 1
    
    # Verificamos que coincidan
    for c in stringS:
        if c not in charsCountsP or charsCountsP[c] != charsCountsS[c]:
            return False
    
    return True
# --- end


# --- Ejercicio 5
def noRepeatedElements(lista):
    if lista is None:
        return False
    
    dictionary = dict()
    
    for item in lista:
        if item in dictionary:
            return False
        dictionary[item] = item
    
    return True
# --- end


# --- Ejercicio 6
def postalCodeHash(code):
    code = code.upper()
    ranges = [26, 10, 10, 10, 10, 26, 26, 26]
    currentBase = 1
    hash = 0

    for i in range(len(code) - 1, -1, -1):
        if code[i].isalpha():
            hash += (ord(code[i]) - 65 ) * currentBase
        else:
            hash += int(code[i]) * currentBase
        currentBase *= ranges[i]

    return hash
# --- end
