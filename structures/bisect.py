import bisect

if __name__=="__main__":
    a = [(1, 'a'), (2, 'b'), (3, 'c')]
    print(bisect.bisect_right(a, (2, 'c')))
    print((2, 'b') < (2, 'c'))
    tuple