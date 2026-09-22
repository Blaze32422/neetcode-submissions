class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        heap = []
        a = []

        for i in range(len(nums)):
            if nums[i] in hm:
                hm[nums[i]] += 1
            else:
                hm[nums[i]] = 1
        for index,value in hm.items():
            heapq.heappush(heap,(-value,index))
        while k > 0:
            x,y = heapq.heappop(heap)
            a.append(y)
            k = k - 1
        return a



            

        