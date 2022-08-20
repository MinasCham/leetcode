# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ll2list = []
        value = head
        while value is not None:
            ll2list.append(value.val)
            value = value.next
        middlelistindex = (len(ll2list) - 1) / 2 
        for i in range(middlelistindex): 
            res = head.next
            head = res
        if len(ll2list)%2==0:
            res = head.next
            head = res
        return head
        