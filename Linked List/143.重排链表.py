#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 判断链表是否为空
        if not head:
            return head

        # 新建列表用于存储每个节点
        nodes = list()
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        # i为列表的第一个元素下标，j为列表最后一个元素下标
        i = 0
        j = len(nodes)-1

        # while循环用于将列表中每个元素节点的重排
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            # i == j时为临界条件，用于处理奇数个节点的链表
            if i == j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        # 将重排列表的最后一个节点的next指向None
        nodes[i].next = None
# @lc code=end

