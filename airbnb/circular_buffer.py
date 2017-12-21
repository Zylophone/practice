class Buffer(object):
    def __init__(self, size):
        self.buffer = [None] * (size + 1)
        self.head, self.tail = 0, 0

    def add(self, o):
        if self.tail == (self.head + 1) % len(self.buffer):
            return False
        self.buffer[self.head] = o
        self.head = (self.head + 1) % len(self.buffer)
        return True

    def get(self):
        if self.tail == self.head:
            return None
        res = self.buffer[self.tail]
        self.tail += 1
        self.tail %= len(self.buffer)
        return res

buffer = Buffer(3)
print buffer.add(1)
print buffer.add(2)
print buffer.add(3)
print buffer.add(4)

print buffer.get()
print buffer.get()
print buffer.get()
print buffer.get()




