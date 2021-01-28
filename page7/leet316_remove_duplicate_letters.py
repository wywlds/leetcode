from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        let_counter = Counter(s)
        q = []
        vis = [False] * 26
        for ch in list(s):
            if vis[ord(ch)-ord('a')]:
                let_counter[ch] -= 1
            else:
                while len(q) > 0 and q[-1] > ch and let_counter[q[-1]] > 1:
                    let_counter[q[-1]] -= 1
                    vis[ord(q[-1]) - ord('a')] = False
                    q.pop()
                q.append(ch)
                vis[ord(ch) - ord('a')] = True
        return "".join(q)

if __name__=="__main__":
    solution = Solution()
    print(solution.removeDuplicateLetters("cbacdcbc"))

