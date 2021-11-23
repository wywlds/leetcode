class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1, n + 1))
        cur = -1
        while len(l) != 1:
            cur = (cur + k) % len(l)
            l.pop(cur)
            cur -= 1
        return l[0]

if __name__=="__main__":
    solution = Solution()
    print(solution.findTheWinner(6, 5))