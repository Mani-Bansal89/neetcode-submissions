class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            num3 = nums[i]
            left = i+1
            right = len(nums)-1

            if num3 > 0:
                break
            if i > 0 and num3 == nums[i - 1]:
                continue

            while left<right:
                if nums[left]+nums[right]+num3>0:
                    right-=1
                elif nums[left]+nums[right]+num3<0:
                    left+=1
                else:
                    result.append((num3,nums[left],nums[right]))
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        return result
