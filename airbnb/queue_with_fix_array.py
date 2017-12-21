class Node(object):
    def __init__(self, size):
        self.arr = [None] * size
        self.next = None


class Queue(object):
    def __init__(self):
        self.size = 10
        self.write_node = self.read_node = Node(self.size)
        self.write_idx = 0
        self.read_idx = 0

    def push(self, val):
        if self.write_idx >= len(self.write_node.arr):
            node = Node(self.size)
            self.write_node.next = node
            self.write_node = self.write_node.next
            self.write_idx = 0
        self.write_node.arr[self.write_idx] = val
        self.write_idx += 1

    def pop(self):
        if not self.read_node:
            return None
        if self.read_idx >= len(self.read_node.arr):
            self.read_node = self.read_node.next
            self.read_idx = 0

        if self.read_node:
            result = self.read_node.arr[self.read_idx]
            self.read_idx += 1
            return result
        else:
            return None

queue = Queue()
for i in range(15):
    queue.push(i)

for i in range(8):
    print queue.pop()

for i in range(15, 20):
    queue.push(i)

for i in range(20):
    print queue.pop()