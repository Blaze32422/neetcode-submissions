class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = len(nums)
        a = [1] * m
        pfix,afix = 1, 1

        for i in range(m):
            a[i] = pfix
            pfix = pfix * nums[i]
        for i in range(m-1,-1,-1):
            a[i] = a[i] * afix
            afix = afix * nums[i]
        return a
    

        
            
            
           
        return a
            
        