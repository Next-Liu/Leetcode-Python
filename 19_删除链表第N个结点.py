# 删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return head.next
        temp = ListNode(0, head)
        i = temp
        j = head
        while n > 0:
            j = j.next
            n -= 1
        while j:
            i = i.next
            j = j.next
        i.next = i.next.next
        return temp.next


if __name__ == '__main__':
    e = ListNode(5)
    d = ListNode(4, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)
    print(Solution().removeNthFromEnd(a, 2))
