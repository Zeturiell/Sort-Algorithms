import random
import time

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
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
organizado = bubble_sort(arr)
fim = time.time()

#print("Array ordenado:", organizado)
print("Bubble Sort levou ",fim - inicio," segundos")
