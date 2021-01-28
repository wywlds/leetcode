import collections
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        people_R, people_D, ban_R, ban_D = 0,0,0,0
        q = collections.deque()
        for ch in senate:
            if ch == 'R':
                people_R += 1
            else:
                people_D += 1
            q.append(ch)
        while people_R and people_D:
            per = q.popleft()
            if per == 'R' and ban_R != 0:
                ban_R -= 1
                people_R -= 1
            elif per == 'D' and ban_D != 0:
                ban_D -= 1
                people_D -= 1
            elif per == 'R' and ban_R == 0:
                ban_D += 1
                q.append(per)
            else:
                ban_R += 1
                q.append(per)
        return 'R' if people_R != 0 else 'D'