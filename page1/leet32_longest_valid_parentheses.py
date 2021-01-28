class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2:
            return 0
        stack = []
        max_count = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                count = 0
                if stack and stack[-1] != ")" and stack[-1] != "(":
                    count += stack.pop()
                if stack and stack[-1] == "(":
                    stack.pop()
                    count += 2
                    max_count = max(count, max_count)
                else:
                    stack.append(ch)
                    continue
                if stack and stack[-1] != ")" and stack[-1] != "(":
                    count += stack.pop()
                    max_count = max(count, max_count)
                stack.append(count)
        return max_count


if __name__=="__main__":
    solution = Solution()
    print(solution.longestValidParentheses(")()())"))
    print(solution.longestValidParentheses("()(()"))
    print(solution.longestValidParentheses("()(())"))