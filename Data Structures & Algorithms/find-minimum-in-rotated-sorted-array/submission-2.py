class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        while start < end :
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
            mid = (start + end) // 2
        return nums[mid]
