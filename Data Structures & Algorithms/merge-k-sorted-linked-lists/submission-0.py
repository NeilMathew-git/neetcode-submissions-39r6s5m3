# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        min_heap = []
        dummy = ListNode()
        curr = dummy
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, index, node))

        while min_heap:
            smallest_val, smallest_index, smallest_node = heapq.heappop(min_heap)
            curr.next = smallest_node
            curr = curr.next
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, smallest_index, smallest_node.next))
                smallest_node = smallest_node.next
            
        return dummy.next
            


        