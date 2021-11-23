import bisect
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

def binary_search_right(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return right

def binary_search_left(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

if __name__=="__main__":
    l = [1,2,3,3,5]
    print(binary_search_right(l, 3))
    print(binary_search_left(l, 3))
    # print(binary_search(l, 6))
    # print(binary_search_right(l, 6))
    # print(binary_search_right(l, 5))
    # print(binary_search_right(l, 4))
    # print(binary_search_right(l, 3))
    # print(binary_search_right(l, 0))
    # print(binary_search_left(l, 4))
    # print(binary_search_left(l, 5))
    # print(binary_search_left(l, 0))
    # print(binary_search_left(l, 3))
    # print(binary_search_left(l, 6))
    #
    # print(binary_search_right(l, 3))
    # print(binary_search_left(l, 3))