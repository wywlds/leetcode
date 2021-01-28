def binary_search_right(nums):
    left, right = 0, len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if mid != 0 and nums[mid] < nums[mid - 1]:
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return left

if __name__=="__main__":
    q1 = [1,2,3,4,5,6]
    q2 = [6,5,4,3,2,1]
    q3 = [1,2,3,2,1]
    print(binary_search_right(q1))
    print(binary_search_right(q2))
    print(binary_search_right(q3))