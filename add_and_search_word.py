class WordDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        d = self.trie
        self.addToTrie(word, d)

    def addToTrie(self, word, d):
        if len(word) == 0:
            d['_end_'] = '_end_'
            return

        if word[0] not in d:
            d[word[0]] = {}
        return self.addToTrie(word[1:], d[word[0]])

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchInTrie(word, self.trie)

    def searchInTrie(self, word, d):
        if len(word) == 0:
            return '_end_' in d
        if word[0] == '.':
            for c in d:
                if c == '_end_':
                    continue
                if self.searchInTrie(word[1:], d[c]):
                    return True
        elif word[0] in d:
            return self.searchInTrie(word[1:], d[word[0]])

        return False




        # Your WordDictionary object will be instantiated and called as such:
        # obj = WordDictionary()
        # obj.addWord(word)
        # param_2 = obj.search(word)
