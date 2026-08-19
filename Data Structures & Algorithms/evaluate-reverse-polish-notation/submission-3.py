class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                if token == '+':
                    num = nums.pop(-2) + nums.pop(-1)
                elif token == '-':
                    num = nums.pop(-2) - nums.pop(-1)
                elif token == '*':
                    num = nums.pop(-2) * nums.pop(-1)
                else:
                    num = nums.pop(-2) / nums.pop(-1)                          
                nums.append(int(num))
            else:
                nums.append(int(token))
        return nums.pop()
        