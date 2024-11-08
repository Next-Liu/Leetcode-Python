class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        length = 0
        x = head
        while x:
            length += 1
            x = x.next

        dummy = ListNode(val=0, next=head)
        cur = dummy
        if length < 2:
            return head
        else:
            while length >= 2:
                length -= 2
                p = cur.next
                q = p.next
                p.next = q.next
                q.next = p
                cur.next = q
                cur = p
        return dummy.next


if __name__ == '__main__':
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    Node3 = ListNode(3)
    Node4 = ListNode(4)
    Node1.next = Node2
    Node2.next = Node3
    Node3.next = Node4
    s = Solution().swapPairs(Node1)
