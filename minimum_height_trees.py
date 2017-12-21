import collections


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        children = collections.defaultdict(set)
        for f, t in edges:
            children[f].add(t)
            children[t].add(f)
        while len(children) > 2:
            leaves = [x for x in children if len(children[x]) == 1]
            for x in leaves:
                y = children[x].pop()
                children[y].remove(x)
                children.pop(x)
        return children.keys() if n != 1 else [0]
