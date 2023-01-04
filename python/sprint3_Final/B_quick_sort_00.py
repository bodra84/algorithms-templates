def partition(array, pivot):
    left, center, right = [], [], []
    for i in range(len(array)):
        if int(array[i]) < int(pivot):
            left.append(array[i])
        elif int(array[i]) > int(pivot):
            right.append(array[i])
        else:
            center.append(array[i])
    return left, center, right


def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        mid = len(array) // 2
        if array[0] < array[mid] < array[-1]:
            pivot = array[mid]
        elif array[mid] <= array[0] < array[-1]:
            pivot = array[0]
        else:
            pivot = array[-1]
        left, center, right = partition(array, pivot)
        return quick_sort(left) + center + quick_sort(right)


arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
drt = quick_sort(arr)
print(drt)
