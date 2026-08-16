class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)

        while start < end:
            if nums[start] == val:
                end -= 1
                nums[start] = nums[end]  
            else:
                start += 1
        return end