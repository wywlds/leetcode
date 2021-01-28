class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        BS = ""
        num = len(B) // len(A)
        for n in range(num + 2):
            BS += A
            if B in BS:
                return n
        return -1