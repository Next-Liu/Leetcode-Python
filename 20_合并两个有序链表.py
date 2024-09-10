# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list2 is None:
            return list1
        elif list1 is None:
            return list2
        else:
            list3 = list4 = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    list3.next = list1
                    list3 = list3.next
                    list1 = list1.next
                else:
                    list3.next = list2
                    list3 = list3.next
                    list2 = list2.next
            while list1:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            while list2:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        return list4.next



