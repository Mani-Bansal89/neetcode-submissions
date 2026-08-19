class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                num1 = nums.pop()
                num2 = nums.pop()
                if token == '+':
                    num = num2 + num1
                elif token == '-':
                    num = num2 - num1
                elif token == '*':
                    num = num2 * num1
                else:
                    num = num2 / num1                         
                nums.append(int(num))
            else:
                nums.append(int(token))
        return nums.pop()
        