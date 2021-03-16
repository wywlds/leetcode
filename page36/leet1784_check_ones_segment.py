class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        import re
        splits = re.split(s, "0+")
        cnt = 0
        for split in splits:
            if len(split) > 0:
                cnt += 1
        return cnt == 1