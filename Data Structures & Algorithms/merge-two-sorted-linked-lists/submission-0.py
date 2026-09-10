# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        new_list = ListNode()
        curr_new = new_list

        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr_new.next = curr1
                curr1 = curr1.next
            else:
                curr_new.next = curr2
                curr2 = curr2.next
            curr_new = curr_new.next
    
        if curr1 is None:
            curr_new.next = curr2
        else:
            curr_new.next = curr1
        
        return new_list.next








