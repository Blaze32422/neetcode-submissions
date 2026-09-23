class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = 0
        mnm = 1000000000000
        l = 1
        time = 0

        for i in range(len(piles)):
            if piles[i] > mx:
                mx = piles[i]
        while l <= mx:
            time = 0
            mid = (mx + l) // 2
            for i in piles:
                time += math.ceil(i/mid)
            if time <= h:
                if mid < mnm:
                    mnm = mid
                mx = mid - 1
            else:
                l = mid + 1
        return mnm

        
        