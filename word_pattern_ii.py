class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        m = {}
        s = set()

        def is_match(pattern, str):
            if not pattern:
                return not str

            c = pattern[0]
            if c in m:
                if str.startswith(m[c]):
                    return is_match(pattern[1:], str[len(m[c]):])
                else:
                    return False
            else:
                for i in range(1, len(str) + 1):
                    item = str[:i]
                    if item in s:
                        continue
                    rest = str[i:]
                    m[c] = item
                    s.add(item)
                    if is_match(pattern[1:], rest):
                        return True
                    del m[c]
                    s.remove(item)
            return False
        return is_match(pattern, str)
print Solution().wordPatternMatch('d', 'e')