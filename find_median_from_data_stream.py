from heapq import *


class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        else:
            return (large[0] - small[0]) / 2.0


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print mf.findMedian()
mf.addNum(3)
print mf.findMedian()
