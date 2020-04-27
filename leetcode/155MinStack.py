class MinStack1:

    """
    1。 直接用列表 (leetcode已提交, 这种耗时较高主要是因为没有存最小值)
    2。 用链表 (leetcode已提交)
    3。 用tuple列表
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if self.stack == []:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        if not self.min:
            self.min.append(x)
        elif self.min[-1] >= x:
            self.min.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
if __name__ == '__main__':

    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
