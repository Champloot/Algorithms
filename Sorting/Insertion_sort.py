from random import randint


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

    return arr


arr = [randint(-30, 30) for _ in range(20)]

print(arr)
print(insertion_sort(arr))
