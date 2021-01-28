class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 1
        longest_start = 0
        longest_end = 0
        for core in range(len(s)):
            start = core - 1
            end = core + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    leng = end - start + 1
                    if leng > longest_len:
                        longest_start = start
                        longest_end = end
                        longest_len = leng
                    start -= 1
                    end += 1
                else:
                    break
            start = core
            end = core + 1
            while start >= 0 and end < len(s):
                if s[start] == s[end]:
                    leng = end - start + 1
                    if leng > longest_len:
                        longest_start = start
                        longest_end = end
                        longest_len = leng
                    start -= 1
                    end += 1
                else:
                    break
        return s[longest_start:longest_end + 1]

if __name__=="__main__":
    solution = Solution()
    result = solution.longestPalindrome("babab")
    print(result)