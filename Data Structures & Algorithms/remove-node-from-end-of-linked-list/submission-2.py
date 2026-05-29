# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1

        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        print(prev, slow.val, slow.next)
        if prev and slow.next:
            prev.next = slow.next
        elif not prev:
            head = head.next
        else:
            prev.next = None
        return head