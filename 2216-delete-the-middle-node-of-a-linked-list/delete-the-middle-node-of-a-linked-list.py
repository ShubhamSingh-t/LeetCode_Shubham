# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        n = len(arr)
        target = n//2
        arr[target - 1].next = arr[target].next
        return head

        