class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        is_present = {}
        for num in nums:
            is_present[num] = 1
        longest_cons = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in is_present:
                start_num = nums[i]
                cons_count = 0
                while start_num in is_present:
                    cons_count += 1
                    start_num += 1      
                    longest_cons = max(longest_cons, cons_count)        
        return longest_cons
