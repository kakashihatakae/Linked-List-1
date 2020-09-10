class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        def helper(head):
            if head.next == None:
                return head, head
            
            root, end = helper(head.next)
            end.next = head
            head.next = None
            return root, head
        
        to_ret, _  = helper(head)
        return to_ret