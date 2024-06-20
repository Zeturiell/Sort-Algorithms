import random
import time

def particao(array, inicio, final):
    pivo = array[final]
    i = inicio - 1
    for j in range(inicio, final):
        if array[j] <= pivo:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[final] = array[final], array[i + 1]
    return i + 1

def quick_sort(array, inicio, final):
    if inicio < final:
        posicao = particao(array, inicio, final)
        # Ordena a metade esquerda
        quick_sort(array, inicio, posicao - 1)
        # Ordena a metade direita
        quick_sort(array, posicao + 1, final)
    return array

arr =[]
for i in range(10000):
    var = random.randint(1,10000)
    if var in arr:
        while var in arr:
            var = random.randint(1,10000)
    else:
        arr.append(var)
    

inicio = time.time()
organizado = quick_sort(arr, 0, len(arr) - 1)
fim = time.time()

#print("Array ordenado:", organizado)
print("Quick sort levou ",fim - inicio," segundos")