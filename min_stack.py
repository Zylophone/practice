class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min_stack or self.stack[self.min_stack[-1]] > x:
            self.min_stack.append(len(self.stack) - 1)

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        self.stack.pop(-1)
        if self.min_stack and self.min_stack[-1] >= len(self.stack):
            self.min_stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.min_stack[-1]]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print ms.getMin()
print ms.pop()
print ms.top()
print ms.getMin()