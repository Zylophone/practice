class Solution(object):
    def addWord(self, d, word, prefix_len):
        abbv = self.getAbbv(word, prefix_len)
        if abbv in d:
            exist = d.pop(abbv)
            pl = self.getCommPrefixLen(word, exist)
            self.addWord(d, word, pl)
            self.addWord(d, exist, pl)
        else:
            d[abbv] = word

    # hadoop 2
    # had2p
    def getAbbv(self, word, prefix_len):
        n = len(word)
        if n - prefix_len < 4:
            return word
        return word[0:prefix_len + 1] + str(n - prefix_len - 2) + word[-1]

    def wordsAbbreviation(self, l):
        """
        :type l: List[str]
        :rtype: List[str]
        """

        d = {}
        for word in l:
            self.addWord(d, word, 0)
        return d.keys()

    def getCommPrefixLen(self, w1, w2):
        for i in range(0, len(w1)):
            if w1[i] != w2[i]:
                return i

        return len(w1)

print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])