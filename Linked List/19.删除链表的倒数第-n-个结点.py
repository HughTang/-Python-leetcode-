#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 方法一：暴力求解
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = dummy = ListNode(0,head)
        length = 0
        while cur.next:
            length += 1
            cur = cur.next
        # 在寻找待删除元素的前驱结点时，cur指向空头结点
        cur = dummy
        for _ in range(length-n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next
    
    # 方法二：快慢指针法
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = slow = fast = ListNode(0,head)
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
# @lc code=end

