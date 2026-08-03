class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numidx = {}
        for idx,num in enumerate(nums):
            numidx[num] = idx

        for idx,num1 in enumerate(nums):
            num2 = target-num1
            if num2 in numidx and numidx[num2]!=idx:
                return [idx,numidx[num2]]
        
                