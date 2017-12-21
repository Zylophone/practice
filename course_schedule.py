class Node(object):
    def __init__(self, val):
        self.val = val
        self.parents = set()
        self.children = set()


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses < 2:
            return True
        node_map = {}
        for to_num, from_num in prerequisites:
            from_node = node_map.get(from_num, Node(from_num))
            to_node = node_map.get(to_num, Node(to_num))
            from_node.children.add(to_node)
            to_node.parents.add(from_node)
            node_map[from_num] = from_node
            node_map[to_num] = to_node

        parent_set = set()
        for num, node in node_map.items():
            if not node.parents:
                parent_set.add(node)
                node_map.pop(num)

        while parent_set:
            node = parent_set.pop()
            for child in node.children:
                child.parents.remove(node)
                if not child.parents:
                    parent_set.add(child)
                    node_map.pop(child.val)
        return not node_map

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        node_map = {}
        for to_num, from_num in prerequisites:
            from_node = node_map.get(from_num, Node(from_num))
            to_node = node_map.get(to_num, Node(to_num))
            from_node.children.add(to_node)
            to_node.parents.add(from_node)
            node_map[from_num] = from_node
            node_map[to_num] = to_node
        res = []
        parent_set = set()
        for num, node in node_map.items():
            if not node.parents:
                parent_set.add(node)
                node_map.pop(num)

        while parent_set:
            node = parent_set.pop()
            res.append(node.val)
            for child in node.children:
                child.parents.remove(node)
                if not child.parents:
                    parent_set.add(child)
                    node_map.pop(child.val)
        if len(res) < numCourses:
            for i in range(0, numCourses):
                if i not in res:
                    res.append(i)
        return res if not node_map else []