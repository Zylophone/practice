import collections


class TrieNode(object):
    def __init__(self):
        self.sentences = set()
        self.children = collections.defaultdict(TrieNode)


class AutocompleteSystem(object):
    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.root = TrieNode()
        self.buffer = ''
        self.node = self.root
        self.time_mapping = collections.Counter()
        for s, time in zip(sentences, times):
            self.add_sentence(s)
            self.time_mapping[s] = time

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c != '#':
            self.buffer += c
            self.node = self.node.children[c]
            ans = sorted(self.node.sentences, key=lambda x: (-self.time_mapping[x], x))[:3]
            return ans
        else:
            self.add_sentence(self.buffer)
            self.time_mapping[self.buffer] += 1
            self.buffer = ''
            self.node = self.root
            return []

    def add_sentence(self, sentence):
        node = self.root
        for letter in sentence:
            node = node.children[letter]
            node.sentences.add(sentence)

