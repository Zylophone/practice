class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if root.val < p.val:
                succ = root
                root = root.right
            else:
                root = root.left
        return succ

