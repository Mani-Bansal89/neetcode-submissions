class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        front_arr = [1] * len(nums)
        back_arr = [1] * len(nums)
        for i in range(1,len(nums)):
            front_arr[i] = front_arr[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            back_arr[i] = back_arr[i+1] * nums[i+1]

        return [front_arr[i] * back_arr[i] for i in range(len(front_arr))]
        
