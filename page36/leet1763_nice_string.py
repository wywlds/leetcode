class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        max_len = 0
        for start in range(len(s)):
            state = 0
            visited = set()
            for end in range(start, len(s)):
                cur_ch = s[end]
                if ord(cur_ch) > ord('Z'):
                    order = ord(cur_ch) - ord('a')
                    if chr(order + ord('A')) not in visited:
                        state |= (1 << order)
                    else:
                        if state & (1 << order):
                            state ^= (1 << order)
                else:
                    order = ord(cur_ch) - ord('A')
                    if chr(order + ord('a')) not in visited:
                        state |= (1 << order)
                    else:
                        if state & (1 << order):
                            state ^= (1 << order)
                visited.add(cur_ch)
                if not state and (end - start + 1) > max_len:
                    max_len = end - start + 1
                    ans = s[start:end + 1]
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.longestNiceSubstring("dDzeE"))
