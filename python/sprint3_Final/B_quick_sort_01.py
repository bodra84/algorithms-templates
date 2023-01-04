def partition(array, pivot):
    left = 0
    right = len(array) - 1
    while left <= right:
        if array[left] >= array[right] >= array[pivot]:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1
        elif array[left] <= array[right] <= array[pivot]:
            array[right], array[pivot] = array[pivot], array[right]
            pivot = right
            right -= 1
            left += 1
        elif array[left] >= array[pivot] >= array[right]:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
        else:
            left += 1
            right -= 1
    return left, right


def quick_sort(array):
    for _ in range(5):
        n = len(array) - 1
        mid = n // 2
        if array[0] < array[mid] < array[n]:
            pivot = mid
        elif array[n] >= array[0] <= array[mid]:
            pivot = 0
        else:
            pivot = n
        array = partition(array, pivot)
    return array

array = [4, 8, 9, 20, 1, 5, 3, 10]
# n = len(array) - 1
# mid = n // 2
# if array[0] < array[mid] < array[n]:
#     pivot = mid
# elif array[n] >= array[0] <= array[mid]:
#     pivot = 0
# else:
#     pivot = n
print(partition(array, 5))
# print(quick_sort(array))
