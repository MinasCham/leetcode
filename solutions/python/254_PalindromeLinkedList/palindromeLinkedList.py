# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ll2list = []
        value = head
        while value is not None:
            ll2list.append(value.val)
            value = value.next
            
        if ll2list == ll2list[::-1]:
            return True
        
        return False
        
        