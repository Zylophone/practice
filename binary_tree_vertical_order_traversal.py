#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import collections

logger = logging.getLogger(__name__)


# Time:  O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                queue += [(root.left, i - 1), (root.right, i + 1)]
                cols[i] = node.val
        return [cols[i] for i in range(min(cols.keys()), max(cols.keys()) + 1)] if cols else []


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s, %(name)s %(levelname)s %(message)s',
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=logging.INFO)
