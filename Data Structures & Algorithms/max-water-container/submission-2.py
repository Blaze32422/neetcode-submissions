class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        s =  0
        while l < r:
            s = max(s,(r - l) * min(heights[l],heights[r])) 
            if heights[r] > heights[l]:
                l +=1
            else:
                r = r - 1
        return s
        

        