from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count_dic = {}
        agg_dic = {}
        count_dic[0] = 1
        agg_dic[0] = 0

        agg = 0
        ans = 0
        for i, a in enumerate(arr):
            agg ^= a
            if agg in count_dic:
                cnt = count_dic[agg]
                agg_index = agg_dic[agg]
                ans += (cnt * i - agg_index)
                count_dic[agg] = (cnt + 1)
                agg_dic[agg] = agg_index + i + 1
            else:
                count_dic[agg] = 1
                agg_dic[agg] = i + 1
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.countTriplets([7,11,12,9,5,2,7,17,22]))