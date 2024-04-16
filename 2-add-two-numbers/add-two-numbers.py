# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(val=0, next=None)
        current = l3
        actual_sum = 0
        extra = 0
        finished = False
        
        # While lists still have elements
        while not finished:
            # Perform sum
            actual_sum = l1.val + l2.val + extra
            extra = 0
            # Calculate extra and actual sum
            if actual_sum >= 10:
                extra = actual_sum / 10
                actual_sum = actual_sum % 10
                
            
            # Add sum to solution
            current.val = int(actual_sum)
            current.next = ListNode(val=0, next=None)
            
            # If both lists are completely traversed, finish
            if l1.next is None and l2.next is None and extra == 0:
                current.next = None
                finished = True
            else:
                current = current.next
            
            # Traverse lists until done, after that value will be equivalent to 0
            if l1.next is not None:
                l1 = l1.next
            else:
                l1.val = 0
            if l2.next is not None:
                l2 = l2.next
            else:
                l2.val = 0
        
        return l3

            