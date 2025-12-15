class MinStack:
    def __init__(self):
        self.s = []
        self.min = []
    
    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.min) == 0 or val <= self.min[-1]:
            self.min.append(val)
    
    def pop(self) -> None:
        top_val = self.s.pop()
        if top_val == self.min[-1]:
            self.min.pop()
    
    def top(self) -> int:
        return self.s[-1]
    
    def getMin(self) -> int:
        return self.min[-1]
    

if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
