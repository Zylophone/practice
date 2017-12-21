class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        def run(node, sum):
            if not node:
                return 0
            result = 0
            if sum == node.val:
                result += 1

            result += run(node.left, sum - node.val)
            result += run(node.right, sum - node.val)
            return result
        if not root:
            return 0
        result = 0
        result += run(root, sum)
        result += self.pathSum(root.left, sum)
        result += self.pathSum(root.right, sum)
        return result


node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node7 = TreeNode(3)
node8 = TreeNode(-2)
node9 = TreeNode(1)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.right = node9
print Solution().pathSum(node1, 8)
