from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ans = []
        lasts = {}
        for i, ch in enumerate(S):
            lasts[ch] = i
        start = 0
        end = 0
        for i, ch in enumerate(S):
            if i > end:
                ans.append(end-start+1)
                start, end = i, i
            end = max(lasts[ch], end)
        ans.append(end-start+1)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.partitionLabels("ababcbacadefegdehijhklij"))