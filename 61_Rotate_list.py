# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            curr = head
            numberNode = 0
            # Get length of head
            while head != None:
                numberNode += 1
                head = head.next
            head = curr
            k %= numberNode
            for i in range(k):
                firstNode = ListNode()
                while head != None:
                    if head.next.next is None:
                        firstNode.next = ListNode(head.next.val)
                        firstNode.next.next = curr
                        curr = firstNode
                        head.next = None
                    head = head.next
                curr = head = curr.next
            return curr


# Referrence
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

#         if not head:
#             return head

#         length = 1
#         dummy = head

#         while dummy.next:
#             dummy = dummy.next
#             length += 1

#         position = k % length
#         if position == 0:
#             return head

#         cur = head

#         for _ in range(length - position - 1):
#             cur = cur.next

#         new_head = cur.next
#         cur.next = None
#         dummy.next = head

#         return new_head