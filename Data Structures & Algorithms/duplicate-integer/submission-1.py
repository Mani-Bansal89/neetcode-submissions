class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_duplicates = False
        nums.sort()
        if len(nums)<=1:  # Always remember edge cases
            return has_duplicates
        for idx in range(0,len(nums)-1):
            if nums[idx] == nums[idx+1]:
                has_duplicates = True
                break
        return has_duplicates
        