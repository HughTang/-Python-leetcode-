#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 判链表是否为空及链表是否只包含一个节点
        if not head or not head.next:
            return head
        
        # 新建一个链表，用于后续存储结果
        dummy = ListNode(0)
        # cur为新链表新增元素后的移动指针
        cur = dummy
        # p为遍历原链表的移动指针
        p = head
        # value用于存储原节点的数值，随着链表遍历而改变
        value = head.val
        
        # 元素是否重复的标志
        flag = 1
        while p.next:
            # 此处的第一个条件p.next是为了判断链表最后的元素是否是重复的
            while p.next and value == p.next.val:
                flag = 0
                p = p.next
            # flag为1时，说明未经上面的while循环，value是单一的
            if flag:
                '''
                将cur.next赋值给新创建的节点，节点的值为value,
                cur.next.next被初始化为None。
                这里需要说明的是，不能将p直接赋值给cur.next，
                因为对于原链表最后一个节点的判断，
                这种方法是不可行的。
                '''
                cur.next = ListNode(value)
                cur = cur.next
            # if用于判断当前p是否指向的是原链表最后一个节点
            if p.next:
                # value被重新赋值给下一个与原value不相等的节点值
                value = p.next.val
                p = p.next
                ''' 
                flag=1只能放在这里赋值，才会在判断原链表
                最后一个节点是否是重复值时发挥作用
                '''
                flag = 1
        '''
        （1）若flag == 1，则p指向的最后一个节点是不重复元素;
        （2）若flag == 0，则原链表最后的节点值是重复的，
            由于在创建新节点时最后节点的next已经初始化为None，
            因此不需要额外赋值操作。
        ''' 
        if flag:
            cur.next = p
        return dummy.next
# @lc code=end

