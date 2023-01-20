# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = ListNode()

        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                cur.next = list2
                list2, cur = list2.next, list2
            else:
                cur.next = list1
                list1, cur = list1.next, list1

        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2

        return head.next
