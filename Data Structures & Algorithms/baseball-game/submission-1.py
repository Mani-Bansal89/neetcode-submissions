class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i, operation in enumerate(operations):
            if operation == '+':
                result.append(result[-1] + result[-2])
            elif operation == 'C':
                result.pop()
            elif operation == 'D':
                result.append(result[-1] * 2)
            else:
                result.append(int(operation))
        return sum(result)