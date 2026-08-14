class MinStack:
    def __init__(self):
        self.minstack = []
        self.min_num = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        val = min(val, self.min_num[-1] if self.min_num else val)
        self.min_num.append(val)

    def pop(self) -> None:
        self.minstack.pop()
        self.min_num.pop()
        
    def top(self) -> int:
        return self.minstack[-1]
        
    def getMin(self) -> int:
        return self.min_num[-1]
