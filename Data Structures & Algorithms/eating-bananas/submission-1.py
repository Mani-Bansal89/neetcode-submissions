class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        minnum = end

        while start <= end:
            k = (start + end) // 2
            i = 0
            total_hrs = 0
            while i < len(piles):
                total_hrs += math.ceil(float(piles[i])/k)
                i += 1
            if total_hrs <= h:
                minnum = k
                end = k - 1
            else:
                start = k + 1
        return minnum