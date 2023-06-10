def bubbleSort_tertinggi(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubbleSort_terendah(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


data = [100, 95, 90]

print(bubbleSort_tertinggi(data))
print(bubbleSort_terendah(data))
