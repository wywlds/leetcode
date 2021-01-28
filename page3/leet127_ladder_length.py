from typing import List
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        node_dict = collections.defaultdict(list)

        def build_edge(word):
            for i in range(len(word)):
                nword = word[0:i] + "*" + word[i+1:]
                node_dict[nword].append(word)
                node_dict[word].append(nword)

        for word in wordList:
            build_edge(word)
        build_edge(beginWord)

        q = [(1, beginWord)]
        visited = set()
        visited.add(beginWord)
        while len(q) != 0:
            count, cur_word = q.pop(0)
            for nword in node_dict[cur_word]:
                if nword not in visited:
                    if nword == endWord:
                        return count//2 + 1
                    visited.add(nword)
                    q.append((count + 1, nword))
        return 0

if __name__=="__main__":
    solution = Solution()
    print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
