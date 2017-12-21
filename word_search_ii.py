import collections


class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_end = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for c in word:
            root = root.children[c]
        root.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for c in word:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return root.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for c in prefix:
            if c in root.children:
                root = root.children[c]
            else:
                return False
        return True

    def delete(self, word):
        node = self.root
        queue = []
        for letter in word:
            queue.append((letter, node))
            child = node.children.get(letter)
            if not child:
                return False
            node = child

        if not node.is_end:
            return False
        if node.children:
            node.is_end = False
        else:
            for letter, node in reversed(queue):
                del node.children[letter]
                if node.children or node.is_end:
                    break
        return True




class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        visited = [[False for _ in range(n)] for _ in range(m)]
        result = set()

        def dfs(i, j, prefix):
            if not (0 <= i < m and 0 <= j < n and not visited[i][j]):
                return

            visited[i][j] = True
            prefix += board[i][j]
            if trie.startsWith(prefix):
                if trie.search(prefix):
                    result.add(prefix)
                    trie.delete(prefix)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    dfs(dx + i, dy + j, prefix)
            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                dfs(i, j, '')
        return list(result)


print Solution().findWords([
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
], ["oath", "pea", "eat", "rain"])
