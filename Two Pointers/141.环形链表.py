#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while True:
            if not fast or not fast.next: 
                return False
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                return True
# @lc code=end

