class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num1 in enumerate(numbers):
            num2 = target - num1
            if num2 in seen:
                return [seen[num2][0], i + 1]
            else:
                seen[num1] = [i + 1]
            



