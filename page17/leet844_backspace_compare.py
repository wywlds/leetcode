class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def parse(s):
            ans = []
            for ch in s:
                if ch == '#':
                    if len(ans) >= 1:
                        ans.pop()
                else:
                    ans.append(ch)
            return "".join(ans)
        return parse(S) == parse(T)


if __name__=="__main__":
    solution = Solution()
    print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))