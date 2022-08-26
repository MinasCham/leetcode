# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current_node = head
        while (current_node and current_node.next) is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
                continue
            else:
                current_node = current_node.next
        return head