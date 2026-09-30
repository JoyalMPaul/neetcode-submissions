# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        cur = l1
        while cur:
            num1 += str(cur.val)
            cur = cur.next

        num2 = ""
        cur = l2
        while cur:
            num2 += str(cur.val)
            cur = cur.next

        total = int(num1[::-1]) + int(num2[::-1])
        total = str(total)[::-1]

        l3 = ListNode(int(total[0]))
        cur = l3
        for digit in total[1:]:
            cur.next = ListNode(int(digit))
            cur = cur.next
        return l3