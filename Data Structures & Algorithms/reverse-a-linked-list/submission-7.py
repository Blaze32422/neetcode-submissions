# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head 
        p = None
        while s:
            t = s.next
            s.next = p
            p = s
            s = t



        return p
