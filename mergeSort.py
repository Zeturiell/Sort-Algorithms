import random
import time

def merge_sort(array):
    # Divisão do Array
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        # Chama merge_sort recursivamente para a metade esquerda e direita
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Ordena esquerda e direita
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Ordenação final
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

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
organizado = merge_sort(arr)
fim = time.time()

#print("Array ordenado:", organizado)
print("Merge sort levou ",fim - inicio," segundos")
