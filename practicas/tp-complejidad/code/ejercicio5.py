
# --- Ejercicio 5
def ContieneSuma(a, n):
    if not a or n == None:
        return False
    
    # Ordenamos la lista
    sortedList = sorted(a)

    leftIndex = 0
    rightIndex = len(sortedList) - 1

    # Recorremos la lista desde ambos extremos
    while leftIndex < rightIndex:
        
        # Suma de números actuales
        numbersSum = sortedList[leftIndex] + sortedList[rightIndex]

        # Si suman 'n', retornamos verdadero
        if numbersSum == n:
            return True
        
        # Si no, incrementamos desde la izquierda o
        # desde la derecha, según corresponda
        if numbersSum < n:
            leftIndex += 1
        else:
            rightIndex += -1
    
    # Si los punteros se encontraron, no hay par que sume 'n'
    # y retornamos falso.
    return False

# --- end

a1 = [5,8,1,3,12,6,3,8,8,10]
a2 = [5,8,1,3,12,6,3,2,8,10]
n = 10

print("La lista " + str(a1) + " contiene dos elementos que suman " + str(n) + ": " + str(ContieneSuma(a1, n)))
print("La lista " + str(a2) + " contiene dos elementos que suman " + str(n) + ": " + str(ContieneSuma(a2, n)))

