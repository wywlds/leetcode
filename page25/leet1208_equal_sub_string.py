class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        agg = [0] * (len(s) + 1)
        ans = 0
        p1, p2 = 0, 0
        for i, (sc, tc) in enumerate(zip(s, t)):
            agg[i + 1] = agg[i] + abs(ord(sc) - ord(tc))
            p2 += 1
            while agg[p2] - agg[p1] > maxCost:
                p1 += 1
            ans = max(p2 - p1, ans)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.equalSubstring("abcd", "cdef", 0))