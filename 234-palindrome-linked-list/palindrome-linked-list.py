# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        s, l = 0, len(nums)-1
        while(s<l):
            if(nums[s]==nums[l]):
                s+=1
                l-=1
            else:
                return False
        return True
        