class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        cnts = [0] * 26
        ans = 0
        max_cnt = 0
        while end != len(s):
            i = ord(s[end]) - ord('A')
            cnts[i] = cnts[i] + 1
            max_cnt = max(cnts[i], max_cnt)
            if end - start + 1 - max_cnt <= k:
                ans = max(ans, end - start + 1)
            else:
                i = ord(s[start]) - ord('A')
                start += 1
                cnts[i] -= 1
            end += 1
        return ans

if __name__=="__main__":
    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))
