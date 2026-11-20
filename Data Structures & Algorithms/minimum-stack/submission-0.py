class MinStack:

    def __init__(self):
        self.list = []
        self.minimun = []

    def push(self, val: int) -> None:
        self.list.append(val)
        self.minimun.append(val)
        self.minimun = sorted(self.minimun)

    def pop(self) -> None:
        if self.list:
            pop_val = self.list.pop()
            self.minimun.remove(pop_val)
            sorted(self.minimun)
        
    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        if self.minimun: return self.minimun[0]
        return -1
