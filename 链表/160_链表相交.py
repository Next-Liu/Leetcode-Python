# Definition for singly-linked list.
# 要求返回相交的节点，如果没有相交的节点，返回None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lenA = get_length(headA)
        lenB = get_length(headB)
        gap = abs(lenA - lenB)
        if lenA > lenB:
            while gap > 0:
                headA = headA.next
                gap -= 1
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        elif lenA < lenB:
            while gap > 0:
                headB = headB.next
                gap -= 1
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        else:
            while headA:
                if headA == headB:
                    return headA
                else:
                    headA = headA.next
                    headB = headB.next
        return None

