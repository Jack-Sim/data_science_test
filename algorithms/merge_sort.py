def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(l, r):
    result = []
    pos = 0

    while len(l) > 0 and len(r) > 0:
        if l[pos] <= r[pos]:
            result += [l[pos]]
            l = rest(l)
        else:
             result += [r[pos]]
             r = rest(r)

    while len(l) > 0:
        result += [l[0]]
        l = rest(l)
    while len(r) > 0:
        result += [r[0]]
        r = rest(r)

    return(result)

def rest(lst):
    if len(lst) == 1:
        return []
    else:
        return lst[1:]

print(merge_sort([7, 5, 1, 10, 1, 2, 3]))
