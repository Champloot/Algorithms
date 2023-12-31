from random import randint


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


arr = [randint(-30, 30) for _ in range(20)]
    
print(arr)
print(quick_sort(arr))
