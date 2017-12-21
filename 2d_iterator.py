class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i, self.j = 0, 0
        self.hasNext()
        self.prev_idx = (-1, -1)

    def next(self):
        """
        :rtype: int
        """
        result = self.vec2d[self.i][self.j]
        self.prev_idx = (self.i, self.j)
        self.j += 1
        return result

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.i < len(self.vec2d) and (not 0 <= self.j < len(self.vec2d[self.i])):
            self.i += 1
            self.j = 0
        return self.i < len(self.vec2d)

    def remove(self):
        if self.prev_idx == (-1, -1):
            return
        self.vec2d[self.prev_idx[0]].pop(self.prev_idx[1])
        if self.prev_idx[0] == self.i:
            self.j -= 1


arr = Vector2D([[1, 2], [3], [4, 5, 6]])
while arr.hasNext():
    print arr.next()
arr.remove()
print arr.vec2d
