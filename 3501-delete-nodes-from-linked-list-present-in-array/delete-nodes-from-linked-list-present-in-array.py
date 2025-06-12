# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        remove = set(nums)
        while head and head.val in remove:
            head = head.next
        while not head:
            return None
        curr = head 
        while curr.next:
            if curr.next.val in remove:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


        