# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/submissions/2070117973/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sentinel = ListNode(0, head)
        curr = sentinel

        while curr.next and curr.next.next:
            if curr.next.val == curr.next.next.val:
                while curr.next.next and curr.next.val == curr.next.next.val:
                    curr.next = curr.next.next

                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return sentinel.next