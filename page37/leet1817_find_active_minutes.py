from typing import List

from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_set = set()
        ac_counter = defaultdict(lambda: 0)
        for log in logs:
            if tuple(log) not in user_set:
                ac_counter[log[0]] += 1
                user_set.add(tuple(log))
        ans = [0] * k
        for _, c in ac_counter.items():
            ans[c - 1] += 1
        return ans