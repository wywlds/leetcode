from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_a = 0
        set_a = set()
        for a in A:
            sum_a += a
            set_a.add(a)

        sum_b = 0
        set_b = set()
        for b in B:
            sum_b += b
            set_b.add(b)

        for a in A:
            if (a - (sum_a - sum_b) // 2) in set_b:
                return [a, a - (sum_a - sum_b)//2]
        return []

if __name__=="__main__":
    A = [1,2,5]
    B = [2,4]
    solution = Solution()
    print(solution.fairCandySwap(A, B))