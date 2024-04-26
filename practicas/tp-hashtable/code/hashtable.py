
def hash(k, m):
    return k % m


def insert(d, key, value):
    tableIndex = hash(key, len(d))
    lista = d[tableIndex]

    if not lista:
        d[tableIndex] = [(key, value)]
        return d
    
    for i, (k, v) in enumerate(lista):
        if k == key:
            lista[i].value = (key, value)
            return d
    
    lista.append((key, value))
    return d


def search(d, key):
    tableIndex = hash(key, len(d))
    lista = d[tableIndex]

    if not lista:
        return None
    
    for i, (k, v) in enumerate(lista):
        if k == key:
            return v
    
    return None


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
