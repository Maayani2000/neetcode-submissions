# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next  # 1. Save the next node before breaking the link
            curr.next = prev # 2. Reverse the link (point backward)
            
            # 3. Move pointers one step forward
            prev = curr
            curr = nxt
            
        return prev  # New head of the reversed list