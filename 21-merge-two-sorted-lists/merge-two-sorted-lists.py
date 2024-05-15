# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveAdding(list1, list2)
        
    def recursiveAdding(self, pointer1, pointer2):
        l = None
        if pointer1 and pointer2:
            if pointer1.val <= pointer2.val:
                l = ListNode(val=pointer1.val, next=self.recursiveAdding(pointer1.next, pointer2))
            else:
                l = ListNode(val=pointer2.val, next=self.recursiveAdding(pointer1, pointer2.next))
        elif pointer1:
            l = ListNode(val=pointer1.val, next=self.recursiveAdding(pointer1.next, pointer2))
        elif pointer2:
            l = ListNode(val=pointer2.val, next=self.recursiveAdding(pointer1, pointer2.next))
            
        return l
        
            