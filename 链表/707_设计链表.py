class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.pre = ListNode()
        self.length = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        else:
            count = 0
            head = self.pre.next
            while head:
                if count == index:
                    return head.val
                else:
                    head = head.next
                    count += 1
            return head.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        l = ListNode(val, self.pre.next)
        self.pre.next = l
        self.length += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        pre = self.pre
        while pre.next:
            pre = pre.next
        pre.next = ListNode(val)
        self.length += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
        else:
            curret = self.pre
            s = ListNode(val)
            for i in range(index):
                curret = curret.next
            s.next = curret.next
            curret.next = s
            self.length += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return
        else:
            current = self.pre
            for i in range(index):
                current = current.next
            current.next = current.next.next
            self.length -= 1
