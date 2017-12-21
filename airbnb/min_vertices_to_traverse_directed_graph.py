import collections


def matrix2edges(edges):
    nodes = collections.defaultdict(set)
    n = len(edges)
    for i in range(n):
        for j in range(n):
            if edges[i][j]:
                nodes[i].add(j)
    return nodes


def direct_edge(edges):
    nodes = collections.defaultdict(set)
    for i, o in edges:
        nodes[i].add(o)
    return nodes


def get_min(edges, n):
    nodes = direct_edge(edges)

    order = []
    visited = set()

    def dfs(n):
        if n in visited:
            return
        visited.add(n)
        for next_n in nodes[n]:
            dfs(next_n)
        order.append(n)

    for i in range(n):
        dfs(i)

    unassigned = set(range(n))
    components = collections.defaultdict(set)

    def assign(n, component):
        if n not in unassigned:
            if n in components:
                components[component] |= components[n]
                del components[n]
            return
        unassigned.remove(n)
        components[component].add(n)
        for next_n in nodes[n]:
            assign(next_n, component)

    for num in reversed(order):
        assign(num, num)

    return components.keys()


print get_min([[0, 2], [1, 0]], 3)
'''
print get_min([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
               [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
'''
# print get_min([[0, 1], [1, 2], [2, 3], [3, 0], [2, 4], [4, 5], [5, 6], [6, 4], [7, 6], [7, 8]], 9)
