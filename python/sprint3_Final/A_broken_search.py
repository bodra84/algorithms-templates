# ID 80216715 2 янв 2023, 00:23:47
def broken_search(nums, target):
    """Функция поиска в сломанном массиве."""
    left = 0
    right = len(nums) - 1
    while right >= left:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def read_input():
    """Функция ввода исходных данных."""
    _ = int(input())
    target = int(input())
    nums = [int(x) for x in input().split()]
    return nums, target


def main():
    print(broken_search(*read_input()))


if __name__ == '__main__':
    main()
