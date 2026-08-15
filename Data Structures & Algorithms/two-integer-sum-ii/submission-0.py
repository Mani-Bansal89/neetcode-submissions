class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            if num not in seen:
                seen[num] = [i]
            else:
                seen[num].append(i)
        for i, num1 in enumerate(numbers):
            num2 = target - num1
            if num2 in seen:
                if i not in seen[num2]:
                    return [i + 1 , seen[num2][0] + 1]
                elif i in seen[num2] and len(seen[num2])>1:
                    return [i + 1, seen[num2][1] + 1]
            



