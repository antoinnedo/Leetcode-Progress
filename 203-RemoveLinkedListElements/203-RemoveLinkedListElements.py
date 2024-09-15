# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = ListNode(0)
        newHead.next = head
        dummy = newHead

        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
        
        return newHead.next

'''
Time: O(n) 
Explanation: traverse through the list

Space: O(1)
Explanation: only edit the list in place and create only 1 variable dummy and 1 node 0 pointing to head
'''
