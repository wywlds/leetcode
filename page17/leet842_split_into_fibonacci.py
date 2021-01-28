from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        def dfs(index):
            if index == len(S):
                return len(ans) >= 3
            # 当前等于0的特殊情况
            if S[index] == '0':
                if len(ans) < 2 or ans[-1] + ans[-2] == 0:
                    ans.append(0)
                    if dfs(index + 1):
                        return True
                    ans.pop()
                    return False
            curr = 0
            for i in range(index, len(S)):
                curr = curr * 10 + ord(S[i]) - ord('0')
                if curr > 2 ** 31 - 1:
                    return False
                if len(ans) < 2 or ans[-1] + ans[-2] == curr:
                    ans.append(curr)
                    if dfs(i + 1):
                        return True
                    ans.pop()
                elif len(ans) >= 2 and ans[-1] + ans[-2] < curr:
                    return False

            return False
        if dfs(0):
            return ans
        else:
            return []

if __name__=="__main__":
    solution = Solution()
    #print(solution.splitIntoFibonacci("000000"))
    print(solution.splitIntoFibonacci("123456579"))

