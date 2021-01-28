from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_1(int_value):
            count = 0
            for i in range(16):
                if int_value & (1 << i):
                    count += 1
            return count * 10000 + int_value

        arr.sort(key=count_1)
        return arr

if __name__=="__main__":
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
    solution = Solution()
    arr = solution.sortByBits(arr)
    print(arr)