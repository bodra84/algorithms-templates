def insertion_sort(array):  #сортировка вставкой
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert
        print(f'step {i}, sorted {i+1} elements: {array}')


def select_sort(A):  #сортировка выбором
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[k], A[i] = A[i], A[k]
    print(A)


insertion_sort([11, 2, 9, 7, 1])
select_sort([70, 2, 9, 7, 1])


