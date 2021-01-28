class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        new_words = [word[::-1] for word in words]
        return " ".join(new_words)


if __name__=="__main__":
    solution = Solution()
    print(solution.reverseWords("beijing is a greet city"))