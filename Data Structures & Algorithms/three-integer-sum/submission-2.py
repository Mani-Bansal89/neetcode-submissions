class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            num3 = nums[i]
            while left<right:
                if nums[left]+nums[right]+num3>0:
                    right-=1
                elif nums[left]+nums[right]+num3<0:
                    left+=1
                elif nums[left]+nums[right]+num3==0:
                    result.add((num3,nums[left],nums[right]))
                    left+=1
                    right-=1

        output = []
        for item in result:
            output.append(item)
        return output
