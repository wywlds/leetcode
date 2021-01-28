class Solution:
    def knightDialer(self, N: int) -> int:
        mig=[[6,4], [6,8], [7,9],[4,8],[3,9,0],[],[1,7,0], [2,6],[1,3],[2,4]]
        dp_pre = [1] * 10
        dp_next = [0] * 10
        for i in range(N-1):
            for j in range(10):
                dp_next[j] = 0
            for j in range(10):
                for k in mig[j]:
                    dp_next[k] = (dp_next[k] + dp_pre[j]) % (10**9+7)
            tmp = dp_pre
            dp_pre = dp_next
            dp_next = tmp
        return sum(dp_pre)