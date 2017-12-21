import sys


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = set()


def min_cost(lines, start, end, k):
    graph = {}
    for line in lines:
        route, price = line.split(',')
        ori, des = route.split('->')
        if ori not in graph:
            graph[ori] = Node(ori)
        if des not in graph:
            graph[des] = Node(des)

        ori_node, des_node = graph[ori], graph[des]
        ori_node.children.add((des_node, int(price)))

    best_route = ['']
    best_cost = [sys.maxint]

    def dfs(path, end, stop, cost):
        if stop < 0:
            return
        if end == path[-1]:
            if cost < best_cost[0]:
                best_route[0] = '->'.join(path)
                best_cost[0] = cost
            return
        for node, price in graph[path[-1]].children:
            path.append(node.val)
            dfs(path, end, stop - 1, cost + price)
            path.pop()

    dfs([start], end, k + 1, 0)
    return best_route[0]


lines = ['A->B,100', 'B->C,100', 'A->C,500']
print min_cost(lines, 'A', 'C', 1)
