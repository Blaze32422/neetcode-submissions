class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = []
        for i in range(len(nums)):
            
            if nums[i] in h:
                return True
            else:
                h.append(nums[i])
                k -= 1
            if k < 0:
                k += 1
                h.pop(0)
        return False


