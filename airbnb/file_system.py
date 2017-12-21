import collections


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = collections.defaultdict(Node)
        self.watch = []


class FileSystem(object):
    def __init__(self):
        self.root = Node(None)

    def create(self, path, val):
        paths = path.split('/')
        node = self.root
        for i, p in enumerate(paths):
            if not p:
                continue
            if p not in node.children:
                if i == len(paths) - 1:
                    node.children[p] = Node(val)
                    return True
                else:
                    return False
            else:
                node = node.children[p]
                if node.watch:
                    for func in node.watch:
                        func()
        node.val = val
        return True

    def get(self, path):
        paths = path.split('/')
        node = self.root
        for path in paths:
            if not path:
                continue
            if path in node.children:
                node = node.children[path]
                if node.watch:
                    for func in node.watch:
                        func()
            else:
                return None
        return node.val

    def watch(self, path, func):
        paths = path.split('/')
        node = self.root
        for path in paths:
            if not path:
                continue
            if path in node.children:
                node = node.children[path]
            else:
                return None
        node.watch.append(func)
        return None


def p_yes():
    print 'yes'


def p_no():
    print 'no'

fs = FileSystem()
print fs.create('a', 1)
print fs.get('a')
print fs.create('/a/b', 2)
print fs.get('/a/b')
print fs.create('/c/d', 1)
print fs.get('/c')

fs.watch('/a', p_yes)
fs.watch('/a/b', p_no)
print fs.create('/a/b/c', 1)


