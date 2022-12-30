def merge(arr, lf, mid, rg):
    arr1 = arr[lf: mid]
    arr2 = arr[mid: rg]
    k = lf
    l = r = 0
    while l < len(arr1) and r < len(arr2):
        if arr1[l] <= arr2[r]:
            arr[k] = arr1[l]
            l += 1
        else:
            arr[k] = arr2[r]
            r += 1
        k += 1
    while l < len(arr1):
        arr[k] = arr1[l]
        l += 1
        k += 1
    while r < len(arr2):
        arr[k] = arr2[r]
        r += 1
        k += 1
    return arr


def merge_sort(arr, left, right):
    if right - left <= 1:
        return
    else:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()