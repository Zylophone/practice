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



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)

trie = Trie()
trie.insert('abcde')
trie.insert('abc')
print trie.search('abcd')
print trie.startsWith('abcd')