class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for ch in S:
            if len(s) == 0 or s[-1] != ch:
                s.append(ch)
            elif s[-1] == ch:
                s.pop()
        return "".join(s)


if __name__=="__main__":
    solution = Solution()
    print(solution.removeDuplicates("abbaca"))