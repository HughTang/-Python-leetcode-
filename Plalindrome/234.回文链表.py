#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''
            此处借助字符串或者列表都可以，只不过字符串的连接符
            是+，列表则使用s.append(x)方法。
        '''
        vals = list()
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]
    

    # 要求：O(n) 时间复杂度和 O(1) 空间复杂度
    # 方法：切成两半，把后半段反转，然后比较两半是否相等
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = cur = ListNode(0,head)
        length = 0
        while cur.next:
            length += 1
            cur = cur.next
        cur = dummy
        for _ in range(length // 2):
            cur = cur.next
        # 奇数长度的链表则去掉最中间的节点
        if length % 2 == 1:
            cur.next = cur.next.next
        new_head = self.reverseList(cur.next)
        for _ in range(length // 2):
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True

    def reverseList(self, head: ListNode):
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
# @lc code=end

