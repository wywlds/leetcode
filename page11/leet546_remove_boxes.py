from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        LEN = len(boxes)
        self.dp = [[[0]*LEN for _ in range(LEN)] for _ in range(LEN)]
        self.boxes = boxes
        return self.helper(0, LEN-1, 0)

    def helper(self, l, r, k):
        if l > r:
            return 0
        if self.dp[l][r][k] != 0:
            return self.dp[l][r][k]
        while l < r and self.boxes[r - 1] == self.boxes[r]:
            r -= 1
            k += 1
        self.dp[l][r][k] = self.helper(l, r-1, 0) + (k+1)*(k+1)
        for i in range(l, r+1):
            if self.boxes[i] == self.boxes[r]:
                self.dp[l][r][k] = max(self.dp[l][r][k], self.helper(l, i, k+1) + self.helper(i+1, r-1, 0))
        return self.dp[l][r][k]