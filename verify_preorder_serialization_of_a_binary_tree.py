class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-2:] == ['#', '#'] and stack[-3] != '#':
                stack = stack[:-3]
                stack.append('#')

        return stack == ['#']

    def isValidSerialization1(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        diff = 1
        for node in preorder.split(','):
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0
