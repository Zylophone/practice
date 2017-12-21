class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s
        if p[0] != '*':
            if not s or s[0] != p[0] or p[0] != '?':
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            for i in range(0, len(s) + 1):
                if self.isMatch(s[i:], p[1:]):
                    return True
            return False
