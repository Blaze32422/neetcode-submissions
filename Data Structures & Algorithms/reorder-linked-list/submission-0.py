# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        g = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        h = g
        while prev and g:
            
            z = g.next
            g.next = prev
            prev = prev.next
            g = g.next
            g.next = z
            g = g.next
    

        

        