# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = head
        second = head
        
        for _ in range(1, n):
            second = second.next
            if second.next == None:
                break
        
        if second.next == None:
            return first.next
        flag = 1
        while second.next:
            first = first.next
            second = second.next
            if flag:
                prev = head
                flag = 0
            else:
                prev = prev.next
#         new = head
        
#         while new.next != first:
#             new = new.next
        prev.next = first.next
        
        return head