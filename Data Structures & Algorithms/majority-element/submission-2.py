class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mincnt = len(nums) // 2
        nums.sort()
        maxcnt = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                maxcnt += 1
                if maxcnt > mincnt:
                    return nums[i]
            else:
                maxcnt = 1
        return nums[0]
