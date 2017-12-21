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
        vals = []

        def run(node):
            if node:
                vals.append(str(node.val))
                run(node.left)
                run(node.right)
            else:
                vals.append('#')

        run(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())

        def run():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = run()
            node.right = run()
            return node
        return run()




            # Your Codec object will be instantiated and called as such:
            # codec = Codec()
            # codec.deserialize(codec.serialize(root))
