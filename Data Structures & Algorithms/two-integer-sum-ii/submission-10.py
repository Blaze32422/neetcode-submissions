class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(numbers) + 1):
            d = target - numbers[i]
            if d in hm:
                return [hm[d] + 1,i + 1]
            else:
                hm[numbers[i]] = i
        
        