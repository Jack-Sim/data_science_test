def bubble_sort(arr):
    end = len(arr)
    a = arr
    swapped = False
    
    for j in range(-end, -1):
        for i in range(1, end):
            if a[i - 1] > a[i]:
                a[i-1], a[i] = swap(a[i-1], a[i])
                swapped = True
        end -= 1

    return a

def swap(a,b):
    return b, a

print(bubble_sort([6,2,8,1,9,3]))

import numpy as np

arr = np.random.randint(100, size=30)
print(bubble_sort(arr))
