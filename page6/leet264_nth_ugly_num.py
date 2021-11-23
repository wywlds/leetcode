class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        i2, i3, i5 = 0, 0, 0
        while len(l) != n:
            next2 = 2 * l[i2]
            next3 = 3 * l[i3]
            next5 = 5 * l[i5]
            min_next = min(next2, next3, next5)
            if next2 == min_next:
                if next2 != l[-1]:
                    l.append(next2)
                i2 += 1
            elif next3 == min_next:
                if next3 != l[-1]:
                    l.append(next3)
                i3 += 1
            else:
                if next5 != l[-1]:
                    l.append(next5)
                i5 += 1
        return l[-1]

