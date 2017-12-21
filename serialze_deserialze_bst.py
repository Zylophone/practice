# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if not node:
                return []
            s = [str(node.val)] + helper(node.left) + helper(node.right)
            return s

        s = helper(root)
        return '|'.join(s)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        s = map(int, data.split('|'))

        def helper(s):
            if not s:
                return None
            node = TreeNode(int(s[0]))
            idx = 1
            while idx < len(s):
                if node.val < s[idx]:
                    break
                idx += 1
            node.left = helper(s[1:idx])
            node.right = helper(s[idx:])
            return node

        return helper(s)

node = TreeNode(2)
node.left = TreeNode(1)
node.right = TreeNode(3)
codec = Codec()
s = codec.serialize(node)
print codec.deserialize(s)
