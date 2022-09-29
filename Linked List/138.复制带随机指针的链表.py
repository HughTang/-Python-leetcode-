#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 判断链表是否为空
        if not head:
            return head
        
        # 在原链表每个节点后面插入一个拷贝的节点，random初始为None
        ptr = head
        while ptr:
            new_node = Node(ptr.val,ptr.next,None)
            ptr.next = new_node
            ptr = new_node.next
        
        # 将每个新节点random进行赋值
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
        
        # 将新链表与旧链表分离
        old_list = head
        new_list = head.next
        # ptr保留新链表的第一个节点，用于后续返回
        ptr = head.next
        while old_list:
            old_list.next = new_list.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return ptr 
# @lc code=end

