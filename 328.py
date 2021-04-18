# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Plan temporarily create two linked lists for odd and even nodes, and then merge them

        # Get heads for both linked lists
        evenHead = head

        if evenHead is None:
            return None

        oddHead = head.next
        if oddHead is None:
            return evenHead

        currEven = evenHead
        currOdd = oddHead

        # While more nodes exist
        while currOdd is not None and currOdd.next is not None:
            currEven.next = currOdd.next
            currOdd.next = currEven.next.next

            currEven = currEven.next
            currOdd = currOdd.next

        currEven.next = oddHead

        return evenHead
