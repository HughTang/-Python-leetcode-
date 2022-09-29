#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
        使用栈：把所有数字压入栈中，再依次取出相加。计算过程中
        需要注意进位的情况。
    '''
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 定义两个链表作为栈，并将两个链表分别入栈
        s1 = list()
        s2 = list()
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        # dummy为结果链表的哑结点
        dummy = ListNode(0)
        # carry为进位标志
        carry = 0
        
        # 此处跳出循环的条件为s1、s2都为空且进位carry为0
        while s1 or s2 or carry !=0:
            # s1是否为空时对a的赋值操作
            a = 0 if not s1 else s1.pop()
            # s2是否为空时对b的赋值操作
            b = 0 if not s2 else s2.pop()
            # 相加结果存储在num中
            num = a + b + carry
            # 获取进位
            carry = num // 10
            # 获取进位后的一位数结果
            num %= 10
            # 经典头插法
            node = ListNode(num,dummy.next)
            dummy.next = node
        return dummy.next
# @lc code=end

