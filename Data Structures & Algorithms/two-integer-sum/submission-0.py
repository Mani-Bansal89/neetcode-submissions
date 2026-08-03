class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for idx1 in range(0,size-1):
            num1 = nums[idx1]
            num2 = target-num1
            for idx2 in range(idx1+1,size):
                if num2 == nums[idx2]:
                    return [idx1,idx2]
                
