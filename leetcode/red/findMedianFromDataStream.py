import heapq
class MedianFinder:

    def __init__(self):
        
        # two heaps - large and small
        # heaps shoud be roughly same size

        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num) # to get the maxheap = small heap

        # make sure every element in small is <= every num in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

            # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# ...existing code...

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    print("Median after adding 1:", mf.findMedian())  # Expected: 1

    mf.addNum(2)
    print("Median after adding 2:", mf.findMedian())  # Expected: 1.5

    mf.addNum(3)
    print("Median after adding 3:", mf.findMedian())  # Expected: 2

    mf2 = MedianFinder()
    for num in [5, 15, 1, 3]:
        mf2.addNum(num)
    print("Median after adding [5, 15, 1, 3]:", mf2.findMedian())  # Expected: 4.0