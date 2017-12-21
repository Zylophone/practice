class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev = None
        while head:
            tmp = head
            head = head.next
            tmp.next = prev
            prev = tmp
        return prev
    '''
    def recursion(self, head, prev=None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self.recursion(n, head)
    '''


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node4.next = node5
node3.next = node4
node2.next = node3
node1.next = node2

n = Solution().reverseList(node1)
while n:
    print n.val
    n = n.next

