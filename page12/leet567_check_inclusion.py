class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        set1 = list(s1)
        left = 0
        right = 0
        while right < len(s2):
            ch_right = s2[right]
            if ch_right in set1:
                set1.remove(ch_right)
                if right - left + 1 == s1_len:
                    return True
                right += 1
            elif left == right:
                left += 1
                right += 1
            else:
                while left < right:
                    ch_left = s2[left]
                    set1.append(ch_left)
                    left += 1
                    if ch_left == ch_right:
                        break
        return False


if __name__=="__main__":
    solution = Solution()
    print(solution.checkInclusion("abcdxabcde", "abcdeabcdx"))
