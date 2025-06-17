class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def reverseKGroup(head,k):
    def reverse(head,k):
        prev,curr=None,head
        while k>0:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            k-=1
        return prev
    count=0
    curr=head
    while curr and count<k:
        curr=curr.next
        count+=1
    if count==k:
        reversed_head=reverse(head,k)
        head.next=reverseKGroup(curr,k)
        return reversed_head
    return head