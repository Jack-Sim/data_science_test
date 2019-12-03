def quick_sort(arr):

    if len(arr) == 0: return[]

    left, right, pivot = [], [], arr[0]

    for i in range(1,len(arr)):
        if arr[i] < pivot:
            left += [arr[i]]
        else:
            right += [arr[i]]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([6,2,8,1,9,3]))

import numpy as np

arr = np.random.randint(100, size=30)
print(quick_sort(arr))
