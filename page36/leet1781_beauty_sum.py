class Solution:
    def beautySum(self, s: str) -> int:
        counter = [0] * 26
        max_c = 0
        min_c = float('inf')
        min_chi = -1
        sum_max = 0
        sum_min = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                chi = ord(s[j]) - ord('a')
                counter[chi] += 1
                if counter[chi] > max_c:
                    max_c = counter[chi]
                if chi == min_chi or counter[chi] < min_c:
                    min_c = counter[chi]
                    min_chi = chi
                    for chs, x in enumerate(counter):
                        if x != 0 and x < min_c:
                            min_c = x
                            min_chi = chs
                sum_max += max_c
                sum_min += min_c
            for k in range(26):
                counter[k] = 0
            max_c = 0
            min_c = float('inf')
            min_chi = -1
        return sum_max - sum_min