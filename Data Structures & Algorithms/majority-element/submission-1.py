class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        count = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] in counter:
                if counter[nums[i]] + 1 > count:
                    return nums[i]
                else:
                    counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        return nums[0]
