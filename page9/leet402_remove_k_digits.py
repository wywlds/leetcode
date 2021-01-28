class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count_removed = 0
        s = [0]
        s.append(int(num[0]))
        for i in range(1, len(num)):
            cur_num = int(num[i])
            while cur_num < s[-1] and count_removed < k:
                s.pop()
                count_removed += 1
                if count_removed == k:
                    break
            s.append(cur_num)
        while count_removed < k:
            s.pop()
            count_removed += 1
        while len(s) != 0 and s[0] == 0:
            s.pop(0)
        ans = "0" if len(s) == 0 else "".join([str(n) for n in s])
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.removeKdigits("123456", 2))
    print(solution.removeKdigits("1432219", 3))
    print(solution.removeKdigits("10200", 1))
    print(solution.removeKdigits("10200", 2))
