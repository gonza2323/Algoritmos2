
# --- Ejercicio 4
def halfSort(L):
    n = len(L)
    middleIndex = (len(L) - 1) // 2
    middle = L[middleIndex]

    # Lista resultado con el mismo elemento del medio
    result = [None] * n
    result[middleIndex] = middle

    # Alternamos entre colocar en izquierda o derecha
    placeLesserOnLeft = False
    placeGreaterOnLeft = False

    # Índices en la lista resultado
    leftIndex = 0
    rightIndex = middleIndex + 1

    for i, v in enumerate(L):
        if i == middleIndex:
            continue

        resultIndex = None
        if v < middle:
            if placeLesserOnLeft:
                resultIndex = leftIndex
                leftIndex += 1
            else:
                resultIndex = rightIndex
                rightIndex += 1
            placeLesserOnLeft = not placeLesserOnLeft
        else:
            if placeGreaterOnLeft:
                resultIndex = leftIndex
                leftIndex += 1
            else:
                resultIndex = rightIndex
                rightIndex += 1
            placeGreaterOnLeft = not placeGreaterOnLeft

        result[resultIndex] = v


    return result
# --- end


a = [2,5,7,4,5,10,6,5,6]
print(a)
print(halfSort(a))


a = [2,5,7,7,5,10,6,5]
print(a)
print(halfSort(a))
