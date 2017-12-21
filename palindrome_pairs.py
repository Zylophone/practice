class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = set()
        m = {}
        for i, word in enumerate(words):
            m[word] = i

        for i, word in enumerate(words):
            for n in range(0, len(word) + 1):
                s1 = word[0:n]
                s2 = word[n:]
                if self.isPalindrome(s1):
                    rev_s2 = s2[::-1]
                    if rev_s2 in m and m[rev_s2] != i:
                        result.add((m[rev_s2], i))

                if self.isPalindrome(s2):
                    rev_s1 = s1[::-1]
                    if rev_s1 in m and m[rev_s1] != i:
                        result.add((i, m[rev_s1]))
        return list(result)

    def isPalindrome(self, s):
        for i in range(0, len(s) / 2):
            if s[i] != s[-i - 1]:
                return False
        return True
