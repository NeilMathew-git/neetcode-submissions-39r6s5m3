# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        ind = count - n
        curr = head 
        for i in range(ind - 1):
            curr = curr.next
            #takes us to prev of node we need to remove
        if ind == 0:
            return head.next
        if curr and curr.next:
            temp = curr.next.next
            if curr.next:
                curr.next.next = None
            curr.next = temp
            

        return head
        
        