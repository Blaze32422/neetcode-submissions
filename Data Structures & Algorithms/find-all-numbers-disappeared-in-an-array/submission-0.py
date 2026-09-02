class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                n.append(i)
        return n
        