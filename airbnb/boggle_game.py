from collections import defaultdict


class Node(object):
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_end = True


def max_path(board, words):
    if not board or not board[0]:
        return 0
    trie = Trie()
    for w in words:
        trie.insert(w)
    visited = [[False for _ in xrange(len(board[0]))] for _ in xrange(len(board))]

    def dfs(i, j, node, count):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])) or visited[i][j]:
            return count
        if board[i][j] not in node.children:
            return count
        node = node.children[board[i][j]]
        visited[i][j] = True
        mc = count
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if node.is_end:
                mc = max(dfs(i + dx, j + dy, trie.root, count + 1), mc)
            else:
                mc = max(dfs(i + dx, j + dy, node, count), mc)
        visited[i][j] = False
        return mc

    max_count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            max_count = max(max_count, dfs(i, j, trie.root, 0))
    return max_count


board = [list('abcd'), list('hgie'), list('klmn'), list('opus')]
words = ['abcd', 'eigh', 'klmn', 'supo']
print max_path(board, words)
