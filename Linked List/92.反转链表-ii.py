#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
        与[206]反转链表中的基本迭代方法一致，使用经典头插法，
        需要注意的是，要提前使用pre和succ指向第m个节点的前驱
        结点和第m个节点（第m个节点为新链表反转后的最后一个节
        点），使用dummy2存储反转后的链表节点，最后将pre.next
        指向dummy2.next，然后将succ.next指向第n个节点的后驱
        节点，最后返回dummy1.next（即head）即可。该方法的时间
        复杂度为O(N)，空间复杂度为O(1)。
    ''' 
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # 特殊情况if条件判断
        if not head or not head.next or left == right:
            return head
        # 新建哑结点dummy1，其后驱指向head
        dummy1 = ListNode(0,head)
        # pre：是precursor（前驱）的缩写，初始指向dummy1
        pre = dummy1
        # 经过下面的for循环，pre指向第m个节点的前驱结点
        for i in range(1,left):
            pre = pre.next

        # cur和succ同时指向第m个节点
        # succ：是successor（后继）的缩写
        cur = succ = pre.next
        # dummy2指向反转后的链表
        dummy2 = ListNode(0)
        # 头插法
        for i in range(right-left+1):
            tmp = cur.next
            cur.next = dummy2.next
            dummy2.next = cur
            cur = tmp
        
        # 将pre.next指向反转链表的第一个节点
        pre.next = dummy2.next
        # 将反转链表的最后一个节点指向第n个节点的后驱节点
        succ.next = cur
        # 返回dummy1.next，即head
        return dummy1.next     
# @lc code=end

