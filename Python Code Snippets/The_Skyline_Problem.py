def getSkyline(buildings):
    import heapq
    events=[]
    for left,right,height in buildings:
        events.append((left,-height,right))
        events.append((right,0,0))
    events.sort()
    result=[]
    heap=[(0,float('inf'))]
    for x,neg_height,right in events:
        while x>=heap[0][1]:
            heapq.heappop(heap)
        if neg_height:
            heapq.heappush(heap,(neg_height,right))
        if not result or result[-1][1]!=-heap[0][0]:
            result.append([x,-heap[0][0]])
    return result