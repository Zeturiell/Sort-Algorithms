import random
import time

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marcado = array[i]
        j = i - 1
        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marcado
    return array

arr = []
for i in range(10000):
    var = random.randint(1,10000)
    if var in arr:
        while var in arr:
            var = random.randint(1,10000)
    else:
        arr.append(var)
    

inicio = time.time()
organizado = insertion_sort(arr)
fim = time.time()

#print("Array ordenado:", organizado)
print("Insertion Sort levou ",fim - inicio," segundos")
