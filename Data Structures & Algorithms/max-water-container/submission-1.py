class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        max_amount = 0

        while start<end:
            min_height = min(heights[start], heights[end])
            max_amount = max(max_amount, min_height * (end-start))
            if heights[start] < heights[end]:
                start += 1
            elif heights[start] > heights[end]:
                end -= 1
            else:
                end -= 1

        return max_amount