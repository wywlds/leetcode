from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def count(m):
            ans = 0
            while m:
                ans += 1
                m = m & (m - 1)
            return ans
        masks = []
        for s in arr:
            mask = 0
            duplicated = False
            for ch in s:
                digit = ord(ch) - ord('a')
                if mask & (1 << digit):
                    duplicated = True
                    break
                mask |= 1 << digit
            if duplicated:
                continue
            masks.append(mask)
        LEN = len(masks)
        ans = 0
        def backtrack(i, m):
            nonlocal ans
            if i == LEN:
                ans = max(ans, count(m))
                return
            if not (m & masks[i]):
                backtrack(i + 1, m | masks[i])
            backtrack(i + 1, m)
        backtrack(0, 0)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.maxLength(["yy","bkhwmpbiisbldzknpm"]))