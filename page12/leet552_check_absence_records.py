M = 1000000007
class Solution:
    def checkRecord(self, n: int) -> int:
        c = 3
        a1 = 1
        a1l = 0
        a1ll = 0
        l1 = 1
        l2 = 0
        f = 0
        for i in range(2, n+1):
            newc = 3 * c
            newa1 = c + a1 - a1ll - f
            newa1l = a1 - a1ll - a1l
            newa1ll = a1l
            newl1 = c - l1 - f - l2
            newl2 = l1
            newf = 3 * f + l2 + a1
            c = newc % M
            a1 = newa1 % M
            a1l = newa1l % M
            a1ll = newa1ll % M
            l1 = newl1 % M
            l2 = newl2 % M
            f = newf % M
            print ("%d %d %d %d %d %d %d" % (c, a1, a1l, a1ll, l1, l2, f))
        return (c - f) % M

if __name__=="__main__":
    solution = Solution()
    # print(solution.checkRecord(3))
    # print(solution.checkRecord(4))
    print(solution.checkRecord(6))