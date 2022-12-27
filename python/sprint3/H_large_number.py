def large_num(num):
    return num


def large_num_comp(num1, num2):
    return num1+num2 > num2+num1


def insertion_sort_by_key(array, key):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and key(item_to_insert, array[j-1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return print(''.join(array))


def read_input():
    _ = int(input())
    data = input().split()
    return data


def main():
    arr = read_input()
    insertion_sort_by_key(arr, large_num_comp)


if __name__ == '__main__':
    main()
