class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def removeNthFromEnd(head,n):
    dummy=ListNode(0,head)
    slow=fast=dummy
    for _ in range(n+1):
        fast=fast.next
    while fast:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return dummy.next