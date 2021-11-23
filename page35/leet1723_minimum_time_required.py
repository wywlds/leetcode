from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        l, r = jobs[0], sum(jobs)

        def backtrack(works, i, m):
            if i == len(jobs):
                return True
            cur = jobs[i]
            for j in range(len(works)):
                if works[j] + cur <= m:
                    works[j] += cur
                    if backtrack(works, i + 1, m):
                        return True
                    works[j] -= cur
                if works[j] == 0:
                    return False
            return False

        def check(m):
            works = [0] * k
            return backtrack(works, 0, m)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l

if __name__=="__main__":
    jobs = [6518448,8819833,7991995,7454298,2087579,380625,4031400,2905811,4901241,8480231,7750692,3544254]
    k = 4
    solution = Solution()
    print(solution.minimumTimeRequired(jobs, k))