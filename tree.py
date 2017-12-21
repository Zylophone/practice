class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def bstDistance(values, n, node1, node2):
    # WRITE YOUR CODE HERE

    if node1 not in values or node2 not in values:
        return -1

    root = buildTree(values)
    if not root:
        return -1

    while root:
        if root.val > node1 and root.val > node2:
            root = root.left
        elif root.val < node1 and root.val < node2:
            root = root.right
        else:
            break

    d1 = getDepth(root, node1)
    d2 = getDepth(root, node2)
    if d1 == -1 or d2 == -1:
        return -1
    else:
        return d1 + d2


def getDepth(root, n):
    depth = 0
    while root:
        if root.val == n:
            return depth
        elif root.val > n:
            root = root.left
            depth += 1
        elif root.val < n:
            root = root.right
            depth += 1
    return -1


def buildTree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        node = root
        while node:
            if node.val < val:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
    return root


# print bstDistance([5, 6, 3, 1, 2, 4], 6, 2, 4)


def closestLocations(totalCrates, allLocations, truckCapacity):
    # WRITE YOUR CODE HERE
    l = sorted(allLocations, key=lambda loc: loc[0] * loc[0] + loc[1] * loc[1])
    return l[:truckCapacity]

print closestLocations(3, [[1,2], [3,4], [1,-1]],2)
