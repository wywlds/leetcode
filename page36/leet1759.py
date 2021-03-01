import collections
class Solution:
    def cnt_s(self, s):
        return s * (s + 1) // 2

    def countHomogenous(self, s: str) -> int:
        cnt = collections.Counter()
        start = 0

        base = 10 ** 9 + 7
        for i, ch in enumerate(s):
            if ch != s[start]:
                cnt[(s[start], i - start)] += 1
                start = i
        cnt[(s[start], len(s) - start)] += 1
        ans = 0
        for (v, s), c in cnt.items():
            ans = (ans + self.cnt_s(s) * c ) % base
        return ans

if __name__=="__main__":
    s = "xxyxx"
    # s = "gguuxxooowjjjjjjjjkswxxhhhhhhhzzzzzzzzrrrrrrrrrrrrrrrrrrrrr"
    solution = Solution()
    print(solution.countHomogenous(s))