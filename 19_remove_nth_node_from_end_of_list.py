# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = result = head
        result = curr
        length = 0

        # get length of ListNode
        while head != None:
            head = head.next
            length += 1

        # Remove nth node from end of list
        position = length - n
        if position == 0:
            return curr.next
        elif position == length - 1:
            i = 0
            while curr != None:
                if i == position - 1:
                    curr.next = None
                else:
                    curr = curr.next
                i += 1
            return result
        else:
            i = 0
            while curr != None:
                if i == position - 1:
                    curr.next = curr.next.next
                    curr = curr.next
                    break
                else:
                    curr = curr.next
                i += 1
            return result