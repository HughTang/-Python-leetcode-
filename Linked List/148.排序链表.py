#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    对链表自顶向下归并排序的过程如下:
    
    (1)找到链表的中点，以中点为分界，将链表拆分成两个子链表。
    寻找链表的中点可以使用快慢指针的做法，快指针每次移动2步，
    慢指针每次移动1步，当快指针到达链表末尾时，慢指针指向的
    链表节点即为链表的中点。
    (2)对两个子链表分别排序。
    (3)将两个排序后的子链表合并，得到完整的排序后的链表。可以
    使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行
    合并。

    上述过程可以通过递归实现。递归的终止条件是链表的节点个数小于
    或等于1，即当链表为空或者链表只包含1个节点时，不需要对链表
    进行拆分和排序。
'''    
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            # 两个递归的临界条件
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            # 定义快慢指针
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                # 条件再判断
                if fast != tail:
                    fast = fast.next
            # 确定链表中点
            mid = slow
            # 实施递归
            return merge(sortFunc(head,mid),sortFunc(mid,tail))
        
        # 合并两个有序链表的方法
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    cur.next = ListNode(l2.val)
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next
        
        # 返回sortFunc(head,None)
        return sortFunc(head,None) 
# @lc code=end

