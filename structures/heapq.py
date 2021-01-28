import heapq
if __name__ == "__main__":
    q = [(1, 'a'), (2, 'b'), (3, 'c'), (1, 'b')]
    heapq.heapify(q)
    print(q)

    # 获取堆顶
    print(heapq.heappop(q))
    print(q)
    # 推给堆
    heapq.heappush(q, (5, 'a'))
    print(q)

    while q:
        print(q[0])
        print(heapq.heappop(q))

