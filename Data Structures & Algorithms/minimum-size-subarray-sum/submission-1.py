from _heapq import heapify
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0 
        sm = 0
        k = 10000000000000
        for i in range(len(nums)):
            
            sm += nums[i]
            while sm >= target:
                k = min(k,i-l+1)
                sm -= nums[l]
                l += 1
                
        if k == 10000000000000:
            return 0
        return k
                

            