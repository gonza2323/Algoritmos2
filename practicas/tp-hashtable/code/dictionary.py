
def hash(k, m):
    return k % m


# --- Ejercicio 1a
def insert(d, key, value):
    tableIndex = hash(key, len(d))  # Calculamos índice
    lista = d[tableIndex]           # Obtenemos la lista en ese índice

    # Si no existe una lista, creamos una conteniendo al par (key, value)
    if not lista:
        d[tableIndex] = [(key, value)]
        return d
    
    # Si existe, vemos si ya está la key en ella
    # En tal caso, actualizamos el valor asociado
    for i, (k, v) in enumerate(lista):
        if k == key:
            lista[i] = (key, value)
            return d
    
    # Si no existe la key en la lista, agregamos el par (key, value)
    lista.append((key, value))
    return d
# --- end


# --- Ejercicio 1b
def search(d, key):
    tableIndex = hash(key, len(d))  # Calculamos índice en la tabla
    lista = d[tableIndex]           # Obtenemos la lista en ese índice

    if not lista:                   # Si no existe, no está el elemento
        return None
    
    # Si existe una lista, buscamos la key en ella
    for i, (k, v) in enumerate(lista):
        if k == key:                # Si existe en la lista,
            return v                # retornamos el valor asociado
    
    return None                     # Si no existe en la lista, retornamos None
# --- end


# --- Ejercicio 1c
def delete(d, key):
    tableIndex = hash(key, len(d))  # Calculamos índice en la tabla
    lista = d[tableIndex]           # Obtenemos la lista en ese índice
    
    if not lista:                   # Si no existe, no está el elemento
        return d
    
    # Si existe una lista, buscamos la key en ella
    for i, (k, v) in enumerate(lista):
        if k == key:                # Si existe en la lista,
            lista.pop(i)            # la sacamos de la lista
            if len(lista) == 0:     # Si quedó vacía, la cambiamos por None
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
    
    dictionary = dict()         # Guardamos cada elemento en un diccionario
    
    for item in lista:
        if item in dictionary:  # Si ya hay un elemento igual en el diccionario
            return False        # La lista tiene elementos repetidos
        dictionary[item] = item # Si no, lo añadimos al diccionario
    
    return True                 # Retornamos True si no hubo repeticiones
# --- end


# --- Ejercicio 6
def postalCodeHash(code):
    code = code.upper()
    
    # Cantidad de valores posibles por posición del código postal
    ranges = [26, 10, 10, 10, 10, 26, 26, 26]
    currentBase = 1 # Base con la cual multiplicar a un caracter
    codeHash = 0    # Hash que se está calculando

    # Recorremos el código postal de derecha a izquierda
    # Multiplicamos al valor (mapeado de 0 a 25 para las letras)
    # por la base actual y lo sumamos al hash. Luego actualizamos la base.
    for i in range(len(code) - 1, -1, -1):
        if code[i].isalpha():
            codeHash += (ord(code[i]) - 65 ) * currentBase
        else:
            codeHash += int(code[i]) * currentBase
        currentBase *= ranges[i]

    return codeHash
# --- end


# --- Ejercicio 7
def compress_string(string):
    if string is None:
        return None
    
    if not string:
        return ""
    
    currentChar = string[0]
    charCount = 1
    newStringArray = [''] * len(string)
    arrayIndex = 0

    for i in range(1, len(string)):
        if string[i] == currentChar:
            charCount += 1
        else:
            newStringArray[arrayIndex] = currentChar
            newStringArray[arrayIndex + 1] = str(charCount)

            arrayIndex += 2
            charCount = 1
            currentChar = string[i]

            if len(string) - arrayIndex < 3:
                return string
    
    newStringArray[arrayIndex] = currentChar
    newStringArray[arrayIndex + 1] = str(charCount)
    
    return ''.join(newStringArray[:arrayIndex + 2])
# --- end


# --- Ejercicio 8
def findIndex(s, p):
    return 0
# --- end


# --- Ejercicio 9
def is_subset(s, p):
    pDictionary = dict()
    for element in p:
        pDictionary[element] = 1
    
    for element in s:
        if not pDictionary[element]:
            return False
    
    return True
# --- end
