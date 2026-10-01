class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        x = 0
        
        for i in nums:
            h.append(-i)
        heapq.heapify(h)  
        
        while k > 1:
            k = k - 1
            x = -(heapq.heappop(h))
        return -(h[0])
    

