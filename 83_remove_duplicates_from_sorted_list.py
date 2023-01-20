# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            curr = remove_dup_list = ListNode(head.val)
            head = head.next
            while head != None:
                if head.val != remove_dup_list.val:
                    remove_dup_list.next = ListNode(head.val)
                    remove_dup_list = remove_dup_list.next
                head = head.next
            return curr