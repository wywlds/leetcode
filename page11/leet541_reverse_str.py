class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k == 1:
            return s
        result_str = ""

        start = 0
        while start + 2 * k <= len(s):
            result_str += s[start:start+k][::-1]
            result_str += s[start + k : start + 2 * k]
            start = start + 2 * k

        if start + k > len(s):
            result_str += s[start:][::-1]
        else:
            result_str += s[start:start + k][::-1]
            result_str += s[start +k:]
        return result_str


if __name__=="__main__":
    solution = Solution()
    print(solution.reverseStr("abcdefg", 2))