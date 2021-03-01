from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        LEN = len(s)
        if k == 1:
            return LEN
        ans = 0

        LEN_S = len(set(s))
        for t in range(1, LEN_S + 1):
            l, r = 0, 0
            cnt = Counter()
            less = 0
            tot = 0
            while r < LEN:
                cnt[s[r]] += 1
                if cnt[s[r]] == 1:
                    less += 1
                    tot += 1
                if cnt[s[r]] == k:
                    less -= 1
                while tot > t:
                    cnt[s[l]] -= 1
                    if cnt[s[l]] == 0:
                        less -= 1
                        tot -= 1
                    if cnt[s[l]] == k - 1:
                        less += 1
                    l += 1
                if less == 0:
                    ans = max(ans, r - l + 1)
                r += 1
        return ans

if __name__=="__main__":
    s = "ababbc"
    k = 2
    solution = Solution()
    print(solution.longestSubstring(s, k))