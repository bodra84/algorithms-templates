def broken_search(nums, target, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    if right < left:
        return -1
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target <= nums[right]:
        return broken_search(nums, target, mid + 1, right)
    elif nums[mid] < target >= nums[left]:
        return broken_search(nums, target, left, mid)
    elif nums[mid] > target <= nums[right]:
        return broken_search(nums, target, mid + 1, right)
    else:
        return broken_search(nums, target, left, mid)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


def read_input():
    """Функция ввода исходных данных."""
    _ = int(input())
    target = int(input())
    nums = [int(x) for x in input().split()]
    return nums, target


def main():
    print(broken_search(*read_input()))
    # test()


if __name__ == '__main__':
    main()
