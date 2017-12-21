#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0

        if len(p) == 1 or p[1] != '*':
            if len(s) == 0:
                return False
            elif s[0] == p[0] or p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        else:
            if self.isMatch(s, p[2:]):
                    return True
            i = 0
            while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                if self.isMatch(s[i + 1:], p[2:]):
                    return True
                i += 1
        return False

print Solution().isMatch('aa', 'a*')
