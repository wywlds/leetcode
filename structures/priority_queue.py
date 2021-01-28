import queue
if __name__=="__main__":
    pq = queue.PriorityQueue()
    pq.put((1, 'a'))
    pq.put((2, 'b'))
    pq.put((3, 'c'))
    pq.put((1, 'b'))
    while pq.queue:
        print(pq.queue[0])
        print(pq.get())