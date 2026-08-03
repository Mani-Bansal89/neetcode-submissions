class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numidx = {}
        for idx,num in enumerate(nums):
            if num in numidx:
                numidx[num].append(idx)
            else:
                numidx[num] = [idx]
        for num1 in nums:
            num2 = target-num1
            if num2 in numidx:
                if num1 == num2 and len(numidx[num1])>1:
                    return [numidx[num1][0],numidx[num1][1]]
                if num1 != num2:
                    return [numidx[num1][0],numidx[num2][0]]
        
                