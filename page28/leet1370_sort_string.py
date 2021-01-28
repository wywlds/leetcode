from collections import Counter
import heapq
class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        l1 = []
        for w, c in counter.items():
            l1.append((w, c))
        l1.sort()
        ans = []
        while len(l1) != 0:
            l2 = []
            for w, c in l1:
                ans.append(w)
                if c > 1:
                    l2.append((w, c-1))
            l1 = l2
            l1.reverse()
        return "".join(ans)


if __name__=="__main__":
    solution = Solution()
    print(solution.sortString("ggggg"))
    print(solution.sortString("aaaabbbbcccc"))