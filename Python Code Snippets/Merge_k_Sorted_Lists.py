import heapq

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

def mergeKLists(lists):
    heap=[]
    for l in lists:
        while l:
            heapq.heappush(heap,l.val)
            l=l.next
    dummy=ListNode()
    current=dummy
    while heap:
        current.next=ListNode(heapq.heappop(heap))
        current=current.next
    return dummy.next