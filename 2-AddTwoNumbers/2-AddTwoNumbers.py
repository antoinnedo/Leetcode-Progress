# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()  # Dummy node to simplify result construction
        current = result     # Pointer to the current node in the result list
        carry = 0           # Initialize carry to 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get the values of the current nodes (0 if the node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node for the current digit
            
            # Move pointers
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return result.next