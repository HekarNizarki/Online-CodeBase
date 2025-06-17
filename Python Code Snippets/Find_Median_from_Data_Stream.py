import heapq

class MedianFinder:
    def __init__(self):
        self.small=[]  # Max heap (using negative values)
        self.large=[]  # Min heap
    def addNum(self,num):
        heapq.heappush(self.small,-num)
        heapq.heappush(self.large,-heapq.heappop(self.small))
        if len(self.small)<len(self.large):
            heapq.heappush(self.small,-heapq.heappop(self.large))
    def findMedian(self):
        if len(self.small)>len(self.large):
            return -self.small[0]
        return (-self.small[0]+self.large[0])/2