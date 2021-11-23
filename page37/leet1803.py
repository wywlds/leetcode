from typing import List

class Trie(object):
    def __init__(self):
        self.mem = {}

    def add(self, s):
        cur = self.mem
        for ch in s:
            if '#' not in cur:
                cur['#'] = 1
            else:
                cur['#'] += 1
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        if '#' not in cur:
            cur['#'] = 1
        else:
            cur['#'] += 1

def query(num, limit, i, cur):
    if i == -1:
        return cur['#']
    ans = 0
    q = 1 << i
    ch = num[16-i]
    if ch == '1':
        och = '0'
    else:
        och = '1'
    if q > limit:
        if ch in cur:
            ans += query(num, limit, i - 1, cur[ch])
    else:
        if ch in cur:
            ans += cur[ch]['#']
        if och in cur:
            ans += query(num, limit - q, i-1, cur[och])
    return ans


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def to_str(num):
            res = []
            for i in range(17):
                res.append(str(num % 2))
                num >>= 1
            return res[::-1]
        trie = Trie()
        resl = 0
        resh = 0
        for num in nums:
            num_str = to_str(num)
            resl += query(num_str, low - 1, 16, trie.mem)
            resh += query(num_str, high, 16, trie.mem)
            trie.add(num_str)
        return resh - resl

if __name__=="__main__":
    nums = [1,4,2,7]
    low = 2
    high = 6
    solution = Solution()
    print(solution.countPairs(nums, low, high))