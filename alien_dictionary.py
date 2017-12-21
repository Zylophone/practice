import collections


class Solution(object):
    def alienOrder(self, words):
        parents, children = collections.defaultdict(set), collections.defaultdict(set)
        all_chars = set(list(''.join(words)))
        for first, second in zip(words, words[1:]):
            for i in range(min(len(first), len(second))):
                if first[i] != second[i]:
                    parents[second[i]].add(first[i])
                    children[first[i]].add(second[i])
                    break
        starts = all_chars - set(parents.keys())
        orders = []
        while starts:
            c = starts.pop()
            orders.append(c)
            for child in children[c]:
                parents[child].discard(c)
                if not parents[child]:
                    starts.add(child)
        if len(orders) != len(all_chars):
            return []
        else:
            return orders


print Solution().alienOrder(["za", "zb", "ca", "cb"])
