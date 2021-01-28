from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        sum_clothes = sum(machines)
        LEN = len(machines)
        if sum_clothes % LEN != 0:
            return -1
        avg_clothes = sum_clothes // LEN
        del_clothes = [cnt_cloth - avg_clothes for cnt_cloth in machines]

        agg_count = 0
        max_step = 0
        for del_cloth in del_clothes:
            agg_count += del_cloth
            max_step = max(abs(agg_count), del_cloth, max_step)
        return max_step


if __name__=="__main__":
    solution = Solution()
    print(solution.findMinMoves([1,0,5]))
    print(solution.findMinMoves([0,3,0]))
    print(solution.findMinMoves([0,2,0]))