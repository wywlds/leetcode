class Solution:
    def secondHighest(self, s: str) -> int:
        cnt = [-1] * 10
        for ch in s:
            if ch.isnumeric():
                cnt[int(ch)] = 1
        tmp = 0
        for i in range(9, -1, -1):
            if cnt[i] == 1:
                if tmp == 1:
                    return i
                else:
                    tmp += 1
        return -1

if __name__=="__main__":
    solution = Solution()
    print(solution.secondHighest("dfa12321afd"))