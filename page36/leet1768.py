class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            ans.append(word1[i])
            ans.append(word2[i])
        return "".join(ans) + word1[min_len:] + word2[min_len:]


if __name__=="__main__":
    solution = Solution()
    print(solution.mergeAlternately("abcd", "pg"))